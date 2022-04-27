from enum import Enum

from telefone_types.objects import (
    CallbackQuery,
    ChatJoinRequest,
    ChatMemberUpdated,
    ChosenInlineResult,
    InlineQuery,
    Message,
    Poll,
    PollAnswer,
    PreCheckoutQuery,
    ShippingQuery,
)
from telefone_types.updates.base import BaseBotUpdate


class BotUpdateType(Enum):
    MESSAGE = "message"
    EDITED_MESSAGE = "edited_message"
    CHANNEL_POST = "channel_post"
    EDITED_CHANNEL_POST = "edited_channel_post"
    INLINE_QUERY = "inline_query"
    CHOSEN_INLINE_RESULT = "chosen_inline_result"
    CALLBACK_QUERY = "callback_query"
    SHIPPING_QUERY = "shipping_query"
    PRE_CHECKOUT_QUERY = "pre_checkout_query"
    POLL = "poll"
    POLL_ANSWER = "poll_answer"
    MY_CHAT_MEMBER = "my_chat_member"
    CHAT_MEMBER = "chat_member"
    CHAT_JOIN_REQUEST = "chat_join_request"


class UpdateTypes:
    class CallbackQueryUpdate(BaseBotUpdate, CallbackQuery):
        pass

    class ChatJoinRequestUpdate(BaseBotUpdate, ChatJoinRequest):
        pass

    class ChatMemberUpdate(BaseBotUpdate, ChatMemberUpdated):
        pass

    class ChosenInlineResultUpdate(BaseBotUpdate, ChosenInlineResult):
        pass

    class InlineQueryUpdate(BaseBotUpdate, InlineQuery):
        pass

    class MessageUpdate(BaseBotUpdate, Message):
        pass

    class EditedMessageUpdate(BaseBotUpdate, Message):
        pass

    class ChannelPostUpdate(BaseBotUpdate, Message):
        pass

    class EditedChannelPostUpdate(BaseBotUpdate, Message):
        pass

    class MyChatMemberUpdate(BaseBotUpdate, ChatMemberUpdated):
        pass

    class PollAnswerUpdate(BaseBotUpdate, PollAnswer):
        pass

    class PollUpdate(BaseBotUpdate, Poll):
        pass

    class PreCheckoutQuery(BaseBotUpdate, PreCheckoutQuery):
        pass

    class ShippingQueryUpdate(BaseBotUpdate, ShippingQuery):
        pass
