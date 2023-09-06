import datetime
import json
from typing import *

from .const import UTF_8
from .type import T


class JSON(object):
    @staticmethod
    def marshal(obj: Any, indent=None) -> Optional[str]:
        if obj is None:
            return None
        return json.dumps(
            obj,
            indent=indent,
            ensure_ascii=False,
            default=custom_json_encode_default,
        )

    @staticmethod
    def unmarshal(json_str: str, clazz: Type[T]) -> T:
        dict_obj = json.loads(json_str)
        return clazz(dict_obj)


def custom_json_encode_default(o):
    if hasattr(o, "__dict__"):
        return vars(o)
    if isinstance(o, datetime.datetime):
        return o.strftime("%Y-%m-%d %H:%M:%S")
    if isinstance(o, bytes):
        return str(o, encoding=UTF_8)
    if isinstance(o, int):
        return int(o)
    if isinstance(o, float):
        return float(o)
    if isinstance(o, set):
        return list(o)
    raise TypeError(
        f"Object of type {o.__class__.__name__} " "is not JSON serializable"
    )
