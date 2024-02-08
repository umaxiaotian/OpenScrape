"""Google検索用"""
from time import sleep
from bs4 import BeautifulSoup
from aiohttp import ClientSession
from .user_agents import get_useragent
import urllib


async def _req(session, term, results, lang, start, timeout):
    async with session.get(
        url="https://www.google.com/search",
        headers={"User-Agent": get_useragent()},
        params={
            "q": term,
            "num": results + 2,
            "hl": lang,
            "start": start,
        },
        timeout=timeout,
    ) as resp:
        resp.raise_for_status()
        return await resp.text()


async def search(
    term, num_results=10, lang="en", advanced=False, sleep_interval=0, timeout=5
):
    """Google検索エンジンスクレイプ"""
    escaped_term = urllib.parse.quote_plus(term)
    result_google_search = []
    start = 0
    async with ClientSession() as session:
        while start < num_results:
            resp_text = await _req(
                session, escaped_term, num_results - start, lang, start, timeout
            )
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
                    start += 1
                    result_google_search.append(
                        {
                            "title": title.text,
                            "link": link["href"],
                            "description": description,
                        }
                    )
            sleep(sleep_interval)
            if start == 0:
                return []
    return result_google_search
