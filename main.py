from fastapi import FastAPI
from database import Base, engine
from routes.complaints import router as complaints_router

Base.metadata.create_all(bind=engine)

app = FastAPI()

app.include_router(complaints_router)
