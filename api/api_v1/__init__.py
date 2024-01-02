from fastapi import APIRouter

from .urls.views import router as urls_router


router = APIRouter()
router.include_router(urls_router, prefix="/urls")
