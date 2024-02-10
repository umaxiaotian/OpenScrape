import aiohttp
from bs4 import BeautifulSoup
from ..user_agents import get_useragent


async def search(search: str, num_results: int) -> list:
    """
    Searches Bing with the specified search term and retrieves a specified number of search results.

    Args:
        search (str): The search term.
        num_results (int): The number of search results to retrieve.

    Returns:
        list: A list of search results. Each search result is a dictionary containing a title, a link, and a description.

    Raises:
        aiohttp.ClientError: If the GET request fails.
        bs4.BeautifulSoup.Error: If HTML parsing fails.

    Note:
        This function depends on the HTML structure of Bing. If Bing changes its structure, this function may not work correctly.
        Also, be careful not to violate Bing's terms of use.
    """
    url = "https://www.bing.com/search"
    params = {
        "q": search,
    }
    results_list = []
    async with aiohttp.ClientSession() as session:
        while len(results_list) < num_results:
            async with session.get(
                url, headers={"User-Agent": get_useragent()}, params=params
            ) as response:
                response_text = await response.text()
            soup = BeautifulSoup(response_text, "html.parser")
            results = soup.find_all("li", class_="b_algo")
            entity_results = soup.find_all("li", class_="b_entityTP")

            for result in entity_results:
                if len(results_list) >= num_results:
                    break
                title = result.find("h2").text
                link_tag = result.find("a")
                link = (
                    link_tag["href"] if link_tag and "href" in link_tag.attrs else None
                )
                description = (
                    result.find("div", class_="b_entitySubText").text
                    if result.find("div", class_="b_entitySubText")
                    else ""
                )
                results_list.append(
                    {"title": title, "link": link, "description": description}
                )

            for result in results:
                if len(results_list) >= num_results:
                    break
                title = result.find("h2").text
                link_tag = result.find("a")
                link = (
                    link_tag["href"] if link_tag and "href" in link_tag.attrs else None
                )
                description = result.find("p").text if result.find("p") else ""
                results_list.append(
                    {"title": title, "link": link, "description": description}
                )
            next_page = soup.find("a", class_="sb_pagN")
            if next_page:
                url = "https://www.bing.com" + next_page["href"]
            else:
                break
    return results_list
