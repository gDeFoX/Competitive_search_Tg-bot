from dataclasses import dataclass, field


@dataclass(frozen=True)
class SearchResult:
    title: str
    description: str
    url: str
    source: str
    extra: dict = field(default_factory=dict)