# Code generated by Lark OpenAPI.

from typing import Optional

from lark_oapi.core.construct import init
from .text_element_style import TextElementStyle


class InlineFile(object):
    _types = {
        "file_token": str,
        "source_block_id": str,
        "text_element_style": TextElementStyle,
    }

    def __init__(self, d=None):
        self.file_token: Optional[str] = None
        self.source_block_id: Optional[str] = None
        self.text_element_style: Optional[TextElementStyle] = None
        init(self, d, self._types)

    @staticmethod
    def builder() -> "InlineFileBuilder":
        return InlineFileBuilder()


class InlineFileBuilder(object):
    def __init__(self) -> None:
        self._inline_file = InlineFile()

    def file_token(self, file_token: str) -> "InlineFileBuilder":
        self._inline_file.file_token = file_token
        return self

    def source_block_id(self, source_block_id: str) -> "InlineFileBuilder":
        self._inline_file.source_block_id = source_block_id
        return self

    def text_element_style(self, text_element_style: TextElementStyle) -> "InlineFileBuilder":
        self._inline_file.text_element_style = text_element_style
        return self

    def build(self) -> "InlineFile":
        return self._inline_file
