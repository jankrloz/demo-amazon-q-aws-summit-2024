from fastapi import FastAPI

from app.routers.users import router as users_router

app = FastAPI()

app.include_router(users_router)


@app.get("/")
async def root():
    return {"message": "👋 Hello AWS Summit 2024 CDMX!"}
