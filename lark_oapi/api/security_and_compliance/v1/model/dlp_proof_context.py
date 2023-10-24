# Code generated by Lark OpenAPI.

from typing import Optional

from lark_oapi.core.construct import init


class DlpProofContext(object):
    _types = {
        "hit_content": str,
        "context_snippet": str,
    }

    def __init__(self, d=None):
        self.hit_content: Optional[str] = None
        self.context_snippet: Optional[str] = None
        init(self, d, self._types)

    @staticmethod
    def builder() -> "DlpProofContextBuilder":
        return DlpProofContextBuilder()


class DlpProofContextBuilder(object):
    def __init__(self) -> None:
        self._dlp_proof_context = DlpProofContext()

    def hit_content(self, hit_content: str) -> "DlpProofContextBuilder":
        self._dlp_proof_context.hit_content = hit_content
        return self

    def context_snippet(self, context_snippet: str) -> "DlpProofContextBuilder":
        self._dlp_proof_context.context_snippet = context_snippet
        return self

    def build(self) -> "DlpProofContext":
        return self._dlp_proof_context