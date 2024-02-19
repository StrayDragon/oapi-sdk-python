# Code generated by Lark OpenAPI.

from typing import Optional

from lark_oapi.core.construct import init
from .food_manage_license import FoodManageLicense


class RecognizeFoodManageLicenseResponseBody(object):
    _types = {
        "food_manage_license": FoodManageLicense,
    }

    def __init__(self, d=None):
        self.food_manage_license: Optional[FoodManageLicense] = None
        init(self, d, self._types)

    @staticmethod
    def builder() -> "RecognizeFoodManageLicenseResponseBodyBuilder":
        return RecognizeFoodManageLicenseResponseBodyBuilder()


class RecognizeFoodManageLicenseResponseBodyBuilder(object):
    def __init__(self) -> None:
        self._recognize_food_manage_license_response_body = RecognizeFoodManageLicenseResponseBody()

    def food_manage_license(self,
                            food_manage_license: FoodManageLicense) -> "RecognizeFoodManageLicenseResponseBodyBuilder":
        self._recognize_food_manage_license_response_body.food_manage_license = food_manage_license
        return self

    def build(self) -> "RecognizeFoodManageLicenseResponseBody":
        return self._recognize_food_manage_license_response_body
