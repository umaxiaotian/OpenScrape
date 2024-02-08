from schemas import SearchRequest
from .google_search import search

async def google_search(search_request: SearchRequest):
    search_result = await search(
        term=search_request.search,
        num_results=search_request.num_results,
        lang=search_request.lang,
        sleep_interval=search_request.sleep_interval,
    )

    result = {
        "type": "google",
        "result": search_result
    }

    return result
