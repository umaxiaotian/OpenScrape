# OpenScrape

OpenScrapeは、様々なサービスからデータをスクレイピングするためのPythonライブラリです。現在はGoogle検索、日経株価、日本国内のリアルタイムアニメランキング（dアニメランキング）に対応しており、さらにほとんどのウェブサイトからのスクレイピングもサポートしています。今後はユーザーからのフィードバックに基づき、必要な機能を追加していく予定です。具体的な要望や問題は、GitHubのISSUEにてお知らせください。

## 特徴

- 非同期スクレイピング: OpenScrapeはPythonのasyncioを使用してノンブロッキングI/O操作を行うため、大規模なスクレイピングタスクに効率的です。
- 複数のサービス対応: 現在、OpenScrapeはGoogleの検索結果、日経株価、日本国内のリアルタイムアニメランキング（dアニメランキング）のスクレイピングをサポートしています。
- 同期スクレイピング: OpenScrapeは同期操作もサポートしており、ライブラリの使用方法により柔軟性を持たせています。

## 今後の計画

- より多くのサービス: OpenScrapeを他の様々なサービスからスクレイピングできるように拡張する予定です。具体的な要望や問題は、GitHubのISSUEにてお知らせください。

## インストール

pipを使用してOpenScrapeをインストールできます：

```bash
pip install git+https://github.com/umaxiaotian/OpenScrape.git@main
```

## 使用方法

以下に、OpenScrapeを使用して任意のウェブサイトをスクレイピングする例を示します：

### 非同期

```python
import asyncio
from OpenScrape import any_websites

async def main():
    result = await any_websites.async_crawl("https://www.bloomberg.co.jp/news/articles/2024-01-05/S6PKIWT0AFB400")
    print(result)

if __name__ == "__main__":
    asyncio.run(main())
```

このスクリプトは、指定したURLのウェブページを非同期にスクレイピングし、そのページのタイトルと本文を表示します。

### 同期

```python
from OpenScrape import any_websites

def main():
    result = any_websites.crawl("https://www.bloomberg.co.jp/news/articles/2024-01-05/S6PKIWT0AFB400")
    print(result)

if __name__ == "__main__":
    main()
```

このスクリプトは、指定したURLのウェブページを同期的にスクレイピングし、そのページのタイトルと本文を表示します。

Jupyterのサンプルコードは[こちらのリンク](https://github.com/umaxiaotian/OpenScrape/tree/main/example)からご覧いただけます。

## 注意
このライブラリからクローリングする際は、各ウェブサイトのrobots.txtを参照してください。
| ウェブサイト | Robots.txt URL |
| --- | --- |
| 日本経済新聞社 | [https://www.nikkei.com/robots.txt](https://www.nikkei.com/robots.txt) |
| Google LLC | [https://www.google.com/robots.txt](https://www.google.com/robots.txt) |
| dアニメストア | [https://animestore.docomo.ne.jp/robots.txt](https://animestore.docomo.ne.jp/robots.txt) |
| bing | [https://bing.com/robots.txt](https://bing.com/robots.txt) |

## 貢献

OpenScrapeへの貢献を歓迎します！詳細は[貢献ガイド](CONTRIBUTING.md)をご覧ください。

## ライセンス

OpenScrapeは[MIT License](LICENSE)の下でライセンスされています。