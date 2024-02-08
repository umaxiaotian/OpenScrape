# OpenScrape API

OpenScrape is a powerful application that integrates with various services to scrape information. The scraped data is provided through a REST API. 

## Version
The current version of this API is 1.0.

## Endpoints

### GET /search/google

This endpoint allows you to search Google and retrieve the results.

#### Request

The request body should be a JSON object with the following properties:

- `search` (string, required): The content to search for.
- `num_results` (integer, optional, default: 5): The number of search results to retrieve.
- `lang` (string, optional, default: "ja"): The language to use for the search.
- `sleep_interval` (integer, optional, default: 1): The wait time (in seconds) between search requests.

Example:

```json
{
    "search": "OpenAI",
    "num_results": 10,
    "lang": "en",
    "sleep_interval": 2
}
```

## Example Request with cURL

You can use cURL to send a request to the `/search/google` endpoint. Here is an example:

```bash
curl --location --request GET 'http://127.0.0.1:8080/search/google' \
--header 'Content-Type: application/json' \
--data '{
  "search": "umaxiaotian",
  "num_results": 3,
  "lang": "ja",
  "sleep_interval":5
}'
```

In this example, we are searching for "umaxiaotian", and we want to retrieve 3 results. We are using Japanese for the search, and we are waiting for 5 seconds between each search request.


## Warning
Please exercise caution and ensure that you only use OpenScrape API for research purposes. Be mindful of the terms of service of websites to avoid any violation related to web scraping. Additionally, take into consideration that many websites employ security measures to prevent scraping activities. Adjust the sleep_interval setting accordingly to avoid sending an excessive number of requests or being blocked.

If you have any further questions or concerns, please let me know.