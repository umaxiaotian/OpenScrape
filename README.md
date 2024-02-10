# OpenScrape

OpenScrape is a Python library for scraping data from various services. Currently, it supports Google search, Nikkei stock prices, and real-time anime rankings in Japan (d Anime Ranking). We plan to expand its capabilities to scrape from a variety of other services in the future.

## Features

- Asynchronous scraping: OpenScrape uses Python's asyncio to perform non-blocking I/O operations, making it efficient for large scale scraping tasks.
- Support for multiple services: Currently, OpenScrape supports scraping search results from Google, Nikkei stock prices, and real-time anime rankings in Japan (d Anime Ranking).
- Synchronous scraping: OpenScrape now also supports synchronous operations, allowing for more flexibility in how you use the library.

## Future Plans

- More services: We plan to extend OpenScrape to support scraping from a variety of other services.

## Installation

You can install OpenScrape using pip:

```bash
pip install git+https://github.com/umaxiaotian/OpenScrape.git@main
```

## Usage

Here are examples of how to use OpenScrape to perform a Google search:

### Asynchronous

```python
import asyncio
from OpenScrape import google

async def main():
    result = await google.async_search(search="test", num_results=2, lang="ja")
    print(result)

if __name__ == "__main__":
    asyncio.run(main())
```

This script performs an asynchronous Google search for the search "test", and prints the first two results in Japanese.

### Synchronous

```python
from OpenScrape import google

def main():
    result = google.search(search="test",num_results=1,lang="ja")
    print(result)

if __name__ == "__main__":
    main()
```

This script performs a synchronous Google search for the search "test", and prints the first result in Japanese.

Sample codes for Jupyter can be found at this [link](https://github.com/umaxiaotian/OpenScrape/tree/main/example).

## Warning
Please refer to the robots.txt of each website when crawling from this library.
| Website | Robots.txt URL |
| --- | --- |
| Nikkei | [https://www.nikkei.com/robots.txt](https://www.nikkei.com/robots.txt) |
| Google LLC | [https://www.google.com/robots.txt](https://www.google.com/robots.txt) |
| d Anime Store | [https://animestore.docomo.ne.jp/robots.txt](https://animestore.docomo.ne.jp/robots.txt) |
| bing | [https://bing.com/robots.txt](https://bing.com/robots.txt) |

## Contributing

We welcome contributions to OpenScrape! Please see our [contributing guide](CONTRIBUTING.md) for more details.

## License

OpenScrape is licensed under the [MIT License](LICENSE).
