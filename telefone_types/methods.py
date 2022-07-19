from typing import *

from pydantic import parse_obj_as

from telefone_types.objects import *

if TYPE_CHECKING:
    from telefone.api import ABCAPI, API


class APIMethods:
    def __init__(self, api: Union["ABCAPI", "API"]) -> None:
        self.api = api

    @staticmethod
    def get_params(loc: dict) -> dict:
        n = {
            k: v
            for k, v in loc.items()
            if k not in ("self", "kwargs") and v is not None
        }
        n.update(loc["kwargs"])
        return n

    @staticmethod
    def get_response(r: dict) -> dict:
        if "json" in r:
            r["json_"] = r["json"]
        return r

    async def get_updates(
        self,
        offset: Optional[int] = None,
        limit: Optional[int] = None,
        timeout: Optional[int] = None,
        allowed_updates: Optional[List[str]] = None,
        **kwargs
    ) -> List[Update]:
        response = await self.api.request("getUpdates", self.get_params(locals()))
        return parse_obj_as(List[Update], response)

    async def set_webhook(
        self,
        url: Optional[str] = None,
        certificate: Optional[InputFile] = None,
        ip_address: Optional[str] = None,
        max_connections: Optional[int] = None,
        allowed_updates: Optional[List[str]] = None,
        drop_pending_updates: Optional[bool] = None,
        secret_token: Optional[str] = None,
        **kwargs
    ) -> bool:
        response = await self.api.request("setWebhook", self.get_params(locals()))
        return response

    async def delete_webhook(
        self, drop_pending_updates: Optional[bool] = None, **kwargs
    ) -> bool:
        response = await self.api.request("deleteWebhook", self.get_params(locals()))
        return response

    async def get_webhook_info(self, **kwargs) -> WebhookInfo:
        response = await self.api.request("getWebhookInfo", self.get_params(locals()))
        return WebhookInfo(**response)

    async def get_me(self, **kwargs) -> User:
        response = await self.api.request("getMe", self.get_params(locals()))
        return User(**response)

    async def log_out(self, **kwargs) -> bool:
        response = await self.api.request("logOut", self.get_params(locals()))
        return response

    async def close(self, **kwargs) -> bool:
        response = await self.api.request("close", self.get_params(locals()))
        return response

    async def send_message(
        self,
        chat_id: Optional[Union[int, str]] = None,
        text: Optional[str] = None,
        parse_mode: Optional[str] = None,
        entities: Optional[List[MessageEntity]] = None,
        disable_web_page_preview: Optional[bool] = None,
        disable_notification: Optional[bool] = None,
        protect_content: Optional[bool] = None,
        reply_to_message_id: Optional[int] = None,
        allow_sending_without_reply: Optional[bool] = None,
        reply_markup: Optional[
            Union[
                InlineKeyboardMarkup,
                ReplyKeyboardMarkup,
                ReplyKeyboardRemove,
                ForceReply,
            ]
        ] = None,
        **kwargs
    ) -> Message:
        response = await self.api.request("sendMessage", self.get_params(locals()))
        return Message(**response)

    async def forward_message(
        self,
        chat_id: Optional[Union[int, str]] = None,
        from_chat_id: Optional[Union[int, str]] = None,
        disable_notification: Optional[bool] = None,
        protect_content: Optional[bool] = None,
        message_id: Optional[int] = None,
        **kwargs
    ) -> Message:
        response = await self.api.request("forwardMessage", self.get_params(locals()))
        return Message(**response)

    async def copy_message(
        self,
        chat_id: Optional[Union[int, str]] = None,
        from_chat_id: Optional[Union[int, str]] = None,
        message_id: Optional[int] = None,
        caption: Optional[str] = None,
        parse_mode: Optional[str] = None,
        caption_entities: Optional[List[MessageEntity]] = None,
        disable_notification: Optional[bool] = None,
        protect_content: Optional[bool] = None,
        reply_to_message_id: Optional[int] = None,
        allow_sending_without_reply: Optional[bool] = None,
        reply_markup: Optional[
            Union[
                InlineKeyboardMarkup,
                ReplyKeyboardMarkup,
                ReplyKeyboardRemove,
                ForceReply,
            ]
        ] = None,
        **kwargs
    ) -> MessageId:
        response = await self.api.request("copyMessage", self.get_params(locals()))
        return MessageId(**response)

    async def send_photo(
        self,
        chat_id: Optional[Union[int, str]] = None,
        photo: Optional[Union[InputFile, str]] = None,
        caption: Optional[str] = None,
        parse_mode: Optional[str] = None,
        caption_entities: Optional[List[MessageEntity]] = None,
        disable_notification: Optional[bool] = None,
        protect_content: Optional[bool] = None,
        reply_to_message_id: Optional[int] = None,
        allow_sending_without_reply: Optional[bool] = None,
        reply_markup: Optional[
            Union[
                InlineKeyboardMarkup,
                ReplyKeyboardMarkup,
                ReplyKeyboardRemove,
                ForceReply,
            ]
        ] = None,
        **kwargs
    ) -> Message:
        response = await self.api.request("sendPhoto", self.get_params(locals()))
        return Message(**response)

    async def send_audio(
        self,
        chat_id: Optional[Union[int, str]] = None,
        audio: Optional[Union[InputFile, str]] = None,
        caption: Optional[str] = None,
        parse_mode: Optional[str] = None,
        caption_entities: Optional[List[MessageEntity]] = None,
        duration: Optional[int] = None,
        performer: Optional[str] = None,
        title: Optional[str] = None,
        thumb: Optional[Union[InputFile, str]] = None,
        disable_notification: Optional[bool] = None,
        protect_content: Optional[bool] = None,
        reply_to_message_id: Optional[int] = None,
        allow_sending_without_reply: Optional[bool] = None,
        reply_markup: Optional[
            Union[
                InlineKeyboardMarkup,
                ReplyKeyboardMarkup,
                ReplyKeyboardRemove,
                ForceReply,
            ]
        ] = None,
        **kwargs
    ) -> Message:
        response = await self.api.request("sendAudio", self.get_params(locals()))
        return Message(**response)

    async def send_document(
        self,
        chat_id: Optional[Union[int, str]] = None,
        document: Optional[Union[InputFile, str]] = None,
        thumb: Optional[Union[InputFile, str]] = None,
        caption: Optional[str] = None,
        parse_mode: Optional[str] = None,
        caption_entities: Optional[List[MessageEntity]] = None,
        disable_content_type_detection: Optional[bool] = None,
        disable_notification: Optional[bool] = None,
        protect_content: Optional[bool] = None,
        reply_to_message_id: Optional[int] = None,
        allow_sending_without_reply: Optional[bool] = None,
        reply_markup: Optional[
            Union[
                InlineKeyboardMarkup,
                ReplyKeyboardMarkup,
                ReplyKeyboardRemove,
                ForceReply,
            ]
        ] = None,
        **kwargs
    ) -> Message:
        response = await self.api.request("sendDocument", self.get_params(locals()))
        return Message(**response)

    async def send_video(
        self,
        chat_id: Optional[Union[int, str]] = None,
        video: Optional[Union[InputFile, str]] = None,
        duration: Optional[int] = None,
        width: Optional[int] = None,
        height: Optional[int] = None,
        thumb: Optional[Union[InputFile, str]] = None,
        caption: Optional[str] = None,
        parse_mode: Optional[str] = None,
        caption_entities: Optional[List[MessageEntity]] = None,
        supports_streaming: Optional[bool] = None,
        disable_notification: Optional[bool] = None,
        protect_content: Optional[bool] = None,
        reply_to_message_id: Optional[int] = None,
        allow_sending_without_reply: Optional[bool] = None,
        reply_markup: Optional[
            Union[
                InlineKeyboardMarkup,
                ReplyKeyboardMarkup,
                ReplyKeyboardRemove,
                ForceReply,
            ]
        ] = None,
        **kwargs
    ) -> Message:
        response = await self.api.request("sendVideo", self.get_params(locals()))
        return Message(**response)

    async def send_animation(
        self,
        chat_id: Optional[Union[int, str]] = None,
        animation: Optional[Union[InputFile, str]] = None,
        duration: Optional[int] = None,
        width: Optional[int] = None,
        height: Optional[int] = None,
        thumb: Optional[Union[InputFile, str]] = None,
        caption: Optional[str] = None,
        parse_mode: Optional[str] = None,
        caption_entities: Optional[List[MessageEntity]] = None,
        disable_notification: Optional[bool] = None,
        protect_content: Optional[bool] = None,
        reply_to_message_id: Optional[int] = None,
        allow_sending_without_reply: Optional[bool] = None,
        reply_markup: Optional[
            Union[
                InlineKeyboardMarkup,
                ReplyKeyboardMarkup,
                ReplyKeyboardRemove,
                ForceReply,
            ]
        ] = None,
        **kwargs
    ) -> Message:
        response = await self.api.request("sendAnimation", self.get_params(locals()))
        return Message(**response)

    async def send_voice(
        self,
        chat_id: Optional[Union[int, str]] = None,
        voice: Optional[Union[InputFile, str]] = None,
        caption: Optional[str] = None,
        parse_mode: Optional[str] = None,
        caption_entities: Optional[List[MessageEntity]] = None,
        duration: Optional[int] = None,
        disable_notification: Optional[bool] = None,
        protect_content: Optional[bool] = None,
        reply_to_message_id: Optional[int] = None,
        allow_sending_without_reply: Optional[bool] = None,
        reply_markup: Optional[
            Union[
                InlineKeyboardMarkup,
                ReplyKeyboardMarkup,
                ReplyKeyboardRemove,
                ForceReply,
            ]
        ] = None,
        **kwargs
    ) -> Message:
        response = await self.api.request("sendVoice", self.get_params(locals()))
        return Message(**response)

    async def send_video_note(
        self,
        chat_id: Optional[Union[int, str]] = None,
        video_note: Optional[Union[InputFile, str]] = None,
        duration: Optional[int] = None,
        length: Optional[int] = None,
        thumb: Optional[Union[InputFile, str]] = None,
        disable_notification: Optional[bool] = None,
        protect_content: Optional[bool] = None,
        reply_to_message_id: Optional[int] = None,
        allow_sending_without_reply: Optional[bool] = None,
        reply_markup: Optional[
            Union[
                InlineKeyboardMarkup,
                ReplyKeyboardMarkup,
                ReplyKeyboardRemove,
                ForceReply,
            ]
        ] = None,
        **kwargs
    ) -> Message:
        response = await self.api.request("sendVideoNote", self.get_params(locals()))
        return Message(**response)

    async def send_media_group(
        self,
        chat_id: Optional[Union[int, str]] = None,
        media: Optional[
            List[
                Union[
                    InputMediaAudio,
                    InputMediaDocument,
                    InputMediaPhoto,
                    InputMediaVideo,
                ]
            ]
        ] = None,
        disable_notification: Optional[bool] = None,
        protect_content: Optional[bool] = None,
        reply_to_message_id: Optional[int] = None,
        allow_sending_without_reply: Optional[bool] = None,
        **kwargs
    ) -> List[Message]:
        response = await self.api.request("sendMediaGroup", self.get_params(locals()))
        return parse_obj_as(List[Message], response)

    async def send_location(
        self,
        chat_id: Optional[Union[int, str]] = None,
        latitude: Optional[float] = None,
        longitude: Optional[float] = None,
        horizontal_accuracy: Optional[float] = None,
        live_period: Optional[int] = None,
        heading: Optional[int] = None,
        proximity_alert_radius: Optional[int] = None,
        disable_notification: Optional[bool] = None,
        protect_content: Optional[bool] = None,
        reply_to_message_id: Optional[int] = None,
        allow_sending_without_reply: Optional[bool] = None,
        reply_markup: Optional[
            Union[
                InlineKeyboardMarkup,
                ReplyKeyboardMarkup,
                ReplyKeyboardRemove,
                ForceReply,
            ]
        ] = None,
        **kwargs
    ) -> Message:
        response = await self.api.request("sendLocation", self.get_params(locals()))
        return Message(**response)

    async def edit_message_live_location(
        self,
        chat_id: Optional[Union[int, str]] = None,
        message_id: Optional[int] = None,
        inline_message_id: Optional[str] = None,
        latitude: Optional[float] = None,
        longitude: Optional[float] = None,
        horizontal_accuracy: Optional[float] = None,
        heading: Optional[int] = None,
        proximity_alert_radius: Optional[int] = None,
        reply_markup: Optional[InlineKeyboardMarkup] = None,
        **kwargs
    ) -> Union[Message, bool]:
        response = await self.api.request(
            "editMessageLiveLocation", self.get_params(locals())
        )
        return parse_obj_as(Union[Message, bool], response)

    async def stop_message_live_location(
        self,
        chat_id: Optional[Union[int, str]] = None,
        message_id: Optional[int] = None,
        inline_message_id: Optional[str] = None,
        reply_markup: Optional[InlineKeyboardMarkup] = None,
        **kwargs
    ) -> Union[Message, bool]:
        response = await self.api.request(
            "stopMessageLiveLocation", self.get_params(locals())
        )
        return parse_obj_as(Union[Message, bool], response)

    async def send_venue(
        self,
        chat_id: Optional[Union[int, str]] = None,
        latitude: Optional[float] = None,
        longitude: Optional[float] = None,
        title: Optional[str] = None,
        address: Optional[str] = None,
        foursquare_id: Optional[str] = None,
        foursquare_type: Optional[str] = None,
        google_place_id: Optional[str] = None,
        google_place_type: Optional[str] = None,
        disable_notification: Optional[bool] = None,
        protect_content: Optional[bool] = None,
        reply_to_message_id: Optional[int] = None,
        allow_sending_without_reply: Optional[bool] = None,
        reply_markup: Optional[
            Union[
                InlineKeyboardMarkup,
                ReplyKeyboardMarkup,
                ReplyKeyboardRemove,
                ForceReply,
            ]
        ] = None,
        **kwargs
    ) -> Message:
        response = await self.api.request("sendVenue", self.get_params(locals()))
        return Message(**response)

    async def send_contact(
        self,
        chat_id: Optional[Union[int, str]] = None,
        phone_number: Optional[str] = None,
        first_name: Optional[str] = None,
        last_name: Optional[str] = None,
        vcard: Optional[str] = None,
        disable_notification: Optional[bool] = None,
        protect_content: Optional[bool] = None,
        reply_to_message_id: Optional[int] = None,
        allow_sending_without_reply: Optional[bool] = None,
        reply_markup: Optional[
            Union[
                InlineKeyboardMarkup,
                ReplyKeyboardMarkup,
                ReplyKeyboardRemove,
                ForceReply,
            ]
        ] = None,
        **kwargs
    ) -> Message:
        response = await self.api.request("sendContact", self.get_params(locals()))
        return Message(**response)

    async def send_poll(
        self,
        chat_id: Optional[Union[int, str]] = None,
        question: Optional[str] = None,
        options: Optional[List[str]] = None,
        is_anonymous: Optional[bool] = None,
        type: Optional[str] = None,
        allows_multiple_answers: Optional[bool] = None,
        correct_option_id: Optional[int] = None,
        explanation: Optional[str] = None,
        explanation_parse_mode: Optional[str] = None,
        explanation_entities: Optional[List[MessageEntity]] = None,
        open_period: Optional[int] = None,
        close_date: Optional[int] = None,
        is_closed: Optional[bool] = None,
        disable_notification: Optional[bool] = None,
        protect_content: Optional[bool] = None,
        reply_to_message_id: Optional[int] = None,
        allow_sending_without_reply: Optional[bool] = None,
        reply_markup: Optional[
            Union[
                InlineKeyboardMarkup,
                ReplyKeyboardMarkup,
                ReplyKeyboardRemove,
                ForceReply,
            ]
        ] = None,
        **kwargs
    ) -> Message:
        response = await self.api.request("sendPoll", self.get_params(locals()))
        return Message(**response)

    async def send_dice(
        self,
        chat_id: Optional[Union[int, str]] = None,
        emoji: Optional[str] = None,
        disable_notification: Optional[bool] = None,
        protect_content: Optional[bool] = None,
        reply_to_message_id: Optional[int] = None,
        allow_sending_without_reply: Optional[bool] = None,
        reply_markup: Optional[
            Union[
                InlineKeyboardMarkup,
                ReplyKeyboardMarkup,
                ReplyKeyboardRemove,
                ForceReply,
            ]
        ] = None,
        **kwargs
    ) -> Message:
        response = await self.api.request("sendDice", self.get_params(locals()))
        return Message(**response)

    async def send_chat_action(
        self,
        chat_id: Optional[Union[int, str]] = None,
        action: Optional[str] = None,
        **kwargs
    ) -> bool:
        response = await self.api.request("sendChatAction", self.get_params(locals()))
        return response

    async def get_user_profile_photos(
        self,
        user_id: Optional[int] = None,
        offset: Optional[int] = None,
        limit: Optional[int] = None,
        **kwargs
    ) -> UserProfilePhotos:
        response = await self.api.request(
            "getUserProfilePhotos", self.get_params(locals())
        )
        return UserProfilePhotos(**response)

    async def get_file(self, file_id: Optional[str] = None, **kwargs) -> File:
        response = await self.api.request("getFile", self.get_params(locals()))
        return File(**response)

    async def ban_chat_member(
        self,
        chat_id: Optional[Union[int, str]] = None,
        user_id: Optional[int] = None,
        until_date: Optional[int] = None,
        revoke_messages: Optional[bool] = None,
        **kwargs
    ) -> bool:
        response = await self.api.request("banChatMember", self.get_params(locals()))
        return response

    async def unban_chat_member(
        self,
        chat_id: Optional[Union[int, str]] = None,
        user_id: Optional[int] = None,
        only_if_banned: Optional[bool] = None,
        **kwargs
    ) -> bool:
        response = await self.api.request("unbanChatMember", self.get_params(locals()))
        return response

    async def restrict_chat_member(
        self,
        chat_id: Optional[Union[int, str]] = None,
        user_id: Optional[int] = None,
        permissions: Optional[ChatPermissions] = None,
        until_date: Optional[int] = None,
        **kwargs
    ) -> bool:
        response = await self.api.request(
            "restrictChatMember", self.get_params(locals())
        )
        return response

    async def promote_chat_member(
        self,
        chat_id: Optional[Union[int, str]] = None,
        user_id: Optional[int] = None,
        is_anonymous: Optional[bool] = None,
        can_manage_chat: Optional[bool] = None,
        can_post_messages: Optional[bool] = None,
        can_edit_messages: Optional[bool] = None,
        can_delete_messages: Optional[bool] = None,
        can_manage_video_chats: Optional[bool] = None,
        can_restrict_members: Optional[bool] = None,
        can_promote_members: Optional[bool] = None,
        can_change_info: Optional[bool] = None,
        can_invite_users: Optional[bool] = None,
        can_pin_messages: Optional[bool] = None,
        **kwargs
    ) -> bool:
        response = await self.api.request(
            "promoteChatMember", self.get_params(locals())
        )
        return response

    async def set_chat_administrator_custom_title(
        self,
        chat_id: Optional[Union[int, str]] = None,
        user_id: Optional[int] = None,
        custom_title: Optional[str] = None,
        **kwargs
    ) -> bool:
        response = await self.api.request(
            "setChatAdministratorCustomTitle", self.get_params(locals())
        )
        return response

    async def ban_chat_sender_chat(
        self,
        chat_id: Optional[Union[int, str]] = None,
        sender_chat_id: Optional[int] = None,
        **kwargs
    ) -> bool:
        response = await self.api.request(
            "banChatSenderChat", self.get_params(locals())
        )
        return response

    async def unban_chat_sender_chat(
        self,
        chat_id: Optional[Union[int, str]] = None,
        sender_chat_id: Optional[int] = None,
        **kwargs
    ) -> bool:
        response = await self.api.request(
            "unbanChatSenderChat", self.get_params(locals())
        )
        return response

    async def set_chat_permissions(
        self,
        chat_id: Optional[Union[int, str]] = None,
        permissions: Optional[ChatPermissions] = None,
        **kwargs
    ) -> bool:
        response = await self.api.request(
            "setChatPermissions", self.get_params(locals())
        )
        return response

    async def export_chat_invite_link(
        self, chat_id: Optional[Union[int, str]] = None, **kwargs
    ) -> str:
        response = await self.api.request(
            "exportChatInviteLink", self.get_params(locals())
        )
        return response

    async def create_chat_invite_link(
        self,
        chat_id: Optional[Union[int, str]] = None,
        name: Optional[str] = None,
        expire_date: Optional[int] = None,
        member_limit: Optional[int] = None,
        creates_join_request: Optional[bool] = None,
        **kwargs
    ) -> ChatInviteLink:
        response = await self.api.request(
            "createChatInviteLink", self.get_params(locals())
        )
        return ChatInviteLink(**response)

    async def edit_chat_invite_link(
        self,
        chat_id: Optional[Union[int, str]] = None,
        invite_link: Optional[str] = None,
        name: Optional[str] = None,
        expire_date: Optional[int] = None,
        member_limit: Optional[int] = None,
        creates_join_request: Optional[bool] = None,
        **kwargs
    ) -> ChatInviteLink:
        response = await self.api.request(
            "editChatInviteLink", self.get_params(locals())
        )
        return ChatInviteLink(**response)

    async def revoke_chat_invite_link(
        self,
        chat_id: Optional[Union[int, str]] = None,
        invite_link: Optional[str] = None,
        **kwargs
    ) -> ChatInviteLink:
        response = await self.api.request(
            "revokeChatInviteLink", self.get_params(locals())
        )
        return ChatInviteLink(**response)

    async def approve_chat_join_request(
        self,
        chat_id: Optional[Union[int, str]] = None,
        user_id: Optional[int] = None,
        **kwargs
    ) -> bool:
        response = await self.api.request(
            "approveChatJoinRequest", self.get_params(locals())
        )
        return response

    async def decline_chat_join_request(
        self,
        chat_id: Optional[Union[int, str]] = None,
        user_id: Optional[int] = None,
        **kwargs
    ) -> bool:
        response = await self.api.request(
            "declineChatJoinRequest", self.get_params(locals())
        )
        return response

    async def set_chat_photo(
        self,
        chat_id: Optional[Union[int, str]] = None,
        photo: Optional[InputFile] = None,
        **kwargs
    ) -> bool:
        response = await self.api.request("setChatPhoto", self.get_params(locals()))
        return response

    async def delete_chat_photo(
        self, chat_id: Optional[Union[int, str]] = None, **kwargs
    ) -> bool:
        response = await self.api.request("deleteChatPhoto", self.get_params(locals()))
        return response

    async def set_chat_title(
        self,
        chat_id: Optional[Union[int, str]] = None,
        title: Optional[str] = None,
        **kwargs
    ) -> bool:
        response = await self.api.request("setChatTitle", self.get_params(locals()))
        return response

    async def set_chat_description(
        self,
        chat_id: Optional[Union[int, str]] = None,
        description: Optional[str] = None,
        **kwargs
    ) -> bool:
        response = await self.api.request(
            "setChatDescription", self.get_params(locals())
        )
        return response

    async def pin_chat_message(
        self,
        chat_id: Optional[Union[int, str]] = None,
        message_id: Optional[int] = None,
        disable_notification: Optional[bool] = None,
        **kwargs
    ) -> bool:
        response = await self.api.request("pinChatMessage", self.get_params(locals()))
        return response

    async def unpin_chat_message(
        self,
        chat_id: Optional[Union[int, str]] = None,
        message_id: Optional[int] = None,
        **kwargs
    ) -> bool:
        response = await self.api.request("unpinChatMessage", self.get_params(locals()))
        return response

    async def unpin_all_chat_messages(
        self, chat_id: Optional[Union[int, str]] = None, **kwargs
    ) -> bool:
        response = await self.api.request(
            "unpinAllChatMessages", self.get_params(locals())
        )
        return response

    async def leave_chat(
        self, chat_id: Optional[Union[int, str]] = None, **kwargs
    ) -> bool:
        response = await self.api.request("leaveChat", self.get_params(locals()))
        return response

    async def get_chat(
        self, chat_id: Optional[Union[int, str]] = None, **kwargs
    ) -> Chat:
        response = await self.api.request("getChat", self.get_params(locals()))
        return Chat(**response)

    async def get_chat_administrators(
        self, chat_id: Optional[Union[int, str]] = None, **kwargs
    ) -> List[ChatMember]:
        response = await self.api.request(
            "getChatAdministrators", self.get_params(locals())
        )
        return parse_obj_as(List[ChatMember], response)

    async def get_chat_member_count(
        self, chat_id: Optional[Union[int, str]] = None, **kwargs
    ) -> int:
        response = await self.api.request(
            "getChatMemberCount", self.get_params(locals())
        )
        return response

    async def get_chat_member(
        self,
        chat_id: Optional[Union[int, str]] = None,
        user_id: Optional[int] = None,
        **kwargs
    ) -> ChatMember:
        response = await self.api.request("getChatMember", self.get_params(locals()))
        return ChatMember(**response)

    async def set_chat_sticker_set(
        self,
        chat_id: Optional[Union[int, str]] = None,
        sticker_set_name: Optional[str] = None,
        **kwargs
    ) -> bool:
        response = await self.api.request(
            "setChatStickerSet", self.get_params(locals())
        )
        return response

    async def delete_chat_sticker_set(
        self, chat_id: Optional[Union[int, str]] = None, **kwargs
    ) -> bool:
        response = await self.api.request(
            "deleteChatStickerSet", self.get_params(locals())
        )
        return response

    async def answer_callback_query(
        self,
        callback_query_id: Optional[str] = None,
        text: Optional[str] = None,
        show_alert: Optional[bool] = None,
        url: Optional[str] = None,
        cache_time: Optional[int] = None,
        **kwargs
    ) -> bool:
        response = await self.api.request(
            "answerCallbackQuery", self.get_params(locals())
        )
        return response

    async def set_my_commands(
        self,
        commands: Optional[List[BotCommand]] = None,
        scope: Optional[BotCommandScope] = None,
        language_code: Optional[str] = None,
        **kwargs
    ) -> bool:
        response = await self.api.request("setMyCommands", self.get_params(locals()))
        return response

    async def delete_my_commands(
        self,
        scope: Optional[BotCommandScope] = None,
        language_code: Optional[str] = None,
        **kwargs
    ) -> bool:
        response = await self.api.request("deleteMyCommands", self.get_params(locals()))
        return response

    async def get_my_commands(
        self,
        scope: Optional[BotCommandScope] = None,
        language_code: Optional[str] = None,
        **kwargs
    ) -> List[BotCommand]:
        response = await self.api.request("getMyCommands", self.get_params(locals()))
        return parse_obj_as(List[BotCommand], response)

    async def set_chat_menu_button(
        self,
        chat_id: Optional[int] = None,
        menu_button: Optional[MenuButton] = None,
        **kwargs
    ) -> bool:
        response = await self.api.request(
            "setChatMenuButton", self.get_params(locals())
        )
        return response

    async def get_chat_menu_button(
        self, chat_id: Optional[int] = None, **kwargs
    ) -> MenuButton:
        response = await self.api.request(
            "getChatMenuButton", self.get_params(locals())
        )
        return MenuButton(**response)

    async def set_my_default_administrator_rights(
        self,
        rights: Optional[ChatAdministratorRights] = None,
        for_channels: Optional[bool] = None,
        **kwargs
    ) -> bool:
        response = await self.api.request(
            "setMyDefaultAdministratorRights", self.get_params(locals())
        )
        return response

    async def get_my_default_administrator_rights(
        self, for_channels: Optional[bool] = None, **kwargs
    ) -> ChatAdministratorRights:
        response = await self.api.request(
            "getMyDefaultAdministratorRights", self.get_params(locals())
        )
        return ChatAdministratorRights(**response)

    async def edit_message_text(
        self,
        chat_id: Optional[Union[int, str]] = None,
        message_id: Optional[int] = None,
        inline_message_id: Optional[str] = None,
        text: Optional[str] = None,
        parse_mode: Optional[str] = None,
        entities: Optional[List[MessageEntity]] = None,
        disable_web_page_preview: Optional[bool] = None,
        reply_markup: Optional[InlineKeyboardMarkup] = None,
        **kwargs
    ) -> Union[Message, bool]:
        response = await self.api.request("editMessageText", self.get_params(locals()))
        return parse_obj_as(Union[Message, bool], response)

    async def edit_message_caption(
        self,
        chat_id: Optional[Union[int, str]] = None,
        message_id: Optional[int] = None,
        inline_message_id: Optional[str] = None,
        caption: Optional[str] = None,
        parse_mode: Optional[str] = None,
        caption_entities: Optional[List[MessageEntity]] = None,
        reply_markup: Optional[InlineKeyboardMarkup] = None,
        **kwargs
    ) -> Union[Message, bool]:
        response = await self.api.request(
            "editMessageCaption", self.get_params(locals())
        )
        return parse_obj_as(Union[Message, bool], response)

    async def edit_message_media(
        self,
        chat_id: Optional[Union[int, str]] = None,
        message_id: Optional[int] = None,
        inline_message_id: Optional[str] = None,
        media: Optional[InputMedia] = None,
        reply_markup: Optional[InlineKeyboardMarkup] = None,
        **kwargs
    ) -> Union[Message, bool]:
        response = await self.api.request("editMessageMedia", self.get_params(locals()))
        return parse_obj_as(Union[Message, bool], response)

    async def edit_message_reply_markup(
        self,
        chat_id: Optional[Union[int, str]] = None,
        message_id: Optional[int] = None,
        inline_message_id: Optional[str] = None,
        reply_markup: Optional[InlineKeyboardMarkup] = None,
        **kwargs
    ) -> Union[Message, bool]:
        response = await self.api.request(
            "editMessageReplyMarkup", self.get_params(locals())
        )
        return parse_obj_as(Union[Message, bool], response)

    async def stop_poll(
        self,
        chat_id: Optional[Union[int, str]] = None,
        message_id: Optional[int] = None,
        reply_markup: Optional[InlineKeyboardMarkup] = None,
        **kwargs
    ) -> Poll:
        response = await self.api.request("stopPoll", self.get_params(locals()))
        return Poll(**response)

    async def delete_message(
        self,
        chat_id: Optional[Union[int, str]] = None,
        message_id: Optional[int] = None,
        **kwargs
    ) -> bool:
        response = await self.api.request("deleteMessage", self.get_params(locals()))
        return response

    async def send_sticker(
        self,
        chat_id: Optional[Union[int, str]] = None,
        sticker: Optional[Union[InputFile, str]] = None,
        disable_notification: Optional[bool] = None,
        protect_content: Optional[bool] = None,
        reply_to_message_id: Optional[int] = None,
        allow_sending_without_reply: Optional[bool] = None,
        reply_markup: Optional[
            Union[
                InlineKeyboardMarkup,
                ReplyKeyboardMarkup,
                ReplyKeyboardRemove,
                ForceReply,
            ]
        ] = None,
        **kwargs
    ) -> Message:
        response = await self.api.request("sendSticker", self.get_params(locals()))
        return Message(**response)

    async def get_sticker_set(self, name: Optional[str] = None, **kwargs) -> StickerSet:
        response = await self.api.request("getStickerSet", self.get_params(locals()))
        return StickerSet(**response)

    async def upload_sticker_file(
        self,
        user_id: Optional[int] = None,
        png_sticker: Optional[InputFile] = None,
        **kwargs
    ) -> File:
        response = await self.api.request(
            "uploadStickerFile", self.get_params(locals())
        )
        return File(**response)

    async def create_new_sticker_set(
        self,
        user_id: Optional[int] = None,
        name: Optional[str] = None,
        title: Optional[str] = None,
        png_sticker: Optional[Union[InputFile, str]] = None,
        tgs_sticker: Optional[InputFile] = None,
        webm_sticker: Optional[InputFile] = None,
        emojis: Optional[str] = None,
        contains_masks: Optional[bool] = None,
        mask_position: Optional[MaskPosition] = None,
        **kwargs
    ) -> bool:
        response = await self.api.request(
            "createNewStickerSet", self.get_params(locals())
        )
        return response

    async def add_sticker_to_set(
        self,
        user_id: Optional[int] = None,
        name: Optional[str] = None,
        png_sticker: Optional[Union[InputFile, str]] = None,
        tgs_sticker: Optional[InputFile] = None,
        webm_sticker: Optional[InputFile] = None,
        emojis: Optional[str] = None,
        mask_position: Optional[MaskPosition] = None,
        **kwargs
    ) -> bool:
        response = await self.api.request("addStickerToSet", self.get_params(locals()))
        return response

    async def set_sticker_position_in_set(
        self, sticker: Optional[str] = None, position: Optional[int] = None, **kwargs
    ) -> bool:
        response = await self.api.request(
            "setStickerPositionInSet", self.get_params(locals())
        )
        return response

    async def delete_sticker_from_set(
        self, sticker: Optional[str] = None, **kwargs
    ) -> bool:
        response = await self.api.request(
            "deleteStickerFromSet", self.get_params(locals())
        )
        return response

    async def set_sticker_set_thumb(
        self,
        name: Optional[str] = None,
        user_id: Optional[int] = None,
        thumb: Optional[Union[InputFile, str]] = None,
        **kwargs
    ) -> bool:
        response = await self.api.request(
            "setStickerSetThumb", self.get_params(locals())
        )
        return response

    async def answer_inline_query(
        self,
        inline_query_id: Optional[str] = None,
        results: Optional[List[InlineQueryResult]] = None,
        cache_time: Optional[int] = None,
        is_personal: Optional[bool] = None,
        next_offset: Optional[str] = None,
        switch_pm_text: Optional[str] = None,
        switch_pm_parameter: Optional[str] = None,
        **kwargs
    ) -> bool:
        response = await self.api.request(
            "answerInlineQuery", self.get_params(locals())
        )
        return response

    async def answer_web_app_query(
        self,
        web_app_query_id: Optional[str] = None,
        result: Optional[InlineQueryResult] = None,
        **kwargs
    ) -> SentWebAppMessage:
        response = await self.api.request(
            "answerWebAppQuery", self.get_params(locals())
        )
        return SentWebAppMessage(**response)

    async def send_invoice(
        self,
        chat_id: Optional[Union[int, str]] = None,
        title: Optional[str] = None,
        description: Optional[str] = None,
        payload: Optional[str] = None,
        provider_token: Optional[str] = None,
        currency: Optional[str] = None,
        prices: Optional[List[LabeledPrice]] = None,
        max_tip_amount: Optional[int] = None,
        suggested_tip_amounts: Optional[List[int]] = None,
        start_parameter: Optional[str] = None,
        provider_data: Optional[str] = None,
        photo_url: Optional[str] = None,
        photo_size: Optional[int] = None,
        photo_width: Optional[int] = None,
        photo_height: Optional[int] = None,
        need_name: Optional[bool] = None,
        need_phone_number: Optional[bool] = None,
        need_email: Optional[bool] = None,
        need_shipping_address: Optional[bool] = None,
        send_phone_number_to_provider: Optional[bool] = None,
        send_email_to_provider: Optional[bool] = None,
        is_flexible: Optional[bool] = None,
        disable_notification: Optional[bool] = None,
        protect_content: Optional[bool] = None,
        reply_to_message_id: Optional[int] = None,
        allow_sending_without_reply: Optional[bool] = None,
        reply_markup: Optional[InlineKeyboardMarkup] = None,
        **kwargs
    ) -> Message:
        response = await self.api.request("sendInvoice", self.get_params(locals()))
        return Message(**response)

    async def create_invoice_link(
        self,
        title: Optional[str] = None,
        description: Optional[str] = None,
        payload: Optional[str] = None,
        provider_token: Optional[str] = None,
        currency: Optional[str] = None,
        prices: Optional[List[LabeledPrice]] = None,
        max_tip_amount: Optional[int] = None,
        suggested_tip_amounts: Optional[List[int]] = None,
        provider_data: Optional[str] = None,
        photo_url: Optional[str] = None,
        photo_size: Optional[int] = None,
        photo_width: Optional[int] = None,
        photo_height: Optional[int] = None,
        need_name: Optional[bool] = None,
        need_phone_number: Optional[bool] = None,
        need_email: Optional[bool] = None,
        need_shipping_address: Optional[bool] = None,
        send_phone_number_to_provider: Optional[bool] = None,
        send_email_to_provider: Optional[bool] = None,
        is_flexible: Optional[bool] = None,
        **kwargs
    ) -> str:
        response = await self.api.request(
            "createInvoiceLink", self.get_params(locals())
        )
        return response

    async def answer_shipping_query(
        self,
        shipping_query_id: Optional[str] = None,
        ok: Optional[bool] = None,
        shipping_options: Optional[List[ShippingOption]] = None,
        error_message: Optional[str] = None,
        **kwargs
    ) -> bool:
        response = await self.api.request(
            "answerShippingQuery", self.get_params(locals())
        )
        return response

    async def answer_pre_checkout_query(
        self,
        pre_checkout_query_id: Optional[str] = None,
        ok: Optional[bool] = None,
        error_message: Optional[str] = None,
        **kwargs
    ) -> bool:
        response = await self.api.request(
            "answerPreCheckoutQuery", self.get_params(locals())
        )
        return response

    async def set_passport_data_errors(
        self,
        user_id: Optional[int] = None,
        errors: Optional[List[PassportElementError]] = None,
        **kwargs
    ) -> bool:
        response = await self.api.request(
            "setPassportDataErrors", self.get_params(locals())
        )
        return response

    async def send_game(
        self,
        chat_id: Optional[int] = None,
        game_short_name: Optional[str] = None,
        disable_notification: Optional[bool] = None,
        protect_content: Optional[bool] = None,
        reply_to_message_id: Optional[int] = None,
        allow_sending_without_reply: Optional[bool] = None,
        reply_markup: Optional[InlineKeyboardMarkup] = None,
        **kwargs
    ) -> Message:
        response = await self.api.request("sendGame", self.get_params(locals()))
        return Message(**response)

    async def set_game_score(
        self,
        user_id: Optional[int] = None,
        score: Optional[int] = None,
        force: Optional[bool] = None,
        disable_edit_message: Optional[bool] = None,
        chat_id: Optional[int] = None,
        message_id: Optional[int] = None,
        inline_message_id: Optional[str] = None,
        **kwargs
    ) -> Union[Message, bool]:
        response = await self.api.request("setGameScore", self.get_params(locals()))
        return parse_obj_as(Union[Message, bool], response)

    async def get_game_high_scores(
        self,
        user_id: Optional[int] = None,
        chat_id: Optional[int] = None,
        message_id: Optional[int] = None,
        inline_message_id: Optional[str] = None,
        **kwargs
    ) -> List[GameHighScore]:
        response = await self.api.request(
            "getGameHighScores", self.get_params(locals())
        )
        return parse_obj_as(List[GameHighScore], response)
