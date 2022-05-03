import typing
import inspect

from .base import BaseObject, Field


class Error(BaseObject):
    ok: typing.Optional[bool] = Field(default=None)
    error_code: typing.Optional[int] = Field(default=None)
    description: typing.Optional[str] = Field(default=None)
    parameters: typing.Optional["ResponseParameters"] = Field(default=None)


class Update(BaseObject):
    update_id: typing.Optional[int] = Field(default=None)
    message: typing.Optional["Message"] = Field(default=None)
    edited_message: typing.Optional["Message"] = Field(default=None)
    channel_post: typing.Optional["Message"] = Field(default=None)
    edited_channel_post: typing.Optional["Message"] = Field(default=None)
    inline_query: typing.Optional["InlineQuery"] = Field(default=None)
    chosen_inline_result: typing.Optional["ChosenInlineResult"] = Field(default=None)
    callback_query: typing.Optional["CallbackQuery"] = Field(default=None)
    shipping_query: typing.Optional["ShippingQuery"] = Field(default=None)
    pre_checkout_query: typing.Optional["PreCheckoutQuery"] = Field(default=None)
    poll: typing.Optional["Poll"] = Field(default=None)
    poll_answer: typing.Optional["PollAnswer"] = Field(default=None)
    my_chat_member: typing.Optional["ChatMemberUpdated"] = Field(default=None)
    chat_member: typing.Optional["ChatMemberUpdated"] = Field(default=None)
    chat_join_request: typing.Optional["ChatJoinRequest"] = Field(default=None)


class WebhookInfo(BaseObject):
    url: typing.Optional[str] = Field(default=None)
    has_custom_certificate: typing.Optional[bool] = Field(default=None)
    pending_update_count: typing.Optional[int] = Field(default=None)
    ip_address: typing.Optional[str] = Field(default=None)
    last_error_date: typing.Optional[int] = Field(default=None)
    last_error_message: typing.Optional[str] = Field(default=None)
    last_synchronization_error_date: typing.Optional[int] = Field(default=None)
    max_connections: typing.Optional[int] = Field(default=None)
    allowed_updates: typing.Optional[typing.List[str]] = Field(default=None)


class User(BaseObject):
    id: typing.Optional[int] = Field(default=None)
    is_bot: typing.Optional[bool] = Field(default=None)
    first_name: typing.Optional[str] = Field(default=None)
    last_name: typing.Optional[str] = Field(default=None)
    username: typing.Optional[str] = Field(default=None)
    language_code: typing.Optional[str] = Field(default=None)
    can_join_groups: typing.Optional[bool] = Field(default=None)
    can_read_all_group_messages: typing.Optional[bool] = Field(default=None)
    supports_inline_queries: typing.Optional[bool] = Field(default=None)


class Chat(BaseObject):
    id: typing.Optional[int] = Field(default=None)
    type: typing.Optional[str] = Field(default=None)
    title: typing.Optional[str] = Field(default=None)
    username: typing.Optional[str] = Field(default=None)
    first_name: typing.Optional[str] = Field(default=None)
    last_name: typing.Optional[str] = Field(default=None)
    photo: typing.Optional["ChatPhoto"] = Field(default=None)
    bio: typing.Optional[str] = Field(default=None)
    has_private_forwards: typing.Optional[bool] = Field(default=None)
    description: typing.Optional[str] = Field(default=None)
    invite_link: typing.Optional[str] = Field(default=None)
    pinned_message: typing.Optional["Message"] = Field(default=None)
    permissions: typing.Optional["ChatPermissions"] = Field(default=None)
    slow_mode_delay: typing.Optional[int] = Field(default=None)
    message_auto_delete_time: typing.Optional[int] = Field(default=None)
    has_protected_content: typing.Optional[bool] = Field(default=None)
    sticker_set_name: typing.Optional[str] = Field(default=None)
    can_set_sticker_set: typing.Optional[bool] = Field(default=None)
    linked_chat_id: typing.Optional[int] = Field(default=None)
    location: typing.Optional["ChatLocation"] = Field(default=None)


class Message(BaseObject):
    message_id: typing.Optional[int] = Field(default=None)
    from_: typing.Optional["User"] = Field(default=None, alias="from")
    sender_chat: typing.Optional["Chat"] = Field(default=None)
    date: typing.Optional[int] = Field(default=None)
    chat: typing.Optional["Chat"] = Field(default=None)
    forward_from: typing.Optional["User"] = Field(default=None)
    forward_from_chat: typing.Optional["Chat"] = Field(default=None)
    forward_from_message_id: typing.Optional[int] = Field(default=None)
    forward_signature: typing.Optional[str] = Field(default=None)
    forward_sender_name: typing.Optional[str] = Field(default=None)
    forward_date: typing.Optional[int] = Field(default=None)
    is_automatic_forward: typing.Optional[bool] = Field(default=None)
    reply_to_message: typing.Optional["Message"] = Field(default=None)
    via_bot: typing.Optional["User"] = Field(default=None)
    edit_date: typing.Optional[int] = Field(default=None)
    has_protected_content: typing.Optional[bool] = Field(default=None)
    media_group_id: typing.Optional[str] = Field(default=None)
    author_signature: typing.Optional[str] = Field(default=None)
    text: typing.Optional[str] = Field(default=None)
    entities: typing.Optional[typing.List["MessageEntity"]] = Field(default=None)
    animation: typing.Optional["Animation"] = Field(default=None)
    audio: typing.Optional["Audio"] = Field(default=None)
    document: typing.Optional["Document"] = Field(default=None)
    photo: typing.Optional[typing.List["PhotoSize"]] = Field(default=None)
    sticker: typing.Optional["Sticker"] = Field(default=None)
    video: typing.Optional["Video"] = Field(default=None)
    video_note: typing.Optional["VideoNote"] = Field(default=None)
    voice: typing.Optional["Voice"] = Field(default=None)
    caption: typing.Optional[str] = Field(default=None)
    caption_entities: typing.Optional[typing.List["MessageEntity"]] = Field(
        default=None
    )
    contact: typing.Optional["Contact"] = Field(default=None)
    dice: typing.Optional["Dice"] = Field(default=None)
    game: typing.Optional["Game"] = Field(default=None)
    poll: typing.Optional["Poll"] = Field(default=None)
    venue: typing.Optional["Venue"] = Field(default=None)
    location: typing.Optional["Location"] = Field(default=None)
    new_chat_members: typing.Optional[typing.List["User"]] = Field(default=None)
    left_chat_member: typing.Optional["User"] = Field(default=None)
    new_chat_title: typing.Optional[str] = Field(default=None)
    new_chat_photo: typing.Optional[typing.List["PhotoSize"]] = Field(default=None)
    delete_chat_photo: typing.Optional[bool] = Field(default=None)
    group_chat_created: typing.Optional[bool] = Field(default=None)
    supergroup_chat_created: typing.Optional[bool] = Field(default=None)
    channel_chat_created: typing.Optional[bool] = Field(default=None)
    message_auto_delete_timer_changed: typing.Optional[
        "MessageAutoDeleteTimerChanged"
    ] = Field(default=None)
    migrate_to_chat_id: typing.Optional[int] = Field(default=None)
    migrate_from_chat_id: typing.Optional[int] = Field(default=None)
    pinned_message: typing.Optional["Message"] = Field(default=None)
    invoice: typing.Optional["Invoice"] = Field(default=None)
    successful_payment: typing.Optional["SuccessfulPayment"] = Field(default=None)
    connected_website: typing.Optional[str] = Field(default=None)
    passport_data: typing.Optional["PassportData"] = Field(default=None)
    proximity_alert_triggered: typing.Optional["ProximityAlertTriggered"] = Field(
        default=None
    )
    video_chat_scheduled: typing.Optional["VideoChatScheduled"] = Field(default=None)
    video_chat_started: typing.Optional["VideoChatStarted"] = Field(default=None)
    video_chat_ended: typing.Optional["VideoChatEnded"] = Field(default=None)
    video_chat_participants_invited: typing.Optional[
        "VideoChatParticipantsInvited"
    ] = Field(default=None)
    web_app_data: typing.Optional["WebAppData"] = Field(default=None)
    reply_markup: typing.Optional["InlineKeyboardMarkup"] = Field(default=None)


