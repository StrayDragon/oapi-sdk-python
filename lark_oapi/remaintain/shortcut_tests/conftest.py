import pytest
from pydantic import BaseSettings

from lark_oapi.remaintain.shortcut.compact import FeishuOpenAPICompactSettings
from lark_oapi.remaintain.shortcut.sheets import FeishuSheetsShortcut


class TestingAuth(BaseSettings):
    app_id: str
    app_secret: str

    class Config:
        env_prefix = 'lark_oapi_testing_'


@pytest.fixture()
def testing_auth() -> TestingAuth:
    return TestingAuth()


@pytest.fixture()
def testing_s(testing_auth) -> FeishuOpenAPICompactSettings:
    return FeishuOpenAPICompactSettings(app_id=testing_auth.app_id, app_secret=testing_auth.app_secret,
                                        name="FeishuAPI testing", )


@pytest.fixture()
def fss(testing_s) -> FeishuSheetsShortcut:
    return FeishuSheetsShortcut(s=testing_s)


class TestingSpreadsheetInfo(BaseSettings):
    ss_token: str
    sheet_id: str

    class Config:
        env_prefix = "lark_oapi_testing_testing_spreadsheet_info_"


@pytest.fixture()
def fss_ss() -> TestingSpreadsheetInfo:
    return TestingSpreadsheetInfo()
