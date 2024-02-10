import aiohttp
from bs4 import BeautifulSoup

async def search(query:str, num_results:int):
    """
    Searches Bing with the specified search term and retrieves a specified number of search results.

    Args:
        query (str): The search term.
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
        "q": query,
        "count": num_results
    }
    async with aiohttp.ClientSession() as session:
        async with session.get(url, params=params) as response:
            text = await response.text()
            soup = BeautifulSoup(text, 'html.parser')
            results = soup.find_all('li', class_='b_algo')
            results_list = []
            for result in results:
                title = result.find('h2').text
                link = result.find('a')['href']
                description = result.find('p').text if result.find('p') else ''
                results_list.append({
                    "title": title,
                    "link": link,
                    "description": description
                })
    return results_list
