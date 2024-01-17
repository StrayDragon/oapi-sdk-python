# Code generated by Lark OpenAPI.

import lark_oapi as lark
from lark_oapi.api.calendar.v4 import *


def main():
    # 创建client
    client = lark.Client.builder() \
        .app_id(lark.APP_ID) \
        .app_secret(lark.APP_SECRET) \
        .log_level(lark.LogLevel.DEBUG) \
        .build()

    # 构造请求对象
    request: ReplyCalendarEventRequest = ReplyCalendarEventRequest.builder() \
        .calendar_id("feishu.cn_HF9U2MbibE8PPpjro6xjqa@group.calendar.feishu.cn") \
        .event_id("75d28f9b-e35c-4230-8a83-4a661497db54_0") \
        .request_body(ReplyCalendarEventRequestBody.builder()
                      .rsvp_status("accept")
                      .build()) \
        .build()

    # 发起请求
    response: ReplyCalendarEventResponse = client.calendar.v4.calendar_event.reply(request)

    # 处理失败返回
    if not response.success():
        lark.logger.error(
            f"client.calendar.v4.calendar_event.reply failed, code: {response.code}, msg: {response.msg}, log_id: {response.get_log_id()}")
        return

    # 处理业务结果
    lark.logger.info(lark.JSON.marshal(response.data, indent=4))


if __name__ == "__main__":
    main()