import typing
import inspect
from pydantic import BaseModel, Field


class Error(BaseModel):
    ok: typing.Optional[bool] = Field(default=None)
    error_code: typing.Optional[int] = Field(default=None)
    description: typing.Optional[str] = Field(default=None)
    parameters: typing.Optional["ResponseParameters"] = Field(default=None)


class Update(BaseModel):
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


class WebhookInfo(BaseModel):
    url: typing.Optional[str] = Field(default=None)
    has_custom_certificate: typing.Optional[bool] = Field(default=None)
    pending_update_count: typing.Optional[int] = Field(default=None)
    ip_address: typing.Optional[str] = Field(default=None)
    last_error_date: typing.Optional[int] = Field(default=None)
    last_error_message: typing.Optional[str] = Field(default=None)
    last_synchronization_error_date: typing.Optional[int] = Field(default=None)
    max_connections: typing.Optional[int] = Field(default=None)
    allowed_updates: typing.Optional[typing.List[str]] = Field(default=None)


class User(BaseModel):
    id: typing.Optional[int] = Field(default=None)
    is_bot: typing.Optional[bool] = Field(default=None)
    first_name: typing.Optional[str] = Field(default=None)
    last_name: typing.Optional[str] = Field(default=None)
    username: typing.Optional[str] = Field(default=None)
    language_code: typing.Optional[str] = Field(default=None)
    can_join_groups: typing.Optional[bool] = Field(default=None)
    can_read_all_group_messages: typing.Optional[bool] = Field(default=None)
    supports_inline_queries: typing.Optional[bool] = Field(default=None)


class Chat(BaseModel):
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


class Message(BaseModel):
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


class MessageId(BaseModel):
    message_id: typing.Optional[int] = Field(default=None)


class MessageEntity(BaseModel):
    type: typing.Optional[str] = Field(default=None)
    offset: typing.Optional[int] = Field(default=None)
    length: typing.Optional[int] = Field(default=None)
    url: typing.Optional[str] = Field(default=None)
    user: typing.Optional["User"] = Field(default=None)
    language: typing.Optional[str] = Field(default=None)


class PhotoSize(BaseModel):
    file_id: typing.Optional[str] = Field(default=None)
    file_unique_id: typing.Optional[str] = Field(default=None)
    width: typing.Optional[int] = Field(default=None)
    height: typing.Optional[int] = Field(default=None)
    file_size: typing.Optional[int] = Field(default=None)


class Animation(BaseModel):
    file_id: typing.Optional[str] = Field(default=None)
    file_unique_id: typing.Optional[str] = Field(default=None)
    width: typing.Optional[int] = Field(default=None)
    height: typing.Optional[int] = Field(default=None)
    duration: typing.Optional[int] = Field(default=None)
    thumb: typing.Optional["PhotoSize"] = Field(default=None)
    file_name: typing.Optional[str] = Field(default=None)
    mime_type: typing.Optional[str] = Field(default=None)
    file_size: typing.Optional[int] = Field(default=None)


class Audio(BaseModel):
    file_id: typing.Optional[str] = Field(default=None)
    file_unique_id: typing.Optional[str] = Field(default=None)
    duration: typing.Optional[int] = Field(default=None)
    performer: typing.Optional[str] = Field(default=None)
    title: typing.Optional[str] = Field(default=None)
    file_name: typing.Optional[str] = Field(default=None)
    mime_type: typing.Optional[str] = Field(default=None)
    file_size: typing.Optional[int] = Field(default=None)
    thumb: typing.Optional["PhotoSize"] = Field(default=None)


class Document(BaseModel):
    file_id: typing.Optional[str] = Field(default=None)
    file_unique_id: typing.Optional[str] = Field(default=None)
    thumb: typing.Optional["PhotoSize"] = Field(default=None)
    file_name: typing.Optional[str] = Field(default=None)
    mime_type: typing.Optional[str] = Field(default=None)
    file_size: typing.Optional[int] = Field(default=None)


class Video(BaseModel):
    file_id: typing.Optional[str] = Field(default=None)
    file_unique_id: typing.Optional[str] = Field(default=None)
    width: typing.Optional[int] = Field(default=None)
    height: typing.Optional[int] = Field(default=None)
    duration: typing.Optional[int] = Field(default=None)
    thumb: typing.Optional["PhotoSize"] = Field(default=None)
    file_name: typing.Optional[str] = Field(default=None)
    mime_type: typing.Optional[str] = Field(default=None)
    file_size: typing.Optional[int] = Field(default=None)


