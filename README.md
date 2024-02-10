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