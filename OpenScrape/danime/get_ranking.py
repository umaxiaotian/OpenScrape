import json
import requests
from ..user_agents import get_useragent


def get_anime_rank(num_results: int = 1) -> list:
    """
    Retrieves the top d-anime rankings.

    Args:
        num_results (int): Number of rankings to retrieve (default is 1).

    Returns:
        list: List of dictionaries containing the rank and title of each anime.

    Raises:
        None

    Example:
        >> get_anime_rank(5)
        [{'rank': 1, 'title': 'Attack on Titan'},
         {'rank': 2, 'title': 'My Hero Academia'},
         {'rank': 3, 'title': 'Demon Slayer'},
         {'rank': 4, 'title': 'One Piece'},
         {'rank': 5, 'title': 'Naruto'}]
    """

    anime_rank_array = []

    # アニメランキングを取得する
    response = requests.get(
        url="https://anime.dmkt-sp.jp/animestore/rest/WS000103?rankingType=01",
        headers={"User-Agent": get_useragent()},
    )
    data = json.loads(response.text)

    # アニメランキングを0番目の配列から順番に格納
    for i in range(0, num_results):
        title = data["data"]["workList"][i]["workInfo"]["workTitle"]
        # アニメのタイトルを格納します。
        anime_rank_array.append({"rank": i + 1, "title": title})

    return anime_rank_array
