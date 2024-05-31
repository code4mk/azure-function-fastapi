from fastapi import APIRouter, status
from fastapi.responses import JSONResponse

# Create a api router
router = APIRouter()

# Health check route
@router.get("/")
async def health_check():
    data =  {"status": "ok"}
    return JSONResponse(content=data, status_code=status.HTTP_200_OK)