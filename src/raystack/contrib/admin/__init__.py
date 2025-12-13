from raystack.compat import APIRouter, RedirectResponse, Request

from .urls import router as urls_router

from raystack.middlewares import PermissionMiddleware


router = APIRouter()

# Add /admin redirect BEFORE mounting urls_router
# This ensures it's checked before mount("/admin", ...) intercepts the request
@router.get("/admin")
async def admin_redirect(request: Request):
    """Redirect /admin to /admin/"""
    return RedirectResponse(url="/admin/", status_code=301)

# router.include_router(urls_router, prefix="/admin", include_in_schema=False)
router.include_router(urls_router, prefix="/admin", tags=["restricted"])
