# Code generated by Lark OpenAPI.

from lark_oapi.core.construct import init


class DocContainer(object):
    _types = {
    }

    def __init__(self, d=None):
        init(self, d, self._types)

    @staticmethod
    def builder() -> "DocContainerBuilder":
        return DocContainerBuilder()


class DocContainerBuilder(object):
    def __init__(self) -> None:
        self._doc_container = DocContainer()

    def build(self) -> "DocContainer":
        return self._doc_container