class MessageId(BaseObject):
    message_id: typing.Optional[int] = Field(default=None)


class MessageEntity(BaseObject):
    type: typing.Optional[str] = Field(default=None)
    offset: typing.Optional[int] = Field(default=None)
    length: typing.Optional[int] = Field(default=None)
    url: typing.Optional[str] = Field(default=None)
    user: typing.Optional["User"] = Field(default=None)
    language: typing.Optional[str] = Field(default=None)


class PhotoSize(BaseObject):
    file_id: typing.Optional[str] = Field(default=None)
    file_unique_id: typing.Optional[str] = Field(default=None)
    width: typing.Optional[int] = Field(default=None)
    height: typing.Optional[int] = Field(default=None)
    file_size: typing.Optional[int] = Field(default=None)


class Animation(BaseObject):
    file_id: typing.Optional[str] = Field(default=None)
    file_unique_id: typing.Optional[str] = Field(default=None)
    width: typing.Optional[int] = Field(default=None)
    height: typing.Optional[int] = Field(default=None)
    duration: typing.Optional[int] = Field(default=None)
    thumb: typing.Optional["PhotoSize"] = Field(default=None)
    file_name: typing.Optional[str] = Field(default=None)
    mime_type: typing.Optional[str] = Field(default=None)
    file_size: typing.Optional[int] = Field(default=None)


class Audio(BaseObject):
    file_id: typing.Optional[str] = Field(default=None)
    file_unique_id: typing.Optional[str] = Field(default=None)
    duration: typing.Optional[int] = Field(default=None)
    performer: typing.Optional[str] = Field(default=None)
    title: typing.Optional[str] = Field(default=None)
    file_name: typing.Optional[str] = Field(default=None)
    mime_type: typing.Optional[str] = Field(default=None)
    file_size: typing.Optional[int] = Field(default=None)
    thumb: typing.Optional["PhotoSize"] = Field(default=None)


class Document(BaseObject):
    file_id: typing.Optional[str] = Field(default=None)
    file_unique_id: typing.Optional[str] = Field(default=None)
    thumb: typing.Optional["PhotoSize"] = Field(default=None)
    file_name: typing.Optional[str] = Field(default=None)
    mime_type: typing.Optional[str] = Field(default=None)
    file_size: typing.Optional[int] = Field(default=None)


class Video(BaseObject):
    file_id: typing.Optional[str] = Field(default=None)
    file_unique_id: typing.Optional[str] = Field(default=None)
    width: typing.Optional[int] = Field(default=None)
    height: typing.Optional[int] = Field(default=None)
    duration: typing.Optional[int] = Field(default=None)
    thumb: typing.Optional["PhotoSize"] = Field(default=None)
    file_name: typing.Optional[str] = Field(default=None)
    mime_type: typing.Optional[str] = Field(default=None)
    file_size: typing.Optional[int] = Field(default=None)


class VideoNote(BaseObject):
    file_id: typing.Optional[str] = Field(default=None)
    file_unique_id: typing.Optional[str] = Field(default=None)
    length: typing.Optional[int] = Field(default=None)
    duration: typing.Optional[int] = Field(default=None)
    thumb: typing.Optional["PhotoSize"] = Field(default=None)
    file_size: typing.Optional[int] = Field(default=None)


class Voice(BaseObject):
    file_id: typing.Optional[str] = Field(default=None)
    file_unique_id: typing.Optional[str] = Field(default=None)
    duration: typing.Optional[int] = Field(default=None)
    mime_type: typing.Optional[str] = Field(default=None)
    file_size: typing.Optional[int] = Field(default=None)


class Contact(BaseObject):
    phone_number: typing.Optional[str] = Field(default=None)
    first_name: typing.Optional[str] = Field(default=None)
    last_name: typing.Optional[str] = Field(default=None)
    user_id: typing.Optional[int] = Field(default=None)
    vcard: typing.Optional[str] = Field(default=None)


class Dice(BaseObject):
    emoji: typing.Optional[str] = Field(default=None)
    value: typing.Optional[int] = Field(default=None)


class PollOption(BaseObject):
    text: typing.Optional[str] = Field(default=None)
    voter_count: typing.Optional[int] = Field(default=None)


class PollAnswer(BaseObject):
    poll_id: typing.Optional[str] = Field(default=None)
    user: typing.Optional["User"] = Field(default=None)
    option_ids: typing.Optional[typing.List[int]] = Field(default=None)


class Poll(BaseObject):
    id: typing.Optional[str] = Field(default=None)
    question: typing.Optional[str] = Field(default=None)
    options: typing.Optional[typing.List["PollOption"]] = Field(default=None)
    total_voter_count: typing.Optional[int] = Field(default=None)
    is_closed: typing.Optional[bool] = Field(default=None)
    is_anonymous: typing.Optional[bool] = Field(default=None)
    type: typing.Optional[str] = Field(default=None)
    allows_multiple_answers: typing.Optional[bool] = Field(default=None)
    correct_option_id: typing.Optional[int] = Field(default=None)
    explanation: typing.Optional[str] = Field(default=None)
    explanation_entities: typing.Optional[typing.List["MessageEntity"]] = Field(
        default=None
    )
    open_period: typing.Optional[int] = Field(default=None)
    close_date: typing.Optional[int] = Field(default=None)


class Location(BaseObject):
    longitude: typing.Optional[float] = Field(default=None)
    latitude: typing.Optional[float] = Field(default=None)
    horizontal_accuracy: typing.Optional[float] = Field(default=None)
    live_period: typing.Optional[int] = Field(default=None)
    heading: typing.Optional[int] = Field(default=None)
    proximity_alert_radius: typing.Optional[int] = Field(default=None)


class Venue(BaseObject):
    location: typing.Optional["Location"] = Field(default=None)
    title: typing.Optional[str] = Field(default=None)
    address: typing.Optional[str] = Field(default=None)
    foursquare_id: typing.Optional[str] = Field(default=None)
    foursquare_type: typing.Optional[str] = Field(default=None)
    google_place_id: typing.Optional[str] = Field(default=None)
    google_place_type: typing.Optional[str] = Field(default=None)


class WebAppData(BaseObject):
    data: typing.Optional[str] = Field(default=None)
    button_text: typing.Optional[str] = Field(default=None)


class ProximityAlertTriggered(BaseObject):
    traveler: typing.Optional["User"] = Field(default=None)
    watcher: typing.Optional["User"] = Field(default=None)
    distance: typing.Optional[int] = Field(default=None)


class MessageAutoDeleteTimerChanged(BaseObject):
    message_auto_delete_time: typing.Optional[int] = Field(default=None)


class VideoChatScheduled(BaseObject):
    start_date: typing.Optional[int] = Field(default=None)


class VideoChatStarted(BaseObject):
    pass


class VideoChatEnded(BaseObject):
    duration: typing.Optional[int] = Field(default=None)


class VideoChatParticipantsInvited(BaseObject):
    users: typing.Optional[typing.List["User"]] = Field(default=None)


class UserProfilePhotos(BaseObject):
    total_count: typing.Optional[int] = Field(default=None)
    photos: typing.Optional[typing.List[typing.List["PhotoSize"]]] = Field(default=None)


