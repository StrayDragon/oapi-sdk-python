# Code generated by Lark OpenAPI.

from typing import Optional

from lark_oapi.core.construct import init


class ProductI18nName(object):
    _types = {
        "zh_cn": str,
        "ja_jp": str,
        "en_us": str,
    }

    def __init__(self, d=None):
        self.zh_cn: Optional[str] = None
        self.ja_jp: Optional[str] = None
        self.en_us: Optional[str] = None
        init(self, d, self._types)

    @staticmethod
    def builder() -> "ProductI18nNameBuilder":
        return ProductI18nNameBuilder()


class ProductI18nNameBuilder(object):
    def __init__(self) -> None:
        self._product_i18n_name = ProductI18nName()

    def zh_cn(self, zh_cn: str) -> "ProductI18nNameBuilder":
        self._product_i18n_name.zh_cn = zh_cn
        return self

    def ja_jp(self, ja_jp: str) -> "ProductI18nNameBuilder":
        self._product_i18n_name.ja_jp = ja_jp
        return self

    def en_us(self, en_us: str) -> "ProductI18nNameBuilder":
        self._product_i18n_name.en_us = en_us
        return self

    def build(self) -> "ProductI18nName":
        return self._product_i18n_name
