from lark_oapi.remaintain.shortcut.compact import FeishuOpenAPICompactSettings


def test_init_feishu_openapi_compact_settings(testing_auth):
    assert FeishuOpenAPICompactSettings(app_id=testing_auth.app_id, app_secret=testing_auth.app_secret, )