class File(BaseObject):
    file_id: typing.Optional[str] = Field(default=None)
    file_unique_id: typing.Optional[str] = Field(default=None)
    file_size: typing.Optional[int] = Field(default=None)
    file_path: typing.Optional[str] = Field(default=None)


class WebAppInfo(BaseObject):
    url: typing.Optional[str] = Field(default=None)


class ReplyKeyboardMarkup(BaseObject):
    keyboard: typing.Optional[typing.List[typing.List["KeyboardButton"]]] = Field(
        default=None
    )
    resize_keyboard: typing.Optional[bool] = Field(default=None)
    one_time_keyboard: typing.Optional[bool] = Field(default=None)
    input_field_placeholder: typing.Optional[str] = Field(default=None)
    selective: typing.Optional[bool] = Field(default=None)


class KeyboardButton(BaseObject):
    text: typing.Optional[str] = Field(default=None)
    request_contact: typing.Optional[bool] = Field(default=None)
    request_location: typing.Optional[bool] = Field(default=None)
    request_poll: typing.Optional["KeyboardButtonPollType"] = Field(default=None)
    web_app: typing.Optional["WebAppInfo"] = Field(default=None)


class KeyboardButtonPollType(BaseObject):
    type: typing.Optional[str] = Field(default=None)


class ReplyKeyboardRemove(BaseObject):
    remove_keyboard: typing.Optional[bool] = Field(default=None)
    selective: typing.Optional[bool] = Field(default=None)


class InlineKeyboardMarkup(BaseObject):
    inline_keyboard: typing.Optional[
        typing.List[typing.List["InlineKeyboardButton"]]
    ] = Field(default=None)


class InlineKeyboardButton(BaseObject):
    text: typing.Optional[str] = Field(default=None)
    url: typing.Optional[str] = Field(default=None)
    callback_data: typing.Optional[str] = Field(default=None)
    web_app: typing.Optional["WebAppInfo"] = Field(default=None)
    login_url: typing.Optional["LoginUrl"] = Field(default=None)
    switch_inline_query: typing.Optional[str] = Field(default=None)
    switch_inline_query_current_chat: typing.Optional[str] = Field(default=None)
    callback_game: typing.Optional["CallbackGame"] = Field(default=None)
    pay: typing.Optional[bool] = Field(default=None)


class LoginUrl(BaseObject):
    url: typing.Optional[str] = Field(default=None)
    forward_text: typing.Optional[str] = Field(default=None)
    bot_username: typing.Optional[str] = Field(default=None)
    request_write_access: typing.Optional[bool] = Field(default=None)


class CallbackQuery(BaseObject):
    id: typing.Optional[str] = Field(default=None)
    from_: typing.Optional["User"] = Field(default=None, alias="from")
    message: typing.Optional["Message"] = Field(default=None)
    inline_message_id: typing.Optional[str] = Field(default=None)
    chat_instance: typing.Optional[str] = Field(default=None)
    data: typing.Optional[str] = Field(default=None)
    game_short_name: typing.Optional[str] = Field(default=None)


class ForceReply(BaseObject):
    force_reply: typing.Optional[bool] = Field(default=None)
    input_field_placeholder: typing.Optional[str] = Field(default=None)
    selective: typing.Optional[bool] = Field(default=None)


class ChatPhoto(BaseObject):
    small_file_id: typing.Optional[str] = Field(default=None)
    small_file_unique_id: typing.Optional[str] = Field(default=None)
    big_file_id: typing.Optional[str] = Field(default=None)
    big_file_unique_id: typing.Optional[str] = Field(default=None)


class ChatInviteLink(BaseObject):
    invite_link: typing.Optional[str] = Field(default=None)
    creator: typing.Optional["User"] = Field(default=None)
    creates_join_request: typing.Optional[bool] = Field(default=None)
    is_primary: typing.Optional[bool] = Field(default=None)
    is_revoked: typing.Optional[bool] = Field(default=None)
    name: typing.Optional[str] = Field(default=None)
    expire_date: typing.Optional[int] = Field(default=None)
    member_limit: typing.Optional[int] = Field(default=None)
    pending_join_request_count: typing.Optional[int] = Field(default=None)


class ChatAdministratorRights(BaseObject):
    is_anonymous: typing.Optional[bool] = Field(default=None)
    can_manage_chat: typing.Optional[bool] = Field(default=None)
    can_delete_messages: typing.Optional[bool] = Field(default=None)
    can_manage_video_chats: typing.Optional[bool] = Field(default=None)
    can_restrict_members: typing.Optional[bool] = Field(default=None)
    can_promote_members: typing.Optional[bool] = Field(default=None)
    can_change_info: typing.Optional[bool] = Field(default=None)
    can_invite_users: typing.Optional[bool] = Field(default=None)
    can_post_messages: typing.Optional[bool] = Field(default=None)
    can_edit_messages: typing.Optional[bool] = Field(default=None)
    can_pin_messages: typing.Optional[bool] = Field(default=None)


class ChatMember(BaseObject):
    pass


class ChatMemberOwner(BaseObject):
    status: typing.Optional[str] = Field(default=None)
    user: typing.Optional["User"] = Field(default=None)
    is_anonymous: typing.Optional[bool] = Field(default=None)
    custom_title: typing.Optional[str] = Field(default=None)


class ChatMemberAdministrator(BaseObject):
    status: typing.Optional[str] = Field(default=None)
    user: typing.Optional["User"] = Field(default=None)
    can_be_edited: typing.Optional[bool] = Field(default=None)
    is_anonymous: typing.Optional[bool] = Field(default=None)
    can_manage_chat: typing.Optional[bool] = Field(default=None)
    can_delete_messages: typing.Optional[bool] = Field(default=None)
    can_manage_video_chats: typing.Optional[bool] = Field(default=None)
    can_restrict_members: typing.Optional[bool] = Field(default=None)
    can_promote_members: typing.Optional[bool] = Field(default=None)
    can_change_info: typing.Optional[bool] = Field(default=None)
    can_invite_users: typing.Optional[bool] = Field(default=None)
    can_post_messages: typing.Optional[bool] = Field(default=None)
    can_edit_messages: typing.Optional[bool] = Field(default=None)
    can_pin_messages: typing.Optional[bool] = Field(default=None)
    custom_title: typing.Optional[str] = Field(default=None)


class ChatMemberMember(BaseObject):
    status: typing.Optional[str] = Field(default=None)
    user: typing.Optional["User"] = Field(default=None)


class ChatMemberRestricted(BaseObject):
    status: typing.Optional[str] = Field(default=None)
    user: typing.Optional["User"] = Field(default=None)
    is_member: typing.Optional[bool] = Field(default=None)
    can_change_info: typing.Optional[bool] = Field(default=None)
    can_invite_users: typing.Optional[bool] = Field(default=None)
    can_pin_messages: typing.Optional[bool] = Field(default=None)
    can_send_messages: typing.Optional[bool] = Field(default=None)
    can_send_media_messages: typing.Optional[bool] = Field(default=None)
    can_send_polls: typing.Optional[bool] = Field(default=None)
    can_send_other_messages: typing.Optional[bool] = Field(default=None)
    can_add_web_page_previews: typing.Optional[bool] = Field(default=None)
    until_date: typing.Optional[int] = Field(default=None)


class ChatMemberLeft(BaseObject):
    status: typing.Optional[str] = Field(default=None)
    user: typing.Optional["User"] = Field(default=None)


class ChatMemberBanned(BaseObject):
    status: typing.Optional[str] = Field(default=None)
    user: typing.Optional["User"] = Field(default=None)
    until_date: typing.Optional[int] = Field(default=None)


