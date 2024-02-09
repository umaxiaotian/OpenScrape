# OpenScrape

OpenScrape is a Python library for scraping data from various services. While it currently specializes in Google search, we plan to expand its capabilities to scrape from a variety of other services.

## Features

- Asynchronous scraping: OpenScrape uses Python's asyncio to perform non-blocking I/O operations, making it efficient for large scale scraping tasks.
- Google search: Currently, OpenScrape supports scraping search results from Google. You can specify the search term, number of results, and language.

## Future Plans

- More services: We plan to extend OpenScrape to support scraping from a variety of other services.
- Synchronous scraping: While OpenScrape currently only supports asynchronous operations, we plan to add support for synchronous operations in the future.

## Installation

You can install OpenScrape using pip:

```bash
pip install OpenScrape
```

## Usage

Here is an example of how to use OpenScrape to perform a Google search:

```python
import asyncio
from OpenScrape import google

async def main():
    result = await google.asyncsearch(term="test", num_results=2, lang="ja")
    print(result)

if __name__ == "__main__":
    asyncio.run(main())
```

This script performs an asynchronous Google search for the term "test", and prints the first two results in Japanese.

## Contributing

We welcome contributions to OpenScrape! Please see our [contributing guide](CONTRIBUTING.md) for more details.

## License

OpenScrape is licensed under the [MIT License](LICENSE).