from dotenv import load_dotenv
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from actuator.utils.logger import setup_logger

# Routers
from actuator.router import router as actuator_router

load_dotenv()
setup_logger()


app = FastAPI(
    description="Sammy Actuator API",
    title="Sammy Actuator API",
    version="0.1.0",
    contact={
        "name": "Sammy Actuator API",
        "url": "https://sammy.club",
    },
)

app.add_middleware(
    CORSMiddleware,
    # ToDo: In prod replace
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Routers
app.include_router(actuator_router)

if __name__ == "__main__":
    import uvicorn

    uvicorn.run(app, host="0.0.0.0", port=8001, log_level="debug")