class ChatMemberUpdated(BaseObject):
    chat: typing.Optional["Chat"] = Field(default=None)
    from_: typing.Optional["User"] = Field(default=None, alias="from")
    date: typing.Optional[int] = Field(default=None)
    old_chat_member: typing.Optional["ChatMember"] = Field(default=None)
    new_chat_member: typing.Optional["ChatMember"] = Field(default=None)
    invite_link: typing.Optional["ChatInviteLink"] = Field(default=None)


class ChatJoinRequest(BaseObject):
    chat: typing.Optional["Chat"] = Field(default=None)
    from_: typing.Optional["User"] = Field(default=None, alias="from")
    date: typing.Optional[int] = Field(default=None)
    bio: typing.Optional[str] = Field(default=None)
    invite_link: typing.Optional["ChatInviteLink"] = Field(default=None)


class ChatPermissions(BaseObject):
    can_send_messages: typing.Optional[bool] = Field(default=None)
    can_send_media_messages: typing.Optional[bool] = Field(default=None)
    can_send_polls: typing.Optional[bool] = Field(default=None)
    can_send_other_messages: typing.Optional[bool] = Field(default=None)
    can_add_web_page_previews: typing.Optional[bool] = Field(default=None)
    can_change_info: typing.Optional[bool] = Field(default=None)
    can_invite_users: typing.Optional[bool] = Field(default=None)
    can_pin_messages: typing.Optional[bool] = Field(default=None)


class ChatLocation(BaseObject):
    location: typing.Optional["Location"] = Field(default=None)
    address: typing.Optional[str] = Field(default=None)


class BotCommand(BaseObject):
    command: typing.Optional[str] = Field(default=None)
    description: typing.Optional[str] = Field(default=None)


class BotCommandScope(BaseObject):
    pass


class BotCommandScopeDefault(BaseObject):
    type: typing.Optional[str] = Field(default=None)


class BotCommandScopeAllPrivateChats(BaseObject):
    type: typing.Optional[str] = Field(default=None)


class BotCommandScopeAllGroupChats(BaseObject):
    type: typing.Optional[str] = Field(default=None)


class BotCommandScopeAllChatAdministrators(BaseObject):
    type: typing.Optional[str] = Field(default=None)


class BotCommandScopeChat(BaseObject):
    type: typing.Optional[str] = Field(default=None)
    chat_id: typing.Optional[typing.Union[int, str]] = Field(default=None)


class BotCommandScopeChatAdministrators(BaseObject):
    type: typing.Optional[str] = Field(default=None)
    chat_id: typing.Optional[typing.Union[int, str]] = Field(default=None)


class BotCommandScopeChatMember(BaseObject):
    type: typing.Optional[str] = Field(default=None)
    chat_id: typing.Optional[typing.Union[int, str]] = Field(default=None)
    user_id: typing.Optional[int] = Field(default=None)


class MenuButton(BaseObject):
    pass


class MenuButtonCommands(BaseObject):
    type: typing.Optional[str] = Field(default=None)


class MenuButtonWebApp(BaseObject):
    type: typing.Optional[str] = Field(default=None)
    text: typing.Optional[str] = Field(default=None)
    web_app: typing.Optional["WebAppInfo"] = Field(default=None)


class MenuButtonDefault(BaseObject):
    type: typing.Optional[str] = Field(default=None)


class ResponseParameters(BaseObject):
    migrate_to_chat_id: typing.Optional[int] = Field(default=None)
    retry_after: typing.Optional[int] = Field(default=None)


class InputMedia(BaseObject):
    pass


class InputMediaPhoto(BaseObject):
    type: typing.Optional[str] = Field(default=None)
    media: typing.Optional[str] = Field(default=None)
    caption: typing.Optional[str] = Field(default=None)
    parse_mode: typing.Optional[str] = Field(default=None)
    caption_entities: typing.Optional[typing.List["MessageEntity"]] = Field(
        default=None
    )


class InputMediaVideo(BaseObject):
    type: typing.Optional[str] = Field(default=None)
    media: typing.Optional[str] = Field(default=None)
    thumb: typing.Optional[typing.Union["InputFile", str]] = Field(default=None)
    caption: typing.Optional[str] = Field(default=None)
    parse_mode: typing.Optional[str] = Field(default=None)
    caption_entities: typing.Optional[typing.List["MessageEntity"]] = Field(
        default=None
    )
    width: typing.Optional[int] = Field(default=None)
    height: typing.Optional[int] = Field(default=None)
    duration: typing.Optional[int] = Field(default=None)
    supports_streaming: typing.Optional[bool] = Field(default=None)


class InputMediaAnimation(BaseObject):
    type: typing.Optional[str] = Field(default=None)
    media: typing.Optional[str] = Field(default=None)
    thumb: typing.Optional[typing.Union["InputFile", str]] = Field(default=None)
    caption: typing.Optional[str] = Field(default=None)
    parse_mode: typing.Optional[str] = Field(default=None)
    caption_entities: typing.Optional[typing.List["MessageEntity"]] = Field(
        default=None
    )
    width: typing.Optional[int] = Field(default=None)
    height: typing.Optional[int] = Field(default=None)
    duration: typing.Optional[int] = Field(default=None)


class InputMediaAudio(BaseObject):
    type: typing.Optional[str] = Field(default=None)
    media: typing.Optional[str] = Field(default=None)
    thumb: typing.Optional[typing.Union["InputFile", str]] = Field(default=None)
    caption: typing.Optional[str] = Field(default=None)
    parse_mode: typing.Optional[str] = Field(default=None)
    caption_entities: typing.Optional[typing.List["MessageEntity"]] = Field(
        default=None
    )
    duration: typing.Optional[int] = Field(default=None)
    performer: typing.Optional[str] = Field(default=None)
    title: typing.Optional[str] = Field(default=None)


class InputMediaDocument(BaseObject):
    type: typing.Optional[str] = Field(default=None)
    media: typing.Optional[str] = Field(default=None)
    thumb: typing.Optional[typing.Union["InputFile", str]] = Field(default=None)
    caption: typing.Optional[str] = Field(default=None)
    parse_mode: typing.Optional[str] = Field(default=None)
    caption_entities: typing.Optional[typing.List["MessageEntity"]] = Field(
        default=None
    )
    disable_content_type_detection: typing.Optional[bool] = Field(default=None)


class InputFile(BaseObject):
    pass


class Sticker(BaseObject):
    file_id: typing.Optional[str] = Field(default=None)
    file_unique_id: typing.Optional[str] = Field(default=None)
    width: typing.Optional[int] = Field(default=None)
    height: typing.Optional[int] = Field(default=None)
    is_animated: typing.Optional[bool] = Field(default=None)
    is_video: typing.Optional[bool] = Field(default=None)
    thumb: typing.Optional["PhotoSize"] = Field(default=None)
    emoji: typing.Optional[str] = Field(default=None)
    set_name: typing.Optional[str] = Field(default=None)
    mask_position: typing.Optional["MaskPosition"] = Field(default=None)
    file_size: typing.Optional[int] = Field(default=None)


class StickerSet(BaseObject):
    name: typing.Optional[str] = Field(default=None)
    title: typing.Optional[str] = Field(default=None)
    is_animated: typing.Optional[bool] = Field(default=None)
    is_video: typing.Optional[bool] = Field(default=None)
    contains_masks: typing.Optional[bool] = Field(default=None)
    stickers: typing.Optional[typing.List["Sticker"]] = Field(default=None)
    thumb: typing.Optional["PhotoSize"] = Field(default=None)


