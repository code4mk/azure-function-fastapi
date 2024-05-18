from fastapi import APIRouter, status, Request
from fastapi.responses import JSONResponse

# Create a FastAPI app
router = APIRouter()

# root index
@router.get("/")
async def root_index(request: Request):
    data = {
      'message': 'azure function project is running...'
    }
    return JSONResponse(content=data, status_code=status.HTTP_200_OK)
    