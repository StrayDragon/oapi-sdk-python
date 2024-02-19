# Code generated by Lark OpenAPI.

import lark_oapi as lark
from lark_oapi.api.corehr.v1 import *


def main():
    # 创建client
    client = lark.Client.builder() \
        .app_id(lark.APP_ID) \
        .app_secret(lark.APP_SECRET) \
        .log_level(lark.LogLevel.DEBUG) \
        .build()

    # 构造请求对象
    request: LeaveRequestHistoryLeaveRequest = LeaveRequestHistoryLeaveRequest.builder() \
        .page_token("eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9") \
        .page_size("100") \
        .employment_id_list([]) \
        .initiator_id_list([]) \
        .leave_request_status([]) \
        .leave_type_id_list([]) \
        .leave_start_date_min("2022-07-20 morning") \
        .leave_start_date_max("2022-07-20 morning") \
        .leave_end_date_min("2022-07-20 morning") \
        .leave_end_date_max("2022-07-20 morning") \
        .leave_submit_date_min("2022-07-20 morning") \
        .leave_submit_date_max("2022-07-20 morning") \
        .user_id_type("people_corehr_id") \
        .leave_update_time_min("2022-10-24 10:00:00") \
        .leave_update_time_max("2022-10-24 10:00:00") \
        .return_detail(False) \
        .leave_term_type(0) \
        .time_zone("Asia/Shanghai") \
        .data_source(1) \
        .build()

    # 发起请求
    response: LeaveRequestHistoryLeaveResponse = client.corehr.v1.leave.leave_request_history(request)

    # 处理失败返回
    if not response.success():
        lark.logger.error(
            f"client.corehr.v1.leave.leave_request_history failed, code: {response.code}, msg: {response.msg}, log_id: {response.get_log_id()}")
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
    request: LeaveRequestHistoryLeaveRequest = LeaveRequestHistoryLeaveRequest.builder() \
        .page_token("eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9") \
        .page_size("100") \
        .employment_id_list([]) \
        .initiator_id_list([]) \
        .leave_request_status([]) \
        .leave_type_id_list([]) \
        .leave_start_date_min("2022-07-20 morning") \
        .leave_start_date_max("2022-07-20 morning") \
        .leave_end_date_min("2022-07-20 morning") \
        .leave_end_date_max("2022-07-20 morning") \
        .leave_submit_date_min("2022-07-20 morning") \
        .leave_submit_date_max("2022-07-20 morning") \
        .user_id_type("people_corehr_id") \
        .leave_update_time_min("2022-10-24 10:00:00") \
        .leave_update_time_max("2022-10-24 10:00:00") \
        .return_detail(False) \
        .leave_term_type(0) \
        .time_zone("Asia/Shanghai") \
        .data_source(1) \
        .build()

    # 发起请求
    response: LeaveRequestHistoryLeaveResponse = await client.corehr.v1.leave.aleave_request_history(request)

    # 处理失败返回
    if not response.success():
        lark.logger.error(
            f"client.corehr.v1.leave.aleave_request_history failed, code: {response.code}, msg: {response.msg}, log_id: {response.get_log_id()}")
        return

    # 处理业务结果
    lark.logger.info(lark.JSON.marshal(response.data, indent=4))


if __name__ == "__main__":
    # asyncio.run(amain()) 异步方式
    main()
