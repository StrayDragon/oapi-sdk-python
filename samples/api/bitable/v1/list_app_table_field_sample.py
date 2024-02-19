# Code generated by Lark OpenAPI.

import lark_oapi as lark
from lark_oapi.api.bitable.v1 import *


def main():
    # 创建client
    client = lark.Client.builder() \
        .app_id(lark.APP_ID) \
        .app_secret(lark.APP_SECRET) \
        .log_level(lark.LogLevel.DEBUG) \
        .build()

    # 构造请求对象
    request: ListAppTableFieldRequest = ListAppTableFieldRequest.builder() \
        .app_token("appbcbWCzen6D8dezhoCH2RpMAh") \
        .table_id("tblsRc9GRRXKqhvW") \
        .view_id("vewOVMEXPF") \
        .text_field_as_array(True) \
        .page_token("fldwJ4YrtB") \
        .page_size(20) \
        .build()

    # 发起请求
    response: ListAppTableFieldResponse = client.bitable.v1.app_table_field.list(request)

    # 处理失败返回
    if not response.success():
        lark.logger.error(
            f"client.bitable.v1.app_table_field.list failed, code: {response.code}, msg: {response.msg}, log_id: {response.get_log_id()}")
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
    request: ListAppTableFieldRequest = ListAppTableFieldRequest.builder() \
        .app_token("appbcbWCzen6D8dezhoCH2RpMAh") \
        .table_id("tblsRc9GRRXKqhvW") \
        .view_id("vewOVMEXPF") \
        .text_field_as_array(True) \
        .page_token("fldwJ4YrtB") \
        .page_size(20) \
        .build()

    # 发起请求
    response: ListAppTableFieldResponse = await client.bitable.v1.app_table_field.alist(request)

    # 处理失败返回
    if not response.success():
        lark.logger.error(
            f"client.bitable.v1.app_table_field.alist failed, code: {response.code}, msg: {response.msg}, log_id: {response.get_log_id()}")
        return

    # 处理业务结果
    lark.logger.info(lark.JSON.marshal(response.data, indent=4))


if __name__ == "__main__":
    # asyncio.run(amain()) 异步方式
    main()
