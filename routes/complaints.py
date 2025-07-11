from fastapi import APIRouter, HTTPException, Depends, Request, Query, Path
from sqlalchemy.orm import Session
from datetime import datetime, timedelta

from database import get_db
from models import Complaint
from schemas import ComplaintCreate, ComplaintResponse
from services.sentiment import analyze_sentiment
from services.categorizer import categorize_text
from services.spam import check_spam
from services.geo import get_geo_data

router = APIRouter()

@router.post("/complaints", response_model=ComplaintResponse)
async def create_complaint(complaint: ComplaintCreate, request: Request, db: Session = Depends(get_db)):
    if await check_spam(complaint.text):
        raise HTTPException(status_code=400, detail="Жалоба определена как спам.")

    sentiment = await analyze_sentiment(complaint.text)
    category = await categorize_text(complaint.text)

    new_complaint = Complaint(
        text=complaint.text,
        sentiment=sentiment,
        category=category,
    )
    db.add(new_complaint)
    db.commit()
    db.refresh(new_complaint)

    client_ip = "185.192.246.42"  # request.client.host
    geo_data = await get_geo_data(client_ip)

    return ComplaintResponse(
        id=new_complaint.id,
        status=new_complaint.status,
        sentiment=new_complaint.sentiment,
        category=new_complaint.category,
        geo=geo_data
    )

@router.get("/complaints/open")
def get_open_complaints(
    since: str = Query(..., description="Например: 1h, 30m, 2d"),
    db: Session = Depends(get_db)
):
    now = datetime.utcnow()

    value = int(since[:-1])
    unit = since[-1]

    if unit == "h":
        delta = timedelta(hours=value)
    elif unit == "m":
        delta = timedelta(minutes=value)
    elif unit == "d":
        delta = timedelta(days=value)
    else:
        raise HTTPException(status_code=400, detail="Неверный формат 'since'")

    cutoff = now - delta

    complaints = db.query(Complaint).filter(
        Complaint.status == "open",
        Complaint.timestamp >= cutoff
    ).all()

    return [
        {
            "id": c.id,
            "text": c.text,
            "status": c.status,
            "timestamp": c.timestamp,
            "sentiment": c.sentiment,
            "category": c.category
        }
        for c in complaints
    ]


@router.put("/complaints/{complaint_id}/close")
def close_complaint(
    complaint_id: int = Path(...),
    db: Session = Depends(get_db)
):
    complaint = db.query(Complaint).filter(Complaint.id == complaint_id).first()

    if not complaint:
        raise HTTPException(status_code=404, detail="Жалоба не найдена")

    complaint.status = "closed"
    db.commit()

    return {"message": f"Жалоба {complaint_id} закрыта"}
