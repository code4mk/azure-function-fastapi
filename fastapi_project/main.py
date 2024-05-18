from fastapi import FastAPI
from dotenv import load_dotenv
from fastapi.middleware.cors import CORSMiddleware
from fastapi_project.api import root_index
# Load .env file
load_dotenv()

def create_application():
    application = FastAPI()
    
    # Include routers
    application.include_router(root_index.router)
    
    # Allow all origins (not recommended for production)
    # Replace the "*" with the actual frontend URL in production
    application.add_middleware(
        CORSMiddleware,
        allow_origins=["*"],  # Replace ["*"] with your frontend URL in production
        allow_credentials=True,
        allow_methods=["GET", "POST", "PUT", "DELETE"],
        allow_headers=["*"],
    )
    
    return application

app = create_application()