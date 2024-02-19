# Code generated by Lark OpenAPI.

from typing import Optional

from lark_oapi.core.construct import init
from .text_element_style import TextElementStyle


class InlineBlock(object):
    _types = {
        "block_id": str,
        "text_element_style": TextElementStyle,
    }

    def __init__(self, d=None):
        self.block_id: Optional[str] = None
        self.text_element_style: Optional[TextElementStyle] = None
        init(self, d, self._types)

    @staticmethod
    def builder() -> "InlineBlockBuilder":
        return InlineBlockBuilder()


class InlineBlockBuilder(object):
    def __init__(self) -> None:
        self._inline_block = InlineBlock()

    def block_id(self, block_id: str) -> "InlineBlockBuilder":
        self._inline_block.block_id = block_id
        return self

    def text_element_style(self, text_element_style: TextElementStyle) -> "InlineBlockBuilder":
        self._inline_block.text_element_style = text_element_style
        return self

    def build(self) -> "InlineBlock":
        return self._inline_block
