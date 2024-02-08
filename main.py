from fastapi import FastAPI
from router import search_router

app = FastAPI(
    title="OpenScrape",
    description="This application can integrate with various services and scrape information. The scraped data is provided through a REST API.",
    version="1.0",
)

app.include_router(search_router)

if __name__ == "__main__":
    import uvicorn

    uvicorn.run(app, host="127.0.0.1", port=8080)
