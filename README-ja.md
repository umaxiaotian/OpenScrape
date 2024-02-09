# OpenScrape

OpenScrapeは、様々なサービスからデータをスクレイピングするためのPythonライブラリです。現在はGoogle検索、日経株価、日本国内のリアルタイムアニメランキング（dアニメランキング）に対応しておりますが、今後は他の様々なサービスからのスクレイピングに対応する予定です。

## 特徴

- 非同期スクレイピング: OpenScrapeはPythonのasyncioを使用してノンブロッキングI/O操作を行うため、大規模なスクレイピングタスクに効率的です。
- 複数のサービス対応: 現在、OpenScrapeはGoogleの検索結果、日経株価、日本国内のリアルタイムアニメランキング（dアニメランキング）のスクレイピングをサポートしています。
- 同期スクレイピング: OpenScrapeは同期操作もサポートしており、ライブラリの使用方法により柔軟性を持たせています。

## 今後の計画

- より多くのサービス: OpenScrapeを他の様々なサービスからスクレイピングできるように拡張する予定です。

## インストール

pipを使用してOpenScrapeをインストールできます：

```bash
pip install git+https://github.com/umaxiaotian/OpenScrape.git@main
```

## 使用方法

以下に、OpenScrapeを使用してGoogle検索を行う例を示します：

### 非同期

```python
import asyncio
from OpenScrape import google

async def main():
    result = await google.async_search(search="test", num_results=2, lang="ja")
    print(result)

if __name__ == "__main__":
    asyncio.run(main())
```

このスクリプトは、"test"の検索を非同期でGoogle検索し、日本語で最初の2つの結果を表示します。

### 同期

```python
from OpenScrape import google

def main():
    result = google.search(search="test",num_results=1,lang="ja")
    print(result)

if __name__ == "__main__":
    main()
```

このスクリプトは、"test"の検索を同期的にGoogle検索し、日本語で最初の結果を表示します。

Jupyterのサンプルコードは[こちらのリンク](https://github.com/umaxiaotian/OpenScrape/tree/main/example)からご覧いただけます。

## 注意
このライブラリからクローリングする際は、各ウェブサイトのrobots.txtを参照してください。
| ウェブサイト | Robots.txt URL |
| --- | --- |
| 日本経済新聞社 | [https://www.nikkei.com/robots.txt](https://www.nikkei.com/robots.txt) |
| Google LLC | [https://www.google.com/robots.txt](https://www.google.com/robots.txt) |
| dアニメストア | [https://animestore.docomo.ne.jp/robots.txt](https://animestore.docomo.ne.jp/robots.txt) |


## 貢献

OpenScrapeへの貢献を歓迎します！詳細は[貢献ガイド](CONTRIBUTING.md)をご覧ください。

## ライセンス

OpenScrapeは[MIT License](LICENSE)の下でライセンスされています。
