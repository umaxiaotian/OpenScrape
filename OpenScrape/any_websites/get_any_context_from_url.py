import json
from bs4 import BeautifulSoup
import requests
from ..user_agents import get_useragent


def crawl(url: str) -> dict:
    """
    Crawls the web page of the specified URL, extracts the title and body text,
    and returns them as a JSON-formatted string.

    Args:
        url (str): The URL of the web page to crawl.

    Returns:
        str: A JSON-formatted string containing the title and body text of the web page.

    """
    response = requests.get(
        url=url,
        headers={"User-Agent": get_useragent()},
    )

    # Get the HTML content and explicitly specify the encoding
    html = response.content.decode("utf-8")
    soup = BeautifulSoup(html, "html.parser")

    # Get the title
    title = soup.title.string

    # Get the body text
    paragraphs = soup.find_all("p")
    text = " ".join([p.get_text() for p in paragraphs])

    # Output in JSON format
    return {"title": title, "text": text}