class VideoNote(BaseModel):
    file_id: typing.Optional[str] = Field(default=None)
    file_unique_id: typing.Optional[str] = Field(default=None)
    length: typing.Optional[int] = Field(default=None)
    duration: typing.Optional[int] = Field(default=None)
    thumb: typing.Optional["PhotoSize"] = Field(default=None)
    file_size: typing.Optional[int] = Field(default=None)


class Voice(BaseModel):
    file_id: typing.Optional[str] = Field(default=None)
    file_unique_id: typing.Optional[str] = Field(default=None)
    duration: typing.Optional[int] = Field(default=None)
    mime_type: typing.Optional[str] = Field(default=None)
    file_size: typing.Optional[int] = Field(default=None)


class Contact(BaseModel):
    phone_number: typing.Optional[str] = Field(default=None)
    first_name: typing.Optional[str] = Field(default=None)
    last_name: typing.Optional[str] = Field(default=None)
    user_id: typing.Optional[int] = Field(default=None)
    vcard: typing.Optional[str] = Field(default=None)


class Dice(BaseModel):
    emoji: typing.Optional[str] = Field(default=None)
    value: typing.Optional[int] = Field(default=None)


class PollOption(BaseModel):
    text: typing.Optional[str] = Field(default=None)
    voter_count: typing.Optional[int] = Field(default=None)


class PollAnswer(BaseModel):
    poll_id: typing.Optional[str] = Field(default=None)
    user: typing.Optional["User"] = Field(default=None)
    option_ids: typing.Optional[typing.List[int]] = Field(default=None)


class Poll(BaseModel):
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


class Location(BaseModel):
    longitude: typing.Optional[float] = Field(default=None)
    latitude: typing.Optional[float] = Field(default=None)
    horizontal_accuracy: typing.Optional[float] = Field(default=None)
    live_period: typing.Optional[int] = Field(default=None)
    heading: typing.Optional[int] = Field(default=None)
    proximity_alert_radius: typing.Optional[int] = Field(default=None)


class Venue(BaseModel):
    location: typing.Optional["Location"] = Field(default=None)
    title: typing.Optional[str] = Field(default=None)
    address: typing.Optional[str] = Field(default=None)
    foursquare_id: typing.Optional[str] = Field(default=None)
    foursquare_type: typing.Optional[str] = Field(default=None)
    google_place_id: typing.Optional[str] = Field(default=None)
    google_place_type: typing.Optional[str] = Field(default=None)


class WebAppData(BaseModel):
    data: typing.Optional[str] = Field(default=None)
    button_text: typing.Optional[str] = Field(default=None)


class ProximityAlertTriggered(BaseModel):
    traveler: typing.Optional["User"] = Field(default=None)
    watcher: typing.Optional["User"] = Field(default=None)
    distance: typing.Optional[int] = Field(default=None)


class MessageAutoDeleteTimerChanged(BaseModel):
    message_auto_delete_time: typing.Optional[int] = Field(default=None)


class VideoChatScheduled(BaseModel):
    start_date: typing.Optional[int] = Field(default=None)


class VideoChatStarted(BaseModel):
    pass


class VideoChatEnded(BaseModel):
    duration: typing.Optional[int] = Field(default=None)


class VideoChatParticipantsInvited(BaseModel):
    users: typing.Optional[typing.List["User"]] = Field(default=None)


class UserProfilePhotos(BaseModel):
    total_count: typing.Optional[int] = Field(default=None)
    photos: typing.Optional[typing.List[typing.List["PhotoSize"]]] = Field(default=None)


class File(BaseModel):
    file_id: typing.Optional[str] = Field(default=None)
    file_unique_id: typing.Optional[str] = Field(default=None)
    file_size: typing.Optional[int] = Field(default=None)
    file_path: typing.Optional[str] = Field(default=None)


class WebAppInfo(BaseModel):
    url: typing.Optional[str] = Field(default=None)


