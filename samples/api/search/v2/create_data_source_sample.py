# Code generated by Lark OpenAPI.

import lark_oapi as lark
from lark_oapi.api.search.v2 import *


def main():
    # 创建client
    client = lark.Client.builder() \
        .app_id(lark.APP_ID) \
        .app_secret(lark.APP_SECRET) \
        .log_level(lark.LogLevel.DEBUG) \
        .build()

    # 构造请求对象
    request: CreateDataSourceRequest = CreateDataSourceRequest.builder() \
        .request_body(DataSource.builder()
                      .name("客服工单")
                      .state(0)
                      .description("搜索客服工单")
                      .icon_url(
        "https://s3-imfile.feishucdn.com/static-resource/v1/585fd740-f52e-4098-b864-57a32082ba1g")
                      .template("search_common_card")
                      .searchable_fields([])
                      .i18n_name(I18nMeta.builder().build())
                      .i18n_description(I18nMeta.builder().build())
                      .schema_id("7159054681489010384")
                      .app_id("cli_a1306bed4738d01b")
                      .connect_type(0)
                      .connector_param(ConnectorParam.builder().build())
                      .enable_answer(False)
                      .build()) \
        .build()

    # 发起请求
    response: CreateDataSourceResponse = client.search.v2.data_source.create(request)

    # 处理失败返回
    if not response.success():
        lark.logger.error(
            f"client.search.v2.data_source.create failed, code: {response.code}, msg: {response.msg}, log_id: {response.get_log_id()}")
        return

    # 处理业务结果
    lark.logger.info(lark.JSON.marshal(response.data, indent=4))


# 异步方式
async def amain():
    # 创建client
    client = lark.Client.builder() \
        .app_id(lark.APP_ID) \
        .app_secret(lark.APP_SECRET) \
        .log_level(lark.LogLevel.DEBUG) \
        .build()

    # 构造请求对象
    request: CreateDataSourceRequest = CreateDataSourceRequest.builder() \
        .request_body(DataSource.builder()
                      .name("客服工单")
                      .state(0)
                      .description("搜索客服工单")
                      .icon_url(
        "https://s3-imfile.feishucdn.com/static-resource/v1/585fd740-f52e-4098-b864-57a32082ba1g")
                      .template("search_common_card")
                      .searchable_fields([])
                      .i18n_name(I18nMeta.builder().build())
                      .i18n_description(I18nMeta.builder().build())
                      .schema_id("7159054681489010384")
                      .app_id("cli_a1306bed4738d01b")
                      .connect_type(0)
                      .connector_param(ConnectorParam.builder().build())
                      .enable_answer(False)
                      .build()) \
        .build()

    # 发起请求
    response: CreateDataSourceResponse = await client.search.v2.data_source.acreate(request)

    # 处理失败返回
    if not response.success():
        lark.logger.error(
            f"client.search.v2.data_source.acreate failed, code: {response.code}, msg: {response.msg}, log_id: {response.get_log_id()}")
        return

    # 处理业务结果
    lark.logger.info(lark.JSON.marshal(response.data, indent=4))


if __name__ == "__main__":
    # asyncio.run(amain()) 异步方式
    main()
