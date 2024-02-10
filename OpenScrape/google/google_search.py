import requests
from time import sleep
from bs4 import BeautifulSoup
from ..user_agents import get_useragent
import urllib


def _req(search, results, lang, start, timeout):
    with requests.get(
        url="https://www.google.com/search",
        headers={"User-Agent": get_useragent()},
        params={
            "q": search,
            "num": results + 2,
            "hl": lang,
            "start": start,
        },
        timeout=timeout,
    ) as resp:
        resp.raise_for_status()
        return resp.text


def search(search, num_results=10, lang="en", sleep_interval=0, timeout=5) -> list:
    """
    Synchronously search the Google search engine and return the search results.

    This function sends a search request to Google, parses the HTML response, and
    extracts the title, link, and description of each search result. It returns a list
    of dictionaries, each representing a search result.

    Args:
        search (str): The search search to query.
        num_results (int, optional): The number of search results to return. Defaults to 10.
        lang (str, optional): The language for the search results. Defaults to 'en'.
        sleep_interval (int, optional): The number of seconds to wait between each request. Defaults to 0.
        timeout (int, optional): The number of seconds before the request times out. Defaults to 5.

    Returns:
        list[dict]: A list of dictionaries, each representing a search result. Each dictionary contains
                    the 'title', 'link', and 'description' of a search result.

    Raises:
        requests.exceptions.RequestException: If the request to Google fails.
    """

    escaped_search = urllib.parse.quote_plus(search)

    result_google_search = []
    start = 0
    while start < num_results:
        resp_text = _req(escaped_search, num_results - start, lang, start, timeout)
        soup = BeautifulSoup(resp_text, "html.parser")
        result_block = soup.find_all("div", attrs={"class": "g"})
        if len(result_block) == 0:
            start += 1
        for result in result_block:
            link = result.find("a", href=True)
            title = result.find("h3")
            description_box = result.find("div", {"style": "-webkit-line-clamp:2"})
            if description_box:
                description = description_box.text
                if link and title and description:
                    result_google_search.append(
                        {
                            "title": title.text,
                            "link": link["href"],
                            "description": description,
                        }
                    )
                    if len(result_google_search) >= num_results:
                        return result_google_search
        sleep(sleep_interval)
        if start == 0:
            return []
    return result_google_search
