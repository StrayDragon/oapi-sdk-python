import dataclasses

from lark_oapi import Client
from lark_oapi.remaintain import extra
from lark_oapi.remaintain.extra import DOMAIN_FEISHU, LEVEL_ERROR


@dataclasses.dataclass
class FeishuOpenAPICompactSettings:
    app_id: str
    app_secret: str
    name: str = "Feishu OAPI"
    log_level: int = LEVEL_ERROR

    # post init
    remaintain_extra_app_settings: extra.AppSettings = dataclasses.field(init=False)
    remaintain_extra_config: extra.Config = dataclasses.field(init=False)
    upstream_client: Client = dataclasses.field(init=False)

    def __post_init__(self):
        app_settings = extra.Config.new_internal_app_settings(
            app_id=self.app_id,
            app_secret=self.app_secret,
        )
        self.remaintain_extra_app_settings = app_settings
        self.remaintain_extra_config = extra.Config(
            DOMAIN_FEISHU,
            app_settings,
            log_level=self.log_level,
        )
        self.upstream_client = (
            Client.builder()
            .app_id(
                self.app_id,
            )
            .app_secret(
                self.app_secret,
            )
            .build()
        )