class ReplyKeyboardMarkup(BaseModel):
    keyboard: typing.Optional[typing.List[typing.List["KeyboardButton"]]] = Field(
        default=None
    )
    resize_keyboard: typing.Optional[bool] = Field(default=None)
    one_time_keyboard: typing.Optional[bool] = Field(default=None)
    input_field_placeholder: typing.Optional[str] = Field(default=None)
    selective: typing.Optional[bool] = Field(default=None)


class KeyboardButton(BaseModel):
    text: typing.Optional[str] = Field(default=None)
    request_contact: typing.Optional[bool] = Field(default=None)
    request_location: typing.Optional[bool] = Field(default=None)
    request_poll: typing.Optional["KeyboardButtonPollType"] = Field(default=None)
    web_app: typing.Optional["WebAppInfo"] = Field(default=None)


class KeyboardButtonPollType(BaseModel):
    type: typing.Optional[str] = Field(default=None)


class ReplyKeyboardRemove(BaseModel):
    remove_keyboard: typing.Optional[bool] = Field(default=None)
    selective: typing.Optional[bool] = Field(default=None)


class InlineKeyboardMarkup(BaseModel):
    inline_keyboard: typing.Optional[
        typing.List[typing.List["InlineKeyboardButton"]]
    ] = Field(default=None)


class InlineKeyboardButton(BaseModel):
    text: typing.Optional[str] = Field(default=None)
    url: typing.Optional[str] = Field(default=None)
    callback_data: typing.Optional[str] = Field(default=None)
    web_app: typing.Optional["WebAppInfo"] = Field(default=None)
    login_url: typing.Optional["LoginUrl"] = Field(default=None)
    switch_inline_query: typing.Optional[str] = Field(default=None)
    switch_inline_query_current_chat: typing.Optional[str] = Field(default=None)
    callback_game: typing.Optional["CallbackGame"] = Field(default=None)
    pay: typing.Optional[bool] = Field(default=None)


class LoginUrl(BaseModel):
    url: typing.Optional[str] = Field(default=None)
    forward_text: typing.Optional[str] = Field(default=None)
    bot_username: typing.Optional[str] = Field(default=None)
    request_write_access: typing.Optional[bool] = Field(default=None)


class CallbackQuery(BaseModel):
    id: typing.Optional[str] = Field(default=None)
    from_: typing.Optional["User"] = Field(default=None, alias="from")
    message: typing.Optional["Message"] = Field(default=None)
    inline_message_id: typing.Optional[str] = Field(default=None)
    chat_instance: typing.Optional[str] = Field(default=None)
    data: typing.Optional[str] = Field(default=None)
    game_short_name: typing.Optional[str] = Field(default=None)


class ForceReply(BaseModel):
    force_reply: typing.Optional[bool] = Field(default=None)
    input_field_placeholder: typing.Optional[str] = Field(default=None)
    selective: typing.Optional[bool] = Field(default=None)


class ChatPhoto(BaseModel):
    small_file_id: typing.Optional[str] = Field(default=None)
    small_file_unique_id: typing.Optional[str] = Field(default=None)
    big_file_id: typing.Optional[str] = Field(default=None)
    big_file_unique_id: typing.Optional[str] = Field(default=None)


class ChatInviteLink(BaseModel):
    invite_link: typing.Optional[str] = Field(default=None)
    creator: typing.Optional["User"] = Field(default=None)
    creates_join_request: typing.Optional[bool] = Field(default=None)
    is_primary: typing.Optional[bool] = Field(default=None)
    is_revoked: typing.Optional[bool] = Field(default=None)
    name: typing.Optional[str] = Field(default=None)
    expire_date: typing.Optional[int] = Field(default=None)
    member_limit: typing.Optional[int] = Field(default=None)
    pending_join_request_count: typing.Optional[int] = Field(default=None)


class ChatAdministratorRights(BaseModel):
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


class ChatMember(BaseModel):
    pass


class ChatMemberOwner(BaseModel):
    status: typing.Optional[str] = Field(default=None)
    user: typing.Optional["User"] = Field(default=None)
    is_anonymous: typing.Optional[bool] = Field(default=None)
    custom_title: typing.Optional[str] = Field(default=None)


class ChatMemberAdministrator(BaseModel):
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


class ChatMemberMember(BaseModel):
    status: typing.Optional[str] = Field(default=None)
    user: typing.Optional["User"] = Field(default=None)


