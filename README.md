# OpenScrape

OpenScrape is a Python library for scraping data from various services. Currently, it supports Google search, Nikkei stock prices, and real-time anime rankings in Japan (d Anime Ranking). In addition, it now supports scraping from most websites. Going forward, we plan to add features based on user feedback. Please raise an ISSUE on GitHub for any specific requests or problems.

## Features

- Asynchronous scraping: OpenScrape uses Python's asyncio to perform non-blocking I/O operations, making it efficient for large-scale scraping tasks.
- Support for multiple services: Currently, OpenScrape supports scraping Google search results, Nikkei stock prices, and real-time anime rankings in Japan (d Anime Ranking).
- Synchronous scraping: OpenScrape also supports synchronous operations, providing flexibility in how the library is used.

## Future Plans

- More services: We plan to extend OpenScrape to be able to scrape from various other services. Please raise an ISSUE on GitHub for any specific requests or problems.

## Installation

You can install OpenScrape using pip:

```bash
pip install git+https://github.com/umaxiaotian/OpenScrape.git@main
```

## Usage

Below is an example of using OpenScrape to scrape any website:

### Asynchronous

```python
import asyncio
from OpenScrape import any_websites

async def main():
    result = await any_websites.async_crawl("https://www.bloomberg.co.jp/news/articles/2024-01-05/S6PKIWT0AFB400")
    print(result)

if __name__ == "__main__":
    asyncio.run(main())
```

This script asynchronously scrapes the specified URL and prints the title and body text of the page.

### Synchronous

```python
from OpenScrape import any_websites

def main():
    result = any_websites.crawl("https://www.bloomberg.co.jp/news/articles/2024-01-05/S6PKIWT0AFB400")
    print(result)

if __name__ == "__main__":
    main()
```

This script synchronously scrapes the specified URL and prints the title and body text of the page.

Sample codes for Jupyter can be found at [this link](https://github.com/umaxiaotian/OpenScrape/tree/main/example).

## Note
When crawling from this library, please refer to the robots.txt of each website.
| Website | Robots.txt URL |
| --- | --- |
| Nikkei | [https://www.nikkei.com/robots.txt](https://www.nikkei.com/robots.txt) |
| Google LLC | [https://www.google.com/robots.txt](https://www.google.com/robots.txt) |
| d Anime Store | [https://animestore.docomo.ne.jp/robots.txt](https://animestore.docomo.ne.jp/robots.txt) |
| Bing | [https://bing.com/robots.txt](https://bing.com/robots.txt) |

## Contribution

Contributions to OpenScrape are welcome! For details, please see the [Contribution Guide](CONTRIBUTING.md).

## License

OpenScrape is licensed under the [MIT License](LICENSE).