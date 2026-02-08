from fastapi import APIRouter
import os

router = APIRouter()

@router.get("/entropy/health")
def entropy_health():
    """
    Check if entropy sources are available.
    """
    # In a real system, we'd check /dev/random or camera availability
    return {"status": "ok", "system_random": True}