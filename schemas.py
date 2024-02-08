from pydantic import BaseModel, Field
from typing import Optional

class SearchRequest(BaseModel):
    search: str = Field(..., description="検索する内容")
    num_results: int = Field(5, description="検索結果の数 (デフォルト: 5)")
    lang: Optional[str] = Field('ja', description="検索の対象言語 (デフォルト: 日本語, 省略可能)")
    sleep_interval: Optional[int] = Field(1, description="検索リクエスト間の待機時間（秒）(デフォルト: 1, 省略可能)")
