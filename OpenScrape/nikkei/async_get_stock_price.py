import aiohttp
from bs4 import BeautifulSoup
from .user_agents import get_useragent


async def get_current_value(scode):
    """
    Get the current stock information from the Nikkei website.

    Args:
        scode (str): The stock code to get the information.

    Returns:
        dict: A dictionary containing the stock information. The keys are:
            - 'company_name': The name of the company.
            - 'current_price': The current price of the stock.
            - 'previous_day_comparison': The comparison with the previous day.
            - 'open_price': The opening price of the stock.
            - 'high_price': The highest price of the stock.
            - 'low_price': The lowest price of the stock.
            - 'volume': The volume of the stock.
            - 'expected_per': The expected price-earnings ratio.
            - 'expected_dividend_yield': The expected dividend yield.
    """
    url = "https://www.nikkei.com/nkd/company/"
    async with aiohttp.ClientSession() as session:
        async with session.get(
            url, headers={"User-Agent": get_useragent()}, params={"scode": scode}
        ) as response:
            text = await response.text()
            soup = BeautifulSoup(text, "html.parser")
            # 会社名を取得
            company_name = soup.find("h1", {"class": "m-headlineLarge_text"}).get_text(
                strip=True
            )

            # 現在値と時間を取得
            current_price = soup.find(
                "dd", {"class": "m-stockPriceElm_value now"}
            ).get_text(strip=True)

            # 前日比を取得
            previous_day_comparison = soup.find(
                "dd", {"class": "m-stockPriceElm_value comparison plus"}
            ).get_text(strip=True)

            # 始値
            open_price = (
                soup.find("span", text=lambda x: x and "始値" in x)
                .find_next("span", class_="m-stockInfo_detail_value")
                .get_text(strip=True)
            )

            # 高値
            high_price = (
                soup.find("span", text=lambda x: x and "高値" in x)
                .find_next("span", class_="m-stockInfo_detail_value")
                .get_text(strip=True)
            )

            # 安値
            low_price = (
                soup.find("span", text=lambda x: x and "安値" in x)
                .find_next("span", class_="m-stockInfo_detail_value")
                .get_text(strip=True)
            )

            # 売買高
            volume = (
                soup.find("a", href="/markets/ranking/page/?ba=00&bd=vol")
                .find_next("span", class_="m-stockInfo_detail_value")
                .get_text(strip=True)
            )

            # 予想PER
            expected_per = (
                soup.find("a", href="/markets/ranking/page/?ba=00&bd=perlow_d")
                .find_next("span", class_="m-stockInfo_detail_value")
                .get_text(strip=True)
            )

            # 予想配当利回り
            expected_dividend_yield = (
                soup.find("a", href="/markets/ranking/page/?ba=00&bd=dividend")
                .find_next("span", class_="m-stockInfo_detail_value")
                .get_text(strip=True)
            )

            # JSON形式で返す
            return {
                "company_name": company_name,
                "current_price": current_price,
                "previous_day_comparison": previous_day_comparison,
                "open_price": open_price,
                "high_price": high_price,
                "low_price": low_price,
                "volume": volume,
                "expected_per": expected_per,
                "expected_dividend_yield": expected_dividend_yield,
            }


async def get_stock_history(scode):
    """
    Get the stock history from the Nikkei website.

    Args:
        scode (str): The stock code to get the information.

    Returns:
        list: A list of dictionaries containing the stock history. Each dictionary has the following keys:
            - 'date': The date of the stock data.
            - 'open_price': The opening price of the stock.
            - 'high_price': The highest price of the stock.
            - 'low_price': The lowest price of the stock.
            - 'close_price': The closing price of the stock.
            - 'volume': The volume of the stock.
            - 'adjusted_close_price': The adjusted closing price of the stock.
    """
    url = "https://www.nikkei.com/nkd/company/history/dprice/"
    params = {"scode": scode, "ba": "1"}

    async with aiohttp.ClientSession() as session:
        async with session.get(url, params=params) as response:
            text = await response.text()
            soup = BeautifulSoup(text, "html.parser")
            table = soup.find("table", class_="w668")
            rows = table.find_all("tr")

            history = []

            for row in rows[1:]:  # ヘッダーをスキップする。
                data = row.find_all("td")
                date = row.find("th").get_text(strip=True)
                open_price = data[0].get_text(strip=True)
                high_price = data[1].get_text(strip=True)
                low_price = data[2].get_text(strip=True)
                close_price = data[3].get_text(strip=True)
                volume = data[4].get_text(strip=True)
                adjusted_close_price = data[5].get_text(strip=True)

                history.append(
                    {
                        "date": date,
                        "open_price": open_price,
                        "high_price": high_price,
                        "low_price": low_price,
                        "close_price": close_price,
                        "volume": volume,
                        "adjusted_close_price": adjusted_close_price,
                    }
                )

            return history
