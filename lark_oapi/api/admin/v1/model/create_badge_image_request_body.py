# Code generated by Lark OpenAPI.

from typing import Any, Optional, IO

from lark_oapi.core.construct import init


class CreateBadgeImageRequestBody(object):
    _types = {
        "image_file": IO[Any],
        "image_type": int,
    }

    def __init__(self, d=None):
        self.image_file: Optional[IO[Any]] = None
        self.image_type: Optional[int] = None
        init(self, d, self._types)

    @staticmethod
    def builder() -> "CreateBadgeImageRequestBodyBuilder":
        return CreateBadgeImageRequestBodyBuilder()


class CreateBadgeImageRequestBodyBuilder(object):
    def __init__(self) -> None:
        self._create_badge_image_request_body = CreateBadgeImageRequestBody()

    def image_file(self, image_file: IO[Any]) -> "CreateBadgeImageRequestBodyBuilder":
        self._create_badge_image_request_body.image_file = image_file
        return self

    def image_type(self, image_type: int) -> "CreateBadgeImageRequestBodyBuilder":
        self._create_badge_image_request_body.image_type = image_type
        return self

    def build(self) -> "CreateBadgeImageRequestBody":
        return self._create_badge_image_request_body
