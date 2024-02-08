from fastapi import APIRouter
from schemas import SearchRequest
from google import google_search

search_router = APIRouter()


@search_router.get("/search/google")
async def search(search_request: SearchRequest):
    return await google_search(search_request)