class MaskPosition(BaseObject):
    point: typing.Optional[str] = Field(default=None)
    x_shift: typing.Optional[float] = Field(default=None)
    y_shift: typing.Optional[float] = Field(default=None)
    scale: typing.Optional[float] = Field(default=None)


class InlineQuery(BaseObject):
    id: typing.Optional[str] = Field(default=None)
    from_: typing.Optional["User"] = Field(default=None, alias="from")
    query: typing.Optional[str] = Field(default=None)
    offset: typing.Optional[str] = Field(default=None)
    chat_type: typing.Optional[str] = Field(default=None)
    location: typing.Optional["Location"] = Field(default=None)


class InlineQueryResult(BaseObject):
    pass


class InlineQueryResultArticle(BaseObject):
    type: typing.Optional[str] = Field(default=None)
    id: typing.Optional[str] = Field(default=None)
    title: typing.Optional[str] = Field(default=None)
    input_message_content: typing.Optional["InputMessageContent"] = Field(default=None)
    reply_markup: typing.Optional["InlineKeyboardMarkup"] = Field(default=None)
    url: typing.Optional[str] = Field(default=None)
    hide_url: typing.Optional[bool] = Field(default=None)
    description: typing.Optional[str] = Field(default=None)
    thumb_url: typing.Optional[str] = Field(default=None)
    thumb_width: typing.Optional[int] = Field(default=None)
    thumb_height: typing.Optional[int] = Field(default=None)


class InlineQueryResultPhoto(BaseObject):
    type: typing.Optional[str] = Field(default=None)
    id: typing.Optional[str] = Field(default=None)
    photo_url: typing.Optional[str] = Field(default=None)
    thumb_url: typing.Optional[str] = Field(default=None)
    photo_width: typing.Optional[int] = Field(default=None)
    photo_height: typing.Optional[int] = Field(default=None)
    title: typing.Optional[str] = Field(default=None)
    description: typing.Optional[str] = Field(default=None)
    caption: typing.Optional[str] = Field(default=None)
    parse_mode: typing.Optional[str] = Field(default=None)
    caption_entities: typing.Optional[typing.List["MessageEntity"]] = Field(
        default=None
    )
    reply_markup: typing.Optional["InlineKeyboardMarkup"] = Field(default=None)
    input_message_content: typing.Optional["InputMessageContent"] = Field(default=None)


class InlineQueryResultGif(BaseObject):
    type: typing.Optional[str] = Field(default=None)
    id: typing.Optional[str] = Field(default=None)
    gif_url: typing.Optional[str] = Field(default=None)
    gif_width: typing.Optional[int] = Field(default=None)
    gif_height: typing.Optional[int] = Field(default=None)
    gif_duration: typing.Optional[int] = Field(default=None)
    thumb_url: typing.Optional[str] = Field(default=None)
    thumb_mime_type: typing.Optional[str] = Field(default=None)
    title: typing.Optional[str] = Field(default=None)
    caption: typing.Optional[str] = Field(default=None)
    parse_mode: typing.Optional[str] = Field(default=None)
    caption_entities: typing.Optional[typing.List["MessageEntity"]] = Field(
        default=None
    )
    reply_markup: typing.Optional["InlineKeyboardMarkup"] = Field(default=None)
    input_message_content: typing.Optional["InputMessageContent"] = Field(default=None)


class InlineQueryResultMpeg4Gif(BaseObject):
    type: typing.Optional[str] = Field(default=None)
    id: typing.Optional[str] = Field(default=None)
    mpeg4_url: typing.Optional[str] = Field(default=None)
    mpeg4_width: typing.Optional[int] = Field(default=None)
    mpeg4_height: typing.Optional[int] = Field(default=None)
    mpeg4_duration: typing.Optional[int] = Field(default=None)
    thumb_url: typing.Optional[str] = Field(default=None)
    thumb_mime_type: typing.Optional[str] = Field(default=None)
    title: typing.Optional[str] = Field(default=None)
    caption: typing.Optional[str] = Field(default=None)
    parse_mode: typing.Optional[str] = Field(default=None)
    caption_entities: typing.Optional[typing.List["MessageEntity"]] = Field(
        default=None
    )
    reply_markup: typing.Optional["InlineKeyboardMarkup"] = Field(default=None)
    input_message_content: typing.Optional["InputMessageContent"] = Field(default=None)


class InlineQueryResultVideo(BaseObject):
    type: typing.Optional[str] = Field(default=None)
    id: typing.Optional[str] = Field(default=None)
    video_url: typing.Optional[str] = Field(default=None)
    mime_type: typing.Optional[str] = Field(default=None)
    thumb_url: typing.Optional[str] = Field(default=None)
    title: typing.Optional[str] = Field(default=None)
    caption: typing.Optional[str] = Field(default=None)
    parse_mode: typing.Optional[str] = Field(default=None)
    caption_entities: typing.Optional[typing.List["MessageEntity"]] = Field(
        default=None
    )
    video_width: typing.Optional[int] = Field(default=None)
    video_height: typing.Optional[int] = Field(default=None)
    video_duration: typing.Optional[int] = Field(default=None)
    description: typing.Optional[str] = Field(default=None)
    reply_markup: typing.Optional["InlineKeyboardMarkup"] = Field(default=None)
    input_message_content: typing.Optional["InputMessageContent"] = Field(default=None)


class InlineQueryResultAudio(BaseObject):
    type: typing.Optional[str] = Field(default=None)
    id: typing.Optional[str] = Field(default=None)
    audio_url: typing.Optional[str] = Field(default=None)
    title: typing.Optional[str] = Field(default=None)
    caption: typing.Optional[str] = Field(default=None)
    parse_mode: typing.Optional[str] = Field(default=None)
    caption_entities: typing.Optional[typing.List["MessageEntity"]] = Field(
        default=None
    )
    performer: typing.Optional[str] = Field(default=None)
    audio_duration: typing.Optional[int] = Field(default=None)
    reply_markup: typing.Optional["InlineKeyboardMarkup"] = Field(default=None)
    input_message_content: typing.Optional["InputMessageContent"] = Field(default=None)


class InlineQueryResultVoice(BaseObject):
    type: typing.Optional[str] = Field(default=None)
    id: typing.Optional[str] = Field(default=None)
    voice_url: typing.Optional[str] = Field(default=None)
    title: typing.Optional[str] = Field(default=None)
    caption: typing.Optional[str] = Field(default=None)
    parse_mode: typing.Optional[str] = Field(default=None)
    caption_entities: typing.Optional[typing.List["MessageEntity"]] = Field(
        default=None
    )
    voice_duration: typing.Optional[int] = Field(default=None)
    reply_markup: typing.Optional["InlineKeyboardMarkup"] = Field(default=None)
    input_message_content: typing.Optional["InputMessageContent"] = Field(default=None)


class InlineQueryResultDocument(BaseObject):
    type: typing.Optional[str] = Field(default=None)
    id: typing.Optional[str] = Field(default=None)
    title: typing.Optional[str] = Field(default=None)
    caption: typing.Optional[str] = Field(default=None)
    parse_mode: typing.Optional[str] = Field(default=None)
    caption_entities: typing.Optional[typing.List["MessageEntity"]] = Field(
        default=None
    )
    document_url: typing.Optional[str] = Field(default=None)
    mime_type: typing.Optional[str] = Field(default=None)
    description: typing.Optional[str] = Field(default=None)
    reply_markup: typing.Optional["InlineKeyboardMarkup"] = Field(default=None)
    input_message_content: typing.Optional["InputMessageContent"] = Field(default=None)
    thumb_url: typing.Optional[str] = Field(default=None)
    thumb_width: typing.Optional[int] = Field(default=None)
    thumb_height: typing.Optional[int] = Field(default=None)


