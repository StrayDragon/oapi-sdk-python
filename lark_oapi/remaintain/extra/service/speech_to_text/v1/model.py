# Code generated by lark suite oapi sdk gen

from typing import List, Dict, Any
from ....utils.dt import to_json_decorator
import attr


@to_json_decorator
@attr.s
class FileConfig:
    file_id = attr.ib(type=str, default=None, metadata={"json": "file_id"})
    format = attr.ib(type=str, default=None, metadata={"json": "format"})
    engine_type = attr.ib(type=str, default=None, metadata={"json": "engine_type"})


@to_json_decorator
@attr.s
class Speech:
    speech = attr.ib(type=str, default=None, metadata={"json": "speech"})
    speech_key = attr.ib(type=str, default=None, metadata={"json": "speech_key"})


@to_json_decorator
@attr.s
class StreamConfig:
    stream_id = attr.ib(type=str, default=None, metadata={"json": "stream_id"})
    sequence_id = attr.ib(type=int, default=None, metadata={"json": "sequence_id"})
    action = attr.ib(type=int, default=None, metadata={"json": "action"})
    format = attr.ib(type=str, default=None, metadata={"json": "format"})
    engine_type = attr.ib(type=str, default=None, metadata={"json": "engine_type"})


@to_json_decorator
@attr.s
class SpeechFileRecognizeReqBody:
    speech = attr.ib(type=Speech, default=None, metadata={"json": "speech"})
    config = attr.ib(type=FileConfig, default=None, metadata={"json": "config"})


@attr.s
class SpeechFileRecognizeResult:
    recognition_text = attr.ib(
        type=str, default=None, metadata={"json": "recognition_text"}
    )


@to_json_decorator
@attr.s
class SpeechStreamRecognizeReqBody:
    speech = attr.ib(type=Speech, default=None, metadata={"json": "speech"})
    config = attr.ib(type=StreamConfig, default=None, metadata={"json": "config"})


@attr.s
class SpeechStreamRecognizeResult:
    stream_id = attr.ib(type=str, default=None, metadata={"json": "stream_id"})
    sequence_id = attr.ib(type=int, default=None, metadata={"json": "sequence_id"})
    recognition_text = attr.ib(
        type=str, default=None, metadata={"json": "recognition_text"}
    )
