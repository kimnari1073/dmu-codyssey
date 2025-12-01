# main.py
from fastapi import FastAPI
from question_router import router as question_router

app = FastAPI()
app.include_router(question_router)
