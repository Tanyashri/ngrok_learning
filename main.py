from fastapi import FastAPI
from db import engine, DATABASE_URL
from models import Base
from routes.user_routes import router as user_router
from sqlalchemy import create_engine
from dotenv import load_dotenv
load_dotenv()
import os 

app = FastAPI()

app.include_router(user_router, prefix="/users")

engine=create_engine(DATABASE_URL)
Base.metadata.create_all(engine)

@app.get("/")
def read_root():
    return {"Hello": "World"}

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8000)