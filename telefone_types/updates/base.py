import typing
from pydantic import BaseModel

from telefone_types.states import StatePeer

if typing.TYPE_CHECKING:
    from telefone.api import ABCAPI, API


class BaseBotUpdate(BaseModel):
    state_peer: typing.Optional[StatePeer] = None
    unprepared_ctx_api: typing.Optional[typing.Any] = None

    @property
    def ctx_api(self) -> typing.Optional[typing.Union["ABCAPI", "API"]]:
        return getattr(self, "unprepared_ctx_api")
