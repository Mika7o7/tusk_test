from pydantic import BaseModel
from typing import Optional, Dict

class ComplaintCreate(BaseModel):
    text: str

class ComplaintResponse(BaseModel):
    id: int
    status: str
    sentiment: str
    category: str
    geo: Optional[Dict[str, str]] = None  # Добавим поле гео-данных