class ChatMemberRestricted(BaseModel):
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


class ChatMemberLeft(BaseModel):
    status: typing.Optional[str] = Field(default=None)
    user: typing.Optional["User"] = Field(default=None)


class ChatMemberBanned(BaseModel):
    status: typing.Optional[str] = Field(default=None)
    user: typing.Optional["User"] = Field(default=None)
    until_date: typing.Optional[int] = Field(default=None)


class ChatMemberUpdated(BaseModel):
    chat: typing.Optional["Chat"] = Field(default=None)
    from_: typing.Optional["User"] = Field(default=None, alias="from")
    date: typing.Optional[int] = Field(default=None)
    old_chat_member: typing.Optional["ChatMember"] = Field(default=None)
    new_chat_member: typing.Optional["ChatMember"] = Field(default=None)
    invite_link: typing.Optional["ChatInviteLink"] = Field(default=None)


class ChatJoinRequest(BaseModel):
    chat: typing.Optional["Chat"] = Field(default=None)
    from_: typing.Optional["User"] = Field(default=None, alias="from")
    date: typing.Optional[int] = Field(default=None)
    bio: typing.Optional[str] = Field(default=None)
    invite_link: typing.Optional["ChatInviteLink"] = Field(default=None)


class ChatPermissions(BaseModel):
    can_send_messages: typing.Optional[bool] = Field(default=None)
    can_send_media_messages: typing.Optional[bool] = Field(default=None)
    can_send_polls: typing.Optional[bool] = Field(default=None)
    can_send_other_messages: typing.Optional[bool] = Field(default=None)
    can_add_web_page_previews: typing.Optional[bool] = Field(default=None)
    can_change_info: typing.Optional[bool] = Field(default=None)
    can_invite_users: typing.Optional[bool] = Field(default=None)
    can_pin_messages: typing.Optional[bool] = Field(default=None)


class ChatLocation(BaseModel):
    location: typing.Optional["Location"] = Field(default=None)
    address: typing.Optional[str] = Field(default=None)


class BotCommand(BaseModel):
    command: typing.Optional[str] = Field(default=None)
    description: typing.Optional[str] = Field(default=None)


class BotCommandScope(BaseModel):
    pass


class BotCommandScopeDefault(BaseModel):
    type: typing.Optional[str] = Field(default=None)


class BotCommandScopeAllPrivateChats(BaseModel):
    type: typing.Optional[str] = Field(default=None)


class BotCommandScopeAllGroupChats(BaseModel):
    type: typing.Optional[str] = Field(default=None)


class BotCommandScopeAllChatAdministrators(BaseModel):
    type: typing.Optional[str] = Field(default=None)


class BotCommandScopeChat(BaseModel):
    type: typing.Optional[str] = Field(default=None)
    chat_id: typing.Optional[typing.Union[int, str]] = Field(default=None)


class BotCommandScopeChatAdministrators(BaseModel):
    type: typing.Optional[str] = Field(default=None)
    chat_id: typing.Optional[typing.Union[int, str]] = Field(default=None)


class BotCommandScopeChatMember(BaseModel):
    type: typing.Optional[str] = Field(default=None)
    chat_id: typing.Optional[typing.Union[int, str]] = Field(default=None)
    user_id: typing.Optional[int] = Field(default=None)


class MenuButton(BaseModel):
    pass


class MenuButtonCommands(BaseModel):
    type: typing.Optional[str] = Field(default=None)


class MenuButtonWebApp(BaseModel):
    type: typing.Optional[str] = Field(default=None)
    text: typing.Optional[str] = Field(default=None)
    web_app: typing.Optional["WebAppInfo"] = Field(default=None)


class MenuButtonDefault(BaseModel):
    type: typing.Optional[str] = Field(default=None)


class ResponseParameters(BaseModel):
    migrate_to_chat_id: typing.Optional[int] = Field(default=None)
    retry_after: typing.Optional[int] = Field(default=None)


class InputMedia(BaseModel):
    pass


class InputMediaPhoto(BaseModel):
    type: typing.Optional[str] = Field(default=None)
    media: typing.Optional[str] = Field(default=None)
    caption: typing.Optional[str] = Field(default=None)
    parse_mode: typing.Optional[str] = Field(default=None)
    caption_entities: typing.Optional[typing.List["MessageEntity"]] = Field(
        default=None
    )