class InlineQueryResultLocation(BaseObject):
    type: typing.Optional[str] = Field(default=None)
    id: typing.Optional[str] = Field(default=None)
    latitude: typing.Optional[float] = Field(default=None)
    longitude: typing.Optional[float] = Field(default=None)
    title: typing.Optional[str] = Field(default=None)
    horizontal_accuracy: typing.Optional[float] = Field(default=None)
    live_period: typing.Optional[int] = Field(default=None)
    heading: typing.Optional[int] = Field(default=None)
    proximity_alert_radius: typing.Optional[int] = Field(default=None)
    reply_markup: typing.Optional["InlineKeyboardMarkup"] = Field(default=None)
    input_message_content: typing.Optional["InputMessageContent"] = Field(default=None)
    thumb_url: typing.Optional[str] = Field(default=None)
    thumb_width: typing.Optional[int] = Field(default=None)
    thumb_height: typing.Optional[int] = Field(default=None)


class InlineQueryResultVenue(BaseObject):
    type: typing.Optional[str] = Field(default=None)
    id: typing.Optional[str] = Field(default=None)
    latitude: typing.Optional[float] = Field(default=None)
    longitude: typing.Optional[float] = Field(default=None)
    title: typing.Optional[str] = Field(default=None)
    address: typing.Optional[str] = Field(default=None)
    foursquare_id: typing.Optional[str] = Field(default=None)
    foursquare_type: typing.Optional[str] = Field(default=None)
    google_place_id: typing.Optional[str] = Field(default=None)
    google_place_type: typing.Optional[str] = Field(default=None)
    reply_markup: typing.Optional["InlineKeyboardMarkup"] = Field(default=None)
    input_message_content: typing.Optional["InputMessageContent"] = Field(default=None)
    thumb_url: typing.Optional[str] = Field(default=None)
    thumb_width: typing.Optional[int] = Field(default=None)
    thumb_height: typing.Optional[int] = Field(default=None)


class InlineQueryResultContact(BaseObject):
    type: typing.Optional[str] = Field(default=None)
    id: typing.Optional[str] = Field(default=None)
    phone_number: typing.Optional[str] = Field(default=None)
    first_name: typing.Optional[str] = Field(default=None)
    last_name: typing.Optional[str] = Field(default=None)
    vcard: typing.Optional[str] = Field(default=None)
    reply_markup: typing.Optional["InlineKeyboardMarkup"] = Field(default=None)
    input_message_content: typing.Optional["InputMessageContent"] = Field(default=None)
    thumb_url: typing.Optional[str] = Field(default=None)
    thumb_width: typing.Optional[int] = Field(default=None)
    thumb_height: typing.Optional[int] = Field(default=None)


class InlineQueryResultGame(BaseObject):
    type: typing.Optional[str] = Field(default=None)
    id: typing.Optional[str] = Field(default=None)
    game_short_name: typing.Optional[str] = Field(default=None)
    reply_markup: typing.Optional["InlineKeyboardMarkup"] = Field(default=None)


class InlineQueryResultCachedPhoto(BaseObject):
    type: typing.Optional[str] = Field(default=None)
    id: typing.Optional[str] = Field(default=None)
    photo_file_id: typing.Optional[str] = Field(default=None)
    title: typing.Optional[str] = Field(default=None)
    description: typing.Optional[str] = Field(default=None)
    caption: typing.Optional[str] = Field(default=None)
    parse_mode: typing.Optional[str] = Field(default=None)
    caption_entities: typing.Optional[typing.List["MessageEntity"]] = Field(
        default=None
    )
    reply_markup: typing.Optional["InlineKeyboardMarkup"] = Field(default=None)
    input_message_content: typing.Optional["InputMessageContent"] = Field(default=None)


class InlineQueryResultCachedGif(BaseObject):
    type: typing.Optional[str] = Field(default=None)
    id: typing.Optional[str] = Field(default=None)
    gif_file_id: typing.Optional[str] = Field(default=None)
    title: typing.Optional[str] = Field(default=None)
    caption: typing.Optional[str] = Field(default=None)
    parse_mode: typing.Optional[str] = Field(default=None)
    caption_entities: typing.Optional[typing.List["MessageEntity"]] = Field(
        default=None
    )
    reply_markup: typing.Optional["InlineKeyboardMarkup"] = Field(default=None)
    input_message_content: typing.Optional["InputMessageContent"] = Field(default=None)


class InlineQueryResultCachedMpeg4Gif(BaseObject):
    type: typing.Optional[str] = Field(default=None)
    id: typing.Optional[str] = Field(default=None)
    mpeg4_file_id: typing.Optional[str] = Field(default=None)
    title: typing.Optional[str] = Field(default=None)
    caption: typing.Optional[str] = Field(default=None)
    parse_mode: typing.Optional[str] = Field(default=None)
    caption_entities: typing.Optional[typing.List["MessageEntity"]] = Field(
        default=None
    )
    reply_markup: typing.Optional["InlineKeyboardMarkup"] = Field(default=None)
    input_message_content: typing.Optional["InputMessageContent"] = Field(default=None)


class InlineQueryResultCachedSticker(BaseObject):
    type: typing.Optional[str] = Field(default=None)
    id: typing.Optional[str] = Field(default=None)
    sticker_file_id: typing.Optional[str] = Field(default=None)
    reply_markup: typing.Optional["InlineKeyboardMarkup"] = Field(default=None)
    input_message_content: typing.Optional["InputMessageContent"] = Field(default=None)


class InlineQueryResultCachedDocument(BaseObject):
    type: typing.Optional[str] = Field(default=None)
    id: typing.Optional[str] = Field(default=None)
    title: typing.Optional[str] = Field(default=None)
    document_file_id: typing.Optional[str] = Field(default=None)
    description: typing.Optional[str] = Field(default=None)
    caption: typing.Optional[str] = Field(default=None)
    parse_mode: typing.Optional[str] = Field(default=None)
    caption_entities: typing.Optional[typing.List["MessageEntity"]] = Field(
        default=None
    )
    reply_markup: typing.Optional["InlineKeyboardMarkup"] = Field(default=None)
    input_message_content: typing.Optional["InputMessageContent"] = Field(default=None)


class InlineQueryResultCachedVideo(BaseObject):
    type: typing.Optional[str] = Field(default=None)
    id: typing.Optional[str] = Field(default=None)
    video_file_id: typing.Optional[str] = Field(default=None)
    title: typing.Optional[str] = Field(default=None)
    description: typing.Optional[str] = Field(default=None)
    caption: typing.Optional[str] = Field(default=None)
    parse_mode: typing.Optional[str] = Field(default=None)
    caption_entities: typing.Optional[typing.List["MessageEntity"]] = Field(
        default=None
    )
    reply_markup: typing.Optional["InlineKeyboardMarkup"] = Field(default=None)
    input_message_content: typing.Optional["InputMessageContent"] = Field(default=None)


class InlineQueryResultCachedVoice(BaseObject):
    type: typing.Optional[str] = Field(default=None)
    id: typing.Optional[str] = Field(default=None)
    voice_file_id: typing.Optional[str] = Field(default=None)
    title: typing.Optional[str] = Field(default=None)
    caption: typing.Optional[str] = Field(default=None)
    parse_mode: typing.Optional[str] = Field(default=None)
    caption_entities: typing.Optional[typing.List["MessageEntity"]] = Field(
        default=None
    )
    reply_markup: typing.Optional["InlineKeyboardMarkup"] = Field(default=None)
    input_message_content: typing.Optional["InputMessageContent"] = Field(default=None)


