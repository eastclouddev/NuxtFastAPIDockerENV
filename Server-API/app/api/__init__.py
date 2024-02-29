from fastapi import APIRouter
from .endpoints import some_endpoint

router = APIRouter()
router.include_router(some_endpoint.router, prefix="/somepath", tags=["some"])