class InputMediaVideo(BaseModel):
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


class InputMediaAnimation(BaseModel):
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


class InputMediaAudio(BaseModel):
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


class InputMediaDocument(BaseModel):
    type: typing.Optional[str] = Field(default=None)
    media: typing.Optional[str] = Field(default=None)
    thumb: typing.Optional[typing.Union["InputFile", str]] = Field(default=None)
    caption: typing.Optional[str] = Field(default=None)
    parse_mode: typing.Optional[str] = Field(default=None)
    caption_entities: typing.Optional[typing.List["MessageEntity"]] = Field(
        default=None
    )
    disable_content_type_detection: typing.Optional[bool] = Field(default=None)


class InputFile(BaseModel):
    pass


class Sticker(BaseModel):
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


class StickerSet(BaseModel):
    name: typing.Optional[str] = Field(default=None)
    title: typing.Optional[str] = Field(default=None)
    is_animated: typing.Optional[bool] = Field(default=None)
    is_video: typing.Optional[bool] = Field(default=None)
    contains_masks: typing.Optional[bool] = Field(default=None)
    stickers: typing.Optional[typing.List["Sticker"]] = Field(default=None)
    thumb: typing.Optional["PhotoSize"] = Field(default=None)


class MaskPosition(BaseModel):
    point: typing.Optional[str] = Field(default=None)
    x_shift: typing.Optional[float] = Field(default=None)
    y_shift: typing.Optional[float] = Field(default=None)
    scale: typing.Optional[float] = Field(default=None)


class InlineQuery(BaseModel):
    id: typing.Optional[str] = Field(default=None)
    from_: typing.Optional["User"] = Field(default=None, alias="from")
    query: typing.Optional[str] = Field(default=None)
    offset: typing.Optional[str] = Field(default=None)
    chat_type: typing.Optional[str] = Field(default=None)
    location: typing.Optional["Location"] = Field(default=None)


class InlineQueryResult(BaseModel):
    pass


class InlineQueryResultArticle(BaseModel):
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


class InlineQueryResultPhoto(BaseModel):
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


class InlineQueryResultGif(BaseModel):
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


class InlineQueryResultMpeg4Gif(BaseModel):
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


class InlineQueryResultVideo(BaseModel):
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


class InlineQueryResultAudio(BaseModel):
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


class InlineQueryResultVoice(BaseModel):
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


class InlineQueryResultDocument(BaseModel):
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


class InlineQueryResultLocation(BaseModel):
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


class InlineQueryResultVenue(BaseModel):
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


class InlineQueryResultContact(BaseModel):
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


class InlineQueryResultGame(BaseModel):
    type: typing.Optional[str] = Field(default=None)
    id: typing.Optional[str] = Field(default=None)
    game_short_name: typing.Optional[str] = Field(default=None)
    reply_markup: typing.Optional["InlineKeyboardMarkup"] = Field(default=None)


class InlineQueryResultCachedPhoto(BaseModel):
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


class InlineQueryResultCachedGif(BaseModel):
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


class InlineQueryResultCachedMpeg4Gif(BaseModel):
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


class InlineQueryResultCachedSticker(BaseModel):
    type: typing.Optional[str] = Field(default=None)
    id: typing.Optional[str] = Field(default=None)
    sticker_file_id: typing.Optional[str] = Field(default=None)
    reply_markup: typing.Optional["InlineKeyboardMarkup"] = Field(default=None)
    input_message_content: typing.Optional["InputMessageContent"] = Field(default=None)


class InlineQueryResultCachedDocument(BaseModel):
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


class InlineQueryResultCachedVideo(BaseModel):
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


class InlineQueryResultCachedVoice(BaseModel):
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


class InlineQueryResultCachedAudio(BaseModel):
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


class InputMessageContent(BaseModel):
    pass


class InputTextMessageContent(BaseModel):
    message_text: typing.Optional[str] = Field(default=None)
    parse_mode: typing.Optional[str] = Field(default=None)
    entities: typing.Optional[typing.List["MessageEntity"]] = Field(default=None)
    disable_web_page_preview: typing.Optional[bool] = Field(default=None)


