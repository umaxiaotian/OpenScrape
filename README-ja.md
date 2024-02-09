# OpenScrape

OpenScrapeは、様々なサービスからデータをスクレイピングするためのPythonライブラリです。現在はGoogle検索に特化していますが、今後は他の様々なサービスからスクレイピングできるように機能を拡張する予定です。

## 特徴

- 非同期スクレイピング: OpenScrapeはPythonのasyncioを使用してノンブロッキングI/O操作を行うため、大規模なスクレイピングタスクにも効率的です。
- Google検索: 現在、OpenScrapeはGoogleの検索結果をスクレイピングする機能をサポートしています。検索語、結果の数、言語を指定することができます。

## 将来の計画

- サービスの追加: 今後、OpenScrapeは他の様々なサービスからのスクレイピングをサポートするように拡張する予定です。
- 同期スクレイピング: OpenScrapeは現在、非同期操作のみをサポートしていますが、将来的には同期操作もサポートする予定です。

## インストール

pipを使用してOpenScrapeをインストールできます：

```bash
pip install OpenScrape
```

## 使い方

以下は、OpenScrapeを使用してGoogle検索を行う例です：

```python
import asyncio
from OpenScrape import google

async def main():
    result = await google.asyncsearch(term="test", num_results=2, lang="ja")
    print(result)

if __name__ == "__main__":
    asyncio.run(main())
```

このスクリプトは、"test"という検索語で非同期のGoogle検索を行い、日本語の結果を最初の2つを表示します。

## 貢献

OpenScrapeへの貢献を歓迎します！詳細は[貢献ガイド](CONTRIBUTING.md)をご覧ください。

## ライセンス

OpenScrapeは[MITライセンス](LICENSE)のもとでライセンスされています。