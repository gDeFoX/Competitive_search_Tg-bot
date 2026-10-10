import re
from html import unescape
from urllib.parse import quote

import httpx

from models import SearchResult
from providers.base import SearchProvider

API_URL = "https://en.wikipedia.org/w/api.php"
TAG_RE = re.compile(r"<[^>]+>")


class WikipediaProvider(SearchProvider):
    name = "Wikipedia"

    def __init__(self, client: httpx.AsyncClient, limit: int = 5) -> None:
        self._client = client
        self._limit = limit

    async def search(self, query: str) -> list[SearchResult]:
        params = {
            "action": "query",
            "list": "search",
            "srsearch": query,
            "srlimit": self._limit,
            "format": "json",
            "formatversion": 2,
        }
        response = await self._client.get(API_URL, params=params)
        response.raise_for_status()
        data = response.json()

        results = []
        for item in data["query"]["search"]:
            title = item["title"]
            # в сниппете приходит HTML (<span class="searchmatch">), чистим его
            description = unescape(TAG_RE.sub("", item["snippet"]))
            url = "https://en.wikipedia.org/wiki/" + quote(title.replace(" ", "_"))
            results.append(
                SearchResult(
                    title=title,
                    description=description,
                    url=url,
                    source=self.name,
                )
            )
        return results