class InputLocationMessageContent(BaseModel):
    latitude: typing.Optional[float] = Field(default=None)
    longitude: typing.Optional[float] = Field(default=None)
    horizontal_accuracy: typing.Optional[float] = Field(default=None)
    live_period: typing.Optional[int] = Field(default=None)
    heading: typing.Optional[int] = Field(default=None)
    proximity_alert_radius: typing.Optional[int] = Field(default=None)


class InputVenueMessageContent(BaseModel):
    latitude: typing.Optional[float] = Field(default=None)
    longitude: typing.Optional[float] = Field(default=None)
    title: typing.Optional[str] = Field(default=None)
    address: typing.Optional[str] = Field(default=None)
    foursquare_id: typing.Optional[str] = Field(default=None)
    foursquare_type: typing.Optional[str] = Field(default=None)
    google_place_id: typing.Optional[str] = Field(default=None)
    google_place_type: typing.Optional[str] = Field(default=None)


class InputContactMessageContent(BaseModel):
    phone_number: typing.Optional[str] = Field(default=None)
    first_name: typing.Optional[str] = Field(default=None)
    last_name: typing.Optional[str] = Field(default=None)
    vcard: typing.Optional[str] = Field(default=None)


class InputInvoiceMessageContent(BaseModel):
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


class ChosenInlineResult(BaseModel):
    result_id: typing.Optional[str] = Field(default=None)
    from_: typing.Optional["User"] = Field(default=None, alias="from")
    location: typing.Optional["Location"] = Field(default=None)
    inline_message_id: typing.Optional[str] = Field(default=None)
    query: typing.Optional[str] = Field(default=None)


class SentWebAppMessage(BaseModel):
    inline_message_id: typing.Optional[str] = Field(default=None)


class LabeledPrice(BaseModel):
    label: typing.Optional[str] = Field(default=None)
    amount: typing.Optional[int] = Field(default=None)


class Invoice(BaseModel):
    title: typing.Optional[str] = Field(default=None)
    description: typing.Optional[str] = Field(default=None)
    start_parameter: typing.Optional[str] = Field(default=None)
    currency: typing.Optional[str] = Field(default=None)
    total_amount: typing.Optional[int] = Field(default=None)


class ShippingAddress(BaseModel):
    country_code: typing.Optional[str] = Field(default=None)
    state: typing.Optional[str] = Field(default=None)
    city: typing.Optional[str] = Field(default=None)
    street_line1: typing.Optional[str] = Field(default=None)
    street_line2: typing.Optional[str] = Field(default=None)
    post_code: typing.Optional[str] = Field(default=None)


class OrderInfo(BaseModel):
    name: typing.Optional[str] = Field(default=None)
    phone_number: typing.Optional[str] = Field(default=None)
    email: typing.Optional[str] = Field(default=None)
    shipping_address: typing.Optional["ShippingAddress"] = Field(default=None)


class ShippingOption(BaseModel):
    id: typing.Optional[str] = Field(default=None)
    title: typing.Optional[str] = Field(default=None)
    prices: typing.Optional[typing.List["LabeledPrice"]] = Field(default=None)


class SuccessfulPayment(BaseModel):
    currency: typing.Optional[str] = Field(default=None)
    total_amount: typing.Optional[int] = Field(default=None)
    invoice_payload: typing.Optional[str] = Field(default=None)
    shipping_option_id: typing.Optional[str] = Field(default=None)
    order_info: typing.Optional["OrderInfo"] = Field(default=None)
    telegram_payment_charge_id: typing.Optional[str] = Field(default=None)
    provider_payment_charge_id: typing.Optional[str] = Field(default=None)


class ShippingQuery(BaseModel):
    id: typing.Optional[str] = Field(default=None)
    from_: typing.Optional["User"] = Field(default=None, alias="from")
    invoice_payload: typing.Optional[str] = Field(default=None)
    shipping_address: typing.Optional["ShippingAddress"] = Field(default=None)


class PreCheckoutQuery(BaseModel):
    id: typing.Optional[str] = Field(default=None)
    from_: typing.Optional["User"] = Field(default=None, alias="from")
    currency: typing.Optional[str] = Field(default=None)
    total_amount: typing.Optional[int] = Field(default=None)
    invoice_payload: typing.Optional[str] = Field(default=None)
    shipping_option_id: typing.Optional[str] = Field(default=None)
    order_info: typing.Optional["OrderInfo"] = Field(default=None)


