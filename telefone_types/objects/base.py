from typing import Any

from pydantic import BaseModel, Field


def convert(d: BaseModel) -> Any:
    if isinstance(d, BaseModel):
        return d.convert_to_dict()
    elif isinstance(d, dict):
        return {k: convert(v) for k, v in d.items() if v is not None}
    elif isinstance(d, list):
        l = [convert(o) for o in d]
        return l
    return d


class BaseObject(BaseModel):
    def convert_to_dict(self) -> dict:
        return {k: convert(v) for k, v in self.dict().items() if v is not None}
