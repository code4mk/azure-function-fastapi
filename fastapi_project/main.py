import os
from fastapi import FastAPI
from dotenv import load_dotenv
from fastapi.middleware.cors import CORSMiddleware
from fastapi_project.api import root_index

# Load .env file
load_dotenv()

# Get the value of LOAD_SQL_PROJECT environment variable
load_sql_project = os.getenv('LOAD_SQL_PROJECT', 'false').lower() in ('true', '1', 't', 'y', 'yes')
#load_sql_project = os.getenv('LOAD_SQL_PROJECT', 'true').lower() in ('true', '1', 't', 'y', 'yes')

def create_application():
    application = FastAPI()
    
    # Include the root index router
    application.include_router(root_index.router)
    
    
    if load_sql_project == True:
        print("SQL_PROJECT is enabled")
        # Include additional routers if LOAD_SQL_PROJECT is enabled
        from fastapi_project.api.v1 import user
        application.include_router(user.router)
    
    # Add CORS middleware
    # In production, replace the "*" with the actual frontend URL
    application.add_middleware(
        CORSMiddleware,
        allow_origins=["*"],  # Replace ["*"] with your frontend URL in production
        allow_credentials=True,
        allow_methods=["GET", "POST", "PUT", "DELETE"],
        allow_headers=["*"],
    )
    
    return application

# Create the FastAPI application
app = create_application()