class PassportData(BaseModel):
    data: typing.Optional[typing.List["EncryptedPassportElement"]] = Field(default=None)
    credentials: typing.Optional["EncryptedCredentials"] = Field(default=None)


class PassportFile(BaseModel):
    file_id: typing.Optional[str] = Field(default=None)
    file_unique_id: typing.Optional[str] = Field(default=None)
    file_size: typing.Optional[int] = Field(default=None)
    file_date: typing.Optional[int] = Field(default=None)


class EncryptedPassportElement(BaseModel):
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


class EncryptedCredentials(BaseModel):
    data: typing.Optional[str] = Field(default=None)
    hash: typing.Optional[str] = Field(default=None)
    secret: typing.Optional[str] = Field(default=None)


class PassportElementError(BaseModel):
    pass


class PassportElementErrorDataField(BaseModel):
    source: typing.Optional[str] = Field(default=None)
    type: typing.Optional[str] = Field(default=None)
    field_name: typing.Optional[str] = Field(default=None)
    data_hash: typing.Optional[str] = Field(default=None)
    message: typing.Optional[str] = Field(default=None)


class PassportElementErrorFrontSide(BaseModel):
    source: typing.Optional[str] = Field(default=None)
    type: typing.Optional[str] = Field(default=None)
    file_hash: typing.Optional[str] = Field(default=None)
    message: typing.Optional[str] = Field(default=None)


class PassportElementErrorReverseSide(BaseModel):
    source: typing.Optional[str] = Field(default=None)
    type: typing.Optional[str] = Field(default=None)
    file_hash: typing.Optional[str] = Field(default=None)
    message: typing.Optional[str] = Field(default=None)


class PassportElementErrorSelfie(BaseModel):
    source: typing.Optional[str] = Field(default=None)
    type: typing.Optional[str] = Field(default=None)
    file_hash: typing.Optional[str] = Field(default=None)
    message: typing.Optional[str] = Field(default=None)


class PassportElementErrorFile(BaseModel):
    source: typing.Optional[str] = Field(default=None)
    type: typing.Optional[str] = Field(default=None)
    file_hash: typing.Optional[str] = Field(default=None)
    message: typing.Optional[str] = Field(default=None)


class PassportElementErrorFiles(BaseModel):
    source: typing.Optional[str] = Field(default=None)
    type: typing.Optional[str] = Field(default=None)
    file_hashes: typing.Optional[typing.List[str]] = Field(default=None)
    message: typing.Optional[str] = Field(default=None)


class PassportElementErrorTranslationFile(BaseModel):
    source: typing.Optional[str] = Field(default=None)
    type: typing.Optional[str] = Field(default=None)
    file_hash: typing.Optional[str] = Field(default=None)
    message: typing.Optional[str] = Field(default=None)


class PassportElementErrorTranslationFiles(BaseModel):
    source: typing.Optional[str] = Field(default=None)
    type: typing.Optional[str] = Field(default=None)
    file_hashes: typing.Optional[typing.List[str]] = Field(default=None)
    message: typing.Optional[str] = Field(default=None)


class PassportElementErrorUnspecified(BaseModel):
    source: typing.Optional[str] = Field(default=None)
    type: typing.Optional[str] = Field(default=None)
    element_hash: typing.Optional[str] = Field(default=None)
    message: typing.Optional[str] = Field(default=None)


class Game(BaseModel):
    title: typing.Optional[str] = Field(default=None)
    description: typing.Optional[str] = Field(default=None)
    photo: typing.Optional[typing.List["PhotoSize"]] = Field(default=None)
    text: typing.Optional[str] = Field(default=None)
    text_entities: typing.Optional[typing.List["MessageEntity"]] = Field(default=None)
    animation: typing.Optional["Animation"] = Field(default=None)


class CallbackGame(BaseModel):
    pass


class GameHighScore(BaseModel):
    position: typing.Optional[int] = Field(default=None)
    user: typing.Optional["User"] = Field(default=None)
    score: typing.Optional[int] = Field(default=None)


for v in locals().copy().values():
    if inspect.isclass(v) and issubclass(v, BaseModel):
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