class InlineQueryResultCachedAudio(BaseObject):
    type: typing.Optional[str] = Field(default=None)
    id: typing.Optional[str] = Field(default=None)
    audio_file_id: typing.Optional[str] = Field(default=None)
    caption: typing.Optional[str] = Field(default=None)
    parse_mode: typing.Optional[str] = Field(default=None)
    caption_entities: typing.Optional[typing.List["MessageEntity"]] = Field(
        default=None
    )
    reply_markup: typing.Optional["InlineKeyboardMarkup"] = Field(default=None)
    input_message_content: typing.Optional["InputMessageContent"] = Field(default=None)


class InputMessageContent(BaseObject):
    pass


class InputTextMessageContent(BaseObject):
    message_text: typing.Optional[str] = Field(default=None)
    parse_mode: typing.Optional[str] = Field(default=None)
    entities: typing.Optional[typing.List["MessageEntity"]] = Field(default=None)
    disable_web_page_preview: typing.Optional[bool] = Field(default=None)


class InputLocationMessageContent(BaseObject):
    latitude: typing.Optional[float] = Field(default=None)
    longitude: typing.Optional[float] = Field(default=None)
    horizontal_accuracy: typing.Optional[float] = Field(default=None)
    live_period: typing.Optional[int] = Field(default=None)
    heading: typing.Optional[int] = Field(default=None)
    proximity_alert_radius: typing.Optional[int] = Field(default=None)


class InputVenueMessageContent(BaseObject):
    latitude: typing.Optional[float] = Field(default=None)
    longitude: typing.Optional[float] = Field(default=None)
    title: typing.Optional[str] = Field(default=None)
    address: typing.Optional[str] = Field(default=None)
    foursquare_id: typing.Optional[str] = Field(default=None)
    foursquare_type: typing.Optional[str] = Field(default=None)
    google_place_id: typing.Optional[str] = Field(default=None)
    google_place_type: typing.Optional[str] = Field(default=None)


class InputContactMessageContent(BaseObject):
    phone_number: typing.Optional[str] = Field(default=None)
    first_name: typing.Optional[str] = Field(default=None)
    last_name: typing.Optional[str] = Field(default=None)
    vcard: typing.Optional[str] = Field(default=None)


class InputInvoiceMessageContent(BaseObject):
    title: typing.Optional[str] = Field(default=None)
    description: typing.Optional[str] = Field(default=None)
    payload: typing.Optional[str] = Field(default=None)
    provider_token: typing.Optional[str] = Field(default=None)
    currency: typing.Optional[str] = Field(default=None)
    prices: typing.Optional[typing.List["LabeledPrice"]] = Field(default=None)
    max_tip_amount: typing.Optional[int] = Field(default=None)
    suggested_tip_amounts: typing.Optional[typing.List[int]] = Field(default=None)
    provider_data: typing.Optional[str] = Field(default=None)
    photo_url: typing.Optional[str] = Field(default=None)
    photo_size: typing.Optional[int] = Field(default=None)
    photo_width: typing.Optional[int] = Field(default=None)
    photo_height: typing.Optional[int] = Field(default=None)
    need_name: typing.Optional[bool] = Field(default=None)
    need_phone_number: typing.Optional[bool] = Field(default=None)
    need_email: typing.Optional[bool] = Field(default=None)
    need_shipping_address: typing.Optional[bool] = Field(default=None)
    send_phone_number_to_provider: typing.Optional[bool] = Field(default=None)
    send_email_to_provider: typing.Optional[bool] = Field(default=None)
    is_flexible: typing.Optional[bool] = Field(default=None)


class ChosenInlineResult(BaseObject):
    result_id: typing.Optional[str] = Field(default=None)
    from_: typing.Optional["User"] = Field(default=None, alias="from")
    location: typing.Optional["Location"] = Field(default=None)
    inline_message_id: typing.Optional[str] = Field(default=None)
    query: typing.Optional[str] = Field(default=None)


class SentWebAppMessage(BaseObject):
    inline_message_id: typing.Optional[str] = Field(default=None)


class LabeledPrice(BaseObject):
    label: typing.Optional[str] = Field(default=None)
    amount: typing.Optional[int] = Field(default=None)


class Invoice(BaseObject):
    title: typing.Optional[str] = Field(default=None)
    description: typing.Optional[str] = Field(default=None)
    start_parameter: typing.Optional[str] = Field(default=None)
    currency: typing.Optional[str] = Field(default=None)
    total_amount: typing.Optional[int] = Field(default=None)


class ShippingAddress(BaseObject):
    country_code: typing.Optional[str] = Field(default=None)
    state: typing.Optional[str] = Field(default=None)
    city: typing.Optional[str] = Field(default=None)
    street_line1: typing.Optional[str] = Field(default=None)
    street_line2: typing.Optional[str] = Field(default=None)
    post_code: typing.Optional[str] = Field(default=None)


class OrderInfo(BaseObject):
    name: typing.Optional[str] = Field(default=None)
    phone_number: typing.Optional[str] = Field(default=None)
    email: typing.Optional[str] = Field(default=None)
    shipping_address: typing.Optional["ShippingAddress"] = Field(default=None)


class ShippingOption(BaseObject):
    id: typing.Optional[str] = Field(default=None)
    title: typing.Optional[str] = Field(default=None)
    prices: typing.Optional[typing.List["LabeledPrice"]] = Field(default=None)


class SuccessfulPayment(BaseObject):
    currency: typing.Optional[str] = Field(default=None)
    total_amount: typing.Optional[int] = Field(default=None)
    invoice_payload: typing.Optional[str] = Field(default=None)
    shipping_option_id: typing.Optional[str] = Field(default=None)
    order_info: typing.Optional["OrderInfo"] = Field(default=None)
    telegram_payment_charge_id: typing.Optional[str] = Field(default=None)
    provider_payment_charge_id: typing.Optional[str] = Field(default=None)


class ShippingQuery(BaseObject):
    id: typing.Optional[str] = Field(default=None)
    from_: typing.Optional["User"] = Field(default=None, alias="from")
    invoice_payload: typing.Optional[str] = Field(default=None)
    shipping_address: typing.Optional["ShippingAddress"] = Field(default=None)


class PreCheckoutQuery(BaseObject):
    id: typing.Optional[str] = Field(default=None)
    from_: typing.Optional["User"] = Field(default=None, alias="from")
    currency: typing.Optional[str] = Field(default=None)
    total_amount: typing.Optional[int] = Field(default=None)
    invoice_payload: typing.Optional[str] = Field(default=None)
    shipping_option_id: typing.Optional[str] = Field(default=None)
    order_info: typing.Optional["OrderInfo"] = Field(default=None)


class PassportData(BaseObject):
    data: typing.Optional[typing.List["EncryptedPassportElement"]] = Field(default=None)
    credentials: typing.Optional["EncryptedCredentials"] = Field(default=None)


class PassportFile(BaseObject):
    file_id: typing.Optional[str] = Field(default=None)
    file_unique_id: typing.Optional[str] = Field(default=None)
    file_size: typing.Optional[int] = Field(default=None)
    file_date: typing.Optional[int] = Field(default=None)


class EncryptedPassportElement(BaseObject):
    type: typing.Optional[str] = Field(default=None)
    data: typing.Optional[str] = Field(default=None)
    phone_number: typing.Optional[str] = Field(default=None)
    email: typing.Optional[str] = Field(default=None)
    files: typing.Optional[typing.List["PassportFile"]] = Field(default=None)
    front_side: typing.Optional["PassportFile"] = Field(default=None)
    reverse_side: typing.Optional["PassportFile"] = Field(default=None)
    selfie: typing.Optional["PassportFile"] = Field(default=None)
    translation: typing.Optional[typing.List["PassportFile"]] = Field(default=None)
    hash: typing.Optional[str] = Field(default=None)


class EncryptedCredentials(BaseObject):
    data: typing.Optional[str] = Field(default=None)
    hash: typing.Optional[str] = Field(default=None)
    secret: typing.Optional[str] = Field(default=None)


class PassportElementError(BaseObject):
    pass


class PassportElementErrorDataField(BaseObject):
    source: typing.Optional[str] = Field(default=None)
    type: typing.Optional[str] = Field(default=None)
    field_name: typing.Optional[str] = Field(default=None)
    data_hash: typing.Optional[str] = Field(default=None)
    message: typing.Optional[str] = Field(default=None)


class PassportElementErrorFrontSide(BaseObject):
    source: typing.Optional[str] = Field(default=None)
    type: typing.Optional[str] = Field(default=None)
    file_hash: typing.Optional[str] = Field(default=None)
    message: typing.Optional[str] = Field(default=None)


class PassportElementErrorReverseSide(BaseObject):
    source: typing.Optional[str] = Field(default=None)
    type: typing.Optional[str] = Field(default=None)
    file_hash: typing.Optional[str] = Field(default=None)
    message: typing.Optional[str] = Field(default=None)


class PassportElementErrorSelfie(BaseObject):
    source: typing.Optional[str] = Field(default=None)
    type: typing.Optional[str] = Field(default=None)
    file_hash: typing.Optional[str] = Field(default=None)
    message: typing.Optional[str] = Field(default=None)


class PassportElementErrorFile(BaseObject):
    source: typing.Optional[str] = Field(default=None)
    type: typing.Optional[str] = Field(default=None)
    file_hash: typing.Optional[str] = Field(default=None)
    message: typing.Optional[str] = Field(default=None)


class PassportElementErrorFiles(BaseObject):
    source: typing.Optional[str] = Field(default=None)
    type: typing.Optional[str] = Field(default=None)
    file_hashes: typing.Optional[typing.List[str]] = Field(default=None)
    message: typing.Optional[str] = Field(default=None)


class PassportElementErrorTranslationFile(BaseObject):
    source: typing.Optional[str] = Field(default=None)
    type: typing.Optional[str] = Field(default=None)
    file_hash: typing.Optional[str] = Field(default=None)
    message: typing.Optional[str] = Field(default=None)


class PassportElementErrorTranslationFiles(BaseObject):
    source: typing.Optional[str] = Field(default=None)
    type: typing.Optional[str] = Field(default=None)
    file_hashes: typing.Optional[typing.List[str]] = Field(default=None)
    message: typing.Optional[str] = Field(default=None)


class PassportElementErrorUnspecified(BaseObject):
    source: typing.Optional[str] = Field(default=None)
    type: typing.Optional[str] = Field(default=None)
    element_hash: typing.Optional[str] = Field(default=None)
    message: typing.Optional[str] = Field(default=None)


class Game(BaseObject):
    title: typing.Optional[str] = Field(default=None)
    description: typing.Optional[str] = Field(default=None)
    photo: typing.Optional[typing.List["PhotoSize"]] = Field(default=None)
    text: typing.Optional[str] = Field(default=None)
    text_entities: typing.Optional[typing.List["MessageEntity"]] = Field(default=None)
    animation: typing.Optional["Animation"] = Field(default=None)


class CallbackGame(BaseObject):
    pass


class GameHighScore(BaseObject):
    position: typing.Optional[int] = Field(default=None)
    user: typing.Optional["User"] = Field(default=None)
    score: typing.Optional[int] = Field(default=None)


for v in locals().copy().values():
    if inspect.isclass(v) and issubclass(v, BaseObject):
        v.update_forward_refs()

__all__ = (
    "Error",
    "Update",
    "WebhookInfo",
    "User",
    "Chat",
    "Message",
    "MessageId",
    "MessageEntity",
    "PhotoSize",
    "Animation",
    "Audio",
    "Document",
    "Video",
    "VideoNote",
    "Voice",
    "Contact",
    "Dice",
    "PollOption",
    "PollAnswer",
    "Poll",
    "Location",
    "Venue",
    "WebAppData",
    "ProximityAlertTriggered",
    "MessageAutoDeleteTimerChanged",
    "VideoChatScheduled",
    "VideoChatStarted",
    "VideoChatEnded",
    "VideoChatParticipantsInvited",
    "UserProfilePhotos",
    "File",
    "WebAppInfo",
    "ReplyKeyboardMarkup",
    "KeyboardButton",
    "KeyboardButtonPollType",
    "ReplyKeyboardRemove",
    "InlineKeyboardMarkup",
    "InlineKeyboardButton",
    "LoginUrl",
    "CallbackQuery",
    "ForceReply",
    "ChatPhoto",
    "ChatInviteLink",
    "ChatAdministratorRights",
    "ChatMember",
    "ChatMemberOwner",
    "ChatMemberAdministrator",
    "ChatMemberMember",
    "ChatMemberRestricted",
    "ChatMemberLeft",
    "ChatMemberBanned",
    "ChatMemberUpdated",
    "ChatJoinRequest",
    "ChatPermissions",
    "ChatLocation",
    "BotCommand",
    "BotCommandScope",
    "BotCommandScopeDefault",
    "BotCommandScopeAllPrivateChats",
    "BotCommandScopeAllGroupChats",
    "BotCommandScopeAllChatAdministrators",
    "BotCommandScopeChat",
    "BotCommandScopeChatAdministrators",
    "BotCommandScopeChatMember",
    "MenuButton",
    "MenuButtonCommands",
    "MenuButtonWebApp",
    "MenuButtonDefault",
    "ResponseParameters",
    "InputMedia",
    "InputMediaPhoto",
    "InputMediaVideo",
    "InputMediaAnimation",
    "InputMediaAudio",
    "InputMediaDocument",
    "InputFile",
    "Sticker",
    "StickerSet",
    "MaskPosition",
    "InlineQuery",
    "InlineQueryResult",
    "InlineQueryResultArticle",
    "InlineQueryResultPhoto",
    "InlineQueryResultGif",
    "InlineQueryResultMpeg4Gif",
    "InlineQueryResultVideo",
    "InlineQueryResultAudio",
    "InlineQueryResultVoice",
    "InlineQueryResultDocument",
    "InlineQueryResultLocation",
    "InlineQueryResultVenue",
    "InlineQueryResultContact",
    "InlineQueryResultGame",
    "InlineQueryResultCachedPhoto",
    "InlineQueryResultCachedGif",
    "InlineQueryResultCachedMpeg4Gif",
    "InlineQueryResultCachedSticker",
    "InlineQueryResultCachedDocument",
    "InlineQueryResultCachedVideo",
    "InlineQueryResultCachedVoice",
    "InlineQueryResultCachedAudio",
    "InputMessageContent",
    "InputTextMessageContent",
    "InputLocationMessageContent",
    "InputVenueMessageContent",
    "InputContactMessageContent",
    "InputInvoiceMessageContent",
    "ChosenInlineResult",
    "SentWebAppMessage",
    "LabeledPrice",
    "Invoice",
    "ShippingAddress",
    "OrderInfo",
    "ShippingOption",
    "SuccessfulPayment",
    "ShippingQuery",
    "PreCheckoutQuery",
    "PassportData",
    "PassportFile",
    "EncryptedPassportElement",
    "EncryptedCredentials",
    "PassportElementError",
    "PassportElementErrorDataField",
    "PassportElementErrorFrontSide",
    "PassportElementErrorReverseSide",
    "PassportElementErrorSelfie",
    "PassportElementErrorFile",
    "PassportElementErrorFiles",
    "PassportElementErrorTranslationFile",
    "PassportElementErrorTranslationFiles",
    "PassportElementErrorUnspecified",
    "Game",
    "CallbackGame",
    "GameHighScore",
)
