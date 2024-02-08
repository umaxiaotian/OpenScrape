# OpenScrape API

OpenScrapeは、さまざまなサービスと統合して情報をスクレイピングする強力なアプリケーションです。スクレイピングしたデータはREST APIを通じて提供されます。

## バージョン
このAPIの現在のバージョンは1.0です。

## エンドポイント

### GET /search/google

このエンドポイントを使用すると、Googleを検索し、結果を取得することができます。

#### リクエスト

リクエストボディは次のプロパティを持つJSONオブジェクトである必要があります：

- `search` (文字列, 必須): 検索する内容。
- `num_results` (整数, 任意, デフォルト: 5): 取得する検索結果の数。
- `lang` (文字列, 任意, デフォルト: "ja"): 検索に使用する言語。
- `sleep_interval` (整数, 任意, デフォルト: 1): 検索リクエスト間の待機時間（秒）。

例：

```json
{
    "search": "OpenAI",
    "num_results": 10,
    "lang": "en",
    "sleep_interval": 2
}
```

#### レスポンス

レスポンスはJSONオブジェクトになります。リクエストが成功した場合、200のステータスコードを受け取ります。バリデーションエラーがある場合、422のステータスコードとエラーの詳細を含む`HTTPValidationError`オブジェクトを受け取ります。

## cURLを使用したリクエストの例

cURLを使用して`/search/google`エンドポイントにリクエストを送信することができます。以下に例を示します：

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

この例では、"umaxiaotian"を検索し、3つの結果を取得した場合です。検索には日本語を使用し、各検索リクエストの間に5秒間待機します。

## Warning
Please exercise caution and ensure that you only use OpenScrape API for research purposes. Be mindful of the terms of service of websites to avoid any violation related to web scraping. Additionally, take into consideration that many websites employ security measures to prevent scraping activities. Adjust the sleep_interval setting accordingly to avoid sending an excessive number of requests or being blocked.

If you have any further questions or concerns, please let me know.