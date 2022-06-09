import typing
import inspect
from pydantic import BaseModel, Field


class Update(BaseModel):
    """
    This object represents an incoming update. At most one of the optional parameters
    can be present in any given update.
    :param update_id: The update's unique identifier. Update identifiers start from a certain positive
    number and increase sequentially. This ID becomes especially handy if you're using
    Webhooks, since it allows you to ignore repeated updates or to restore the correct
    update sequence, should they get out of order. If there are no new updates for at
    least a week, then identifier of the next update will be chosen randomly instead of
    sequentially.
    :param message: Optional. New incoming message of any kind — text, photo, sticker, etc.
    :param edited_message: Optional. New version of a message that is known to the bot and was edited
    :param channel_post: Optional. New incoming channel post of any kind — text, photo, sticker, etc.
    :param edited_channel_post: Optional. New version of a channel post that is known to the bot and was edited
    :param inline_query: Optional. New incoming inline query
    :param chosen_inline_result: Optional. The result of an inline query that was chosen by a user and sent to their
    chat partner. Please see our documentation on the feedback collecting for details on
    how to enable these updates for your bot.
    :param callback_query: Optional. New incoming callback query
    :param shipping_query: Optional. New incoming shipping query. Only for invoices with flexible price
    :param pre_checkout_query: Optional. New incoming pre-checkout query. Contains full information about checkout
    :param poll: Optional. New poll state. Bots receive only updates about stopped polls and polls,
    which are sent by the bot
    :param poll_answer: Optional. A user changed their answer in a non-anonymous poll. Bots receive new
    votes only in polls that were sent by the bot itself.
    :param my_chat_member: Optional. The bot's chat member status was updated in a chat. For private chats,
    this update is received only when the bot is blocked or unblocked by the user.
    :param chat_member: Optional. A chat member's status was updated in a chat. The bot must be an
    administrator in the chat and must explicitly specify “chat_member” in the list of
    allowed_updates to receive these updates.
    :param chat_join_request: Optional. A request to join the chat has been sent. The bot must have the
    can_invite_users administrator right in the chat to receive these updates.
    """

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
    """
    Contains information about the current status of a webhook.
    :param url: Webhook URL, may be empty if webhook is not set up
    :param has_custom_certificate: True, if a custom certificate was provided for webhook certificate checks
    :param pending_update_count: Number of updates awaiting delivery
    :param ip_address: Optional. Currently used webhook IP address
    :param last_error_date: Optional. Unix time for the most recent error that happened when trying to deliver
    an update via webhook
    :param last_error_message: Optional. Error message in human-readable format for the most recent error that
    happened when trying to deliver an update via webhook
    :param last_synchronization_error_date: Optional. Unix time of the most recent error that happened when trying to
    synchronize available updates with Telegram datacenters
    :param max_connections: Optional. Maximum allowed number of simultaneous HTTPS connections to the webhook
    for update delivery
    :param allowed_updates: Optional. A list of update types the bot is subscribed to. Defaults to all update
    types except chat_member
    """

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
    """
    This object represents a Telegram user or bot.
    :param id: Unique identifier for this user or bot. This number may have more than 32
    significant bits and some programming languages may have difficulty/silent defects
    in interpreting it. But it has at most 52 significant bits, so a 64-bit integer or
    double-precision float type are safe for storing this identifier.
    :param is_bot: True, if this user is a bot
    :param first_name: User's or bot's first name
    :param last_name: Optional. User's or bot's last name
    :param username: Optional. User's or bot's username
    :param language_code: Optional. IETF language tag of the user's language
    :param can_join_groups: Optional. True, if the bot can be invited to groups. Returned only in getMe.
    :param can_read_all_group_messages: Optional. True, if privacy mode is disabled for the bot. Returned only in getMe.
    :param supports_inline_queries: Optional. True, if the bot supports inline queries. Returned only in getMe.
    """

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
    """
    This object represents a chat.
    :param id: Unique identifier for this chat. This number may have more than 32 significant bits
    and some programming languages may have difficulty/silent defects in interpreting
    it. But it has at most 52 significant bits, so a signed 64-bit integer or double-
    precision float type are safe for storing this identifier.
    :param type: Type of chat, can be either “private”, “group”, “supergroup” or “channel”
    :param title: Optional. Title, for supergroups, channels and group chats
    :param username: Optional. Username, for private chats, supergroups and channels if available
    :param first_name: Optional. First name of the other party in a private chat
    :param last_name: Optional. Last name of the other party in a private chat
    :param photo: Optional. Chat photo. Returned only in getChat.
    :param bio: Optional. Bio of the other party in a private chat. Returned only in getChat.
    :param has_private_forwards: Optional. True, if privacy settings of the other party in the private chat allows to
    use tg://user?id=&lt;user_id&gt; links only in chats with the user. Returned only in
    getChat.
    :param description: Optional. Description, for groups, supergroups and channel chats. Returned only in
    getChat.
    :param invite_link: Optional. Primary invite link, for groups, supergroups and channel chats. Returned
    only in getChat.
    :param pinned_message: Optional. The most recent pinned message (by sending date). Returned only in
    getChat.
    :param permissions: Optional. Default chat member permissions, for groups and supergroups. Returned only
    in getChat.
    :param slow_mode_delay: Optional. For supergroups, the minimum allowed delay between consecutive messages
    sent by each unpriviledged user; in seconds. Returned only in getChat.
    :param message_auto_delete_time: Optional. The time after which all messages sent to the chat will be automatically
    deleted; in seconds. Returned only in getChat.
    :param has_protected_content: Optional. True, if messages from the chat can't be forwarded to other chats.
    Returned only in getChat.
    :param sticker_set_name: Optional. For supergroups, name of group sticker set. Returned only in getChat.
    :param can_set_sticker_set: Optional. True, if the bot can change the group sticker set. Returned only in
    getChat.
    :param linked_chat_id: Optional. Unique identifier for the linked chat, i.e. the discussion group
    identifier for a channel and vice versa; for supergroups and channel chats. This
    identifier may be greater than 32 bits and some programming languages may have
    difficulty/silent defects in interpreting it. But it is smaller than 52 bits, so a
    signed 64 bit integer or double-precision float type are safe for storing this
    identifier. Returned only in getChat.
    :param location: Optional. For supergroups, the location to which the supergroup is connected.
    Returned only in getChat.
    """

    id: typing.Optional[int] = Field(default=None)
    type: typing.Optional[
        typing.Literal["private", "group", "supergroup", "channel"]
    ] = Field(default=None)
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
    """
    This object represents a message.
    :param message_id: Unique message identifier inside this chat
    :param from: Optional. Sender of the message; empty for messages sent to channels. For backward
    compatibility, the field contains a fake sender user in non-channel chats, if the
    message was sent on behalf of a chat.
    :param sender_chat: Optional. Sender of the message, sent on behalf of a chat. For example, the channel
    itself for channel posts, the supergroup itself for messages from anonymous group
    administrators, the linked channel for messages automatically forwarded to the
    discussion group. For backward compatibility, the field from contains a fake sender
    user in non-channel chats, if the message was sent on behalf of a chat.
    :param date: Date the message was sent in Unix time
    :param chat: Conversation the message belongs to
    :param forward_from: Optional. For forwarded messages, sender of the original message
    :param forward_from_chat: Optional. For messages forwarded from channels or from anonymous administrators,
    information about the original sender chat
    :param forward_from_message_id: Optional. For messages forwarded from channels, identifier of the original message
    in the channel
    :param forward_signature: Optional. For forwarded messages that were originally sent in channels or by an
    anonymous chat administrator, signature of the message sender if present
    :param forward_sender_name: Optional. Sender's name for messages forwarded from users who disallow adding a link
    to their account in forwarded messages
    :param forward_date: Optional. For forwarded messages, date the original message was sent in Unix time
    :param is_automatic_forward: Optional. True, if the message is a channel post that was automatically forwarded to
    the connected discussion group
    :param reply_to_message: Optional. For replies, the original message. Note that the Message object in this
    field will not contain further reply_to_message fields even if it itself is a reply.
    :param via_bot: Optional. Bot through which the message was sent
    :param edit_date: Optional. Date the message was last edited in Unix time
    :param has_protected_content: Optional. True, if the message can't be forwarded
    :param media_group_id: Optional. The unique identifier of a media message group this message belongs to
    :param author_signature: Optional. Signature of the post author for messages in channels, or the custom title
    of an anonymous group administrator
    :param text: Optional. For text messages, the actual UTF-8 text of the message, 0-4096 characters
    :param entities: Optional. For text messages, special entities like usernames, URLs, bot commands,
    etc. that appear in the text
    :param animation: Optional. Message is an animation, information about the animation. For backward
    compatibility, when this field is set, the document field will also be set
    :param audio: Optional. Message is an audio file, information about the file
    :param document: Optional. Message is a general file, information about the file
    :param photo: Optional. Message is a photo, available sizes of the photo
    :param sticker: Optional. Message is a sticker, information about the sticker
    :param video: Optional. Message is a video, information about the video
    :param video_note: Optional. Message is a video note, information about the video message
    :param voice: Optional. Message is a voice message, information about the file
    :param caption: Optional. Caption for the animation, audio, document, photo, video or voice, 0-1024
    characters
    :param caption_entities: Optional. For messages with a caption, special entities like usernames, URLs, bot
    commands, etc. that appear in the caption
    :param contact: Optional. Message is a shared contact, information about the contact
    :param dice: Optional. Message is a dice with random value
    :param game: Optional. Message is a game, information about the game. More about games »
    :param poll: Optional. Message is a native poll, information about the poll
    :param venue: Optional. Message is a venue, information about the venue. For backward
    compatibility, when this field is set, the location field will also be set
    :param location: Optional. Message is a shared location, information about the location
    :param new_chat_members: Optional. New members that were added to the group or supergroup and information
    about them (the bot itself may be one of these members)
    :param left_chat_member: Optional. A member was removed from the group, information about them (this member
    may be the bot itself)
    :param new_chat_title: Optional. A chat title was changed to this value
    :param new_chat_photo: Optional. A chat photo was change to this value
    :param delete_chat_photo: Optional. Service message: the chat photo was deleted
    :param group_chat_created: Optional. Service message: the group has been created
    :param supergroup_chat_created: Optional. Service message: the supergroup has been created. This field can't be
    received in a message coming through updates, because bot can't be a member of a
    supergroup when it is created. It can only be found in reply_to_message if someone
    replies to a very first message in a directly created supergroup.
    :param channel_chat_created: Optional. Service message: the channel has been created. This field can't be
    received in a message coming through updates, because bot can't be a member of a
    channel when it is created. It can only be found in reply_to_message if someone
    replies to a very first message in a channel.
    :param message_auto_delete_timer_changed: Optional. Service message: auto-delete timer settings changed in the chat
    :param migrate_to_chat_id: Optional. The group has been migrated to a supergroup with the specified identifier.
    This number may have more than 32 significant bits and some programming languages
    may have difficulty/silent defects in interpreting it. But it has at most 52
    significant bits, so a signed 64-bit integer or double-precision float type are safe
    for storing this identifier.
    :param migrate_from_chat_id: Optional. The supergroup has been migrated from a group with the specified
    identifier. This number may have more than 32 significant bits and some programming
    languages may have difficulty/silent defects in interpreting it. But it has at most
    52 significant bits, so a signed 64-bit integer or double-precision float type are
    safe for storing this identifier.
    :param pinned_message: Optional. Specified message was pinned. Note that the Message object in this field
    will not contain further reply_to_message fields even if it is itself a reply.
    :param invoice: Optional. Message is an invoice for a payment, information about the invoice. More
    about payments »
    :param successful_payment: Optional. Message is a service message about a successful payment, information about
    the payment. More about payments »
    :param connected_website: Optional. The domain name of the website on which the user has logged in. More about
    Telegram Login »
    :param passport_data: Optional. Telegram Passport data
    :param proximity_alert_triggered: Optional. Service message. A user in the chat triggered another user's proximity
    alert while sharing Live Location.
    :param video_chat_scheduled: Optional. Service message: video chat scheduled
    :param video_chat_started: Optional. Service message: video chat started
    :param video_chat_ended: Optional. Service message: video chat ended
    :param video_chat_participants_invited: Optional. Service message: new participants invited to a video chat
    :param web_app_data: Optional. Service message: data sent by a Web App
    :param reply_markup: Optional. Inline keyboard attached to the message. login_url buttons are represented
    as ordinary url buttons.
    """

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
    """
    This object represents a unique message identifier.
    :param message_id: Unique message identifier
    """

    message_id: typing.Optional[int] = Field(default=None)


class MessageEntity(BaseModel):
    """
    This object represents one special entity in a text message. For example, hashtags,
    usernames, URLs, etc.
    :param type: Type of the entity. Currently, can be “mention” (@username), “hashtag” (#hashtag),
    “cashtag” ($USD), “bot_command” (/start@jobs_bot), “url” (https://telegram.org),
    “email” (do-not-reply@telegram.org), “phone_number” (+1-212-555-0123), “bold” (bold
    text), “italic” (italic text), “underline” (underlined text), “strikethrough”
    (strikethrough text), “spoiler” (spoiler message), “code” (monowidth string), “pre”
    (monowidth block), “text_link” (for clickable text URLs), “text_mention” (for users
    without usernames)
    :param offset: Offset in UTF-16 code units to the start of the entity
    :param length: Length of the entity in UTF-16 code units
    :param url: Optional. For “text_link” only, url that will be opened after user taps on the text
    :param user: Optional. For “text_mention” only, the mentioned user
    :param language: Optional. For “pre” only, the programming language of the entity text
    """

    type: typing.Optional[
        typing.Literal[
            "mention",
            "hashtag",
            "cashtag",
            "bot_command",
            "url",
            "email",
            "phone_number",
            "bold",
            "italic",
            "underline",
            "strikethrough",
            "spoiler",
            "code",
            "pre",
            "text_link",
            "text_mention",
        ]
    ] = Field(default=None)
    offset: typing.Optional[int] = Field(default=None)
    length: typing.Optional[int] = Field(default=None)
    url: typing.Optional[str] = Field(default=None)
    user: typing.Optional["User"] = Field(default=None)
    language: typing.Optional[str] = Field(default=None)


class PhotoSize(BaseModel):
    """
    This object represents one size of a photo or a file / sticker thumbnail.
    :param file_id: Identifier for this file, which can be used to download or reuse the file
    :param file_unique_id: Unique identifier for this file, which is supposed to be the same over time and for
    different bots. Can't be used to download or reuse the file.
    :param width: Photo width
    :param height: Photo height
    :param file_size: Optional. File size in bytes
    """

    file_id: typing.Optional[str] = Field(default=None)
    file_unique_id: typing.Optional[str] = Field(default=None)
    width: typing.Optional[int] = Field(default=None)
    height: typing.Optional[int] = Field(default=None)
    file_size: typing.Optional[int] = Field(default=None)


class Animation(BaseModel):
    """
    This object represents an animation file (GIF or H.264/MPEG-4 AVC video without
    sound).
    :param file_id: Identifier for this file, which can be used to download or reuse the file
    :param file_unique_id: Unique identifier for this file, which is supposed to be the same over time and for
    different bots. Can't be used to download or reuse the file.
    :param width: Video width as defined by sender
    :param height: Video height as defined by sender
    :param duration: Duration of the video in seconds as defined by sender
    :param thumb: Optional. Animation thumbnail as defined by sender
    :param file_name: Optional. Original animation filename as defined by sender
    :param mime_type: Optional. MIME type of the file as defined by sender
    :param file_size: Optional. File size in bytes
    """

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
    """
    This object represents an audio file to be treated as music by the Telegram clients.
    :param file_id: Identifier for this file, which can be used to download or reuse the file
    :param file_unique_id: Unique identifier for this file, which is supposed to be the same over time and for
    different bots. Can't be used to download or reuse the file.
    :param duration: Duration of the audio in seconds as defined by sender
    :param performer: Optional. Performer of the audio as defined by sender or by audio tags
    :param title: Optional. Title of the audio as defined by sender or by audio tags
    :param file_name: Optional. Original filename as defined by sender
    :param mime_type: Optional. MIME type of the file as defined by sender
    :param file_size: Optional. File size in bytes
    :param thumb: Optional. Thumbnail of the album cover to which the music file belongs
    """

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
    """
    This object represents a general file (as opposed to photos, voice messages and
    audio files).
    :param file_id: Identifier for this file, which can be used to download or reuse the file
    :param file_unique_id: Unique identifier for this file, which is supposed to be the same over time and for
    different bots. Can't be used to download or reuse the file.
    :param thumb: Optional. Document thumbnail as defined by sender
    :param file_name: Optional. Original filename as defined by sender
    :param mime_type: Optional. MIME type of the file as defined by sender
    :param file_size: Optional. File size in bytes
    """

    file_id: typing.Optional[str] = Field(default=None)
    file_unique_id: typing.Optional[str] = Field(default=None)
    thumb: typing.Optional["PhotoSize"] = Field(default=None)
    file_name: typing.Optional[str] = Field(default=None)
    mime_type: typing.Optional[str] = Field(default=None)
    file_size: typing.Optional[int] = Field(default=None)


class Video(BaseModel):
    """
    This object represents a video file.
    :param file_id: Identifier for this file, which can be used to download or reuse the file
    :param file_unique_id: Unique identifier for this file, which is supposed to be the same over time and for
    different bots. Can't be used to download or reuse the file.
    :param width: Video width as defined by sender
    :param height: Video height as defined by sender
    :param duration: Duration of the video in seconds as defined by sender
    :param thumb: Optional. Video thumbnail
    :param file_name: Optional. Original filename as defined by sender
    :param mime_type: Optional. Mime type of a file as defined by sender
    :param file_size: Optional. File size in bytes
    """

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
    """
    This object represents a video message (available in Telegram apps as of v.4.0).
    :param file_id: Identifier for this file, which can be used to download or reuse the file
    :param file_unique_id: Unique identifier for this file, which is supposed to be the same over time and for
    different bots. Can't be used to download or reuse the file.
    :param length: Video width and height (diameter of the video message) as defined by sender
    :param duration: Duration of the video in seconds as defined by sender
    :param thumb: Optional. Video thumbnail
    :param file_size: Optional. File size in bytes
    """

    file_id: typing.Optional[str] = Field(default=None)
    file_unique_id: typing.Optional[str] = Field(default=None)
    length: typing.Optional[int] = Field(default=None)
    duration: typing.Optional[int] = Field(default=None)
    thumb: typing.Optional["PhotoSize"] = Field(default=None)
    file_size: typing.Optional[int] = Field(default=None)


class Voice(BaseModel):
    """
    This object represents a voice note.
    :param file_id: Identifier for this file, which can be used to download or reuse the file
    :param file_unique_id: Unique identifier for this file, which is supposed to be the same over time and for
    different bots. Can't be used to download or reuse the file.
    :param duration: Duration of the audio in seconds as defined by sender
    :param mime_type: Optional. MIME type of the file as defined by sender
    :param file_size: Optional. File size in bytes
    """

    file_id: typing.Optional[str] = Field(default=None)
    file_unique_id: typing.Optional[str] = Field(default=None)
    duration: typing.Optional[int] = Field(default=None)
    mime_type: typing.Optional[str] = Field(default=None)
    file_size: typing.Optional[int] = Field(default=None)


class Contact(BaseModel):
    """
    This object represents a phone contact.
    :param phone_number: Contact's phone number
    :param first_name: Contact's first name
    :param last_name: Optional. Contact's last name
    :param user_id: Optional. Contact's user identifier in Telegram. This number may have more than 32
    significant bits and some programming languages may have difficulty/silent defects
    in interpreting it. But it has at most 52 significant bits, so a 64-bit integer or
    double-precision float type are safe for storing this identifier.
    :param vcard: Optional. Additional data about the contact in the form of a vCard
    """

    phone_number: typing.Optional[str] = Field(default=None)
    first_name: typing.Optional[str] = Field(default=None)
    last_name: typing.Optional[str] = Field(default=None)
    user_id: typing.Optional[int] = Field(default=None)
    vcard: typing.Optional[str] = Field(default=None)


class Dice(BaseModel):
    """
    This object represents an animated emoji that displays a random value.
    :param emoji: Emoji on which the dice throw animation is based
    :param value: Value of the dice, 1-6 for “🎲”, “🎯” and “🎳” base emoji, 1-5 for “🏀” and “⚽” base
    emoji, 1-64 for “🎰” base emoji
    """

    emoji: typing.Optional[str] = Field(default=None)
    value: typing.Optional[int] = Field(default=None)


class PollOption(BaseModel):
    """
    This object contains information about one answer option in a poll.
    :param text: Option text, 1-100 characters
    :param voter_count: Number of users that voted for this option
    """

    text: typing.Optional[str] = Field(default=None)
    voter_count: typing.Optional[int] = Field(default=None)


class PollAnswer(BaseModel):
    """
    This object represents an answer of a user in a non-anonymous poll.
    :param poll_id: Unique poll identifier
    :param user: The user, who changed the answer to the poll
    :param option_ids: 0-based identifiers of answer options, chosen by the user. May be empty if the user
    retracted their vote.
    """

    poll_id: typing.Optional[str] = Field(default=None)
    user: typing.Optional["User"] = Field(default=None)
    option_ids: typing.Optional[typing.List[int]] = Field(default=None)


class Poll(BaseModel):
    """
    This object contains information about a poll.
    :param id: Unique poll identifier
    :param question: Poll question, 1-300 characters
    :param options: List of poll options
    :param total_voter_count: Total number of users that voted in the poll
    :param is_closed: True, if the poll is closed
    :param is_anonymous: True, if the poll is anonymous
    :param type: Poll type, currently can be “regular” or “quiz”
    :param allows_multiple_answers: True, if the poll allows multiple answers
    :param correct_option_id: Optional. 0-based identifier of the correct answer option. Available only for polls
    in the quiz mode, which are closed, or was sent (not forwarded) by the bot or to the
    private chat with the bot.
    :param explanation: Optional. Text that is shown when a user chooses an incorrect answer or taps on the
    lamp icon in a quiz-style poll, 0-200 characters
    :param explanation_entities: Optional. Special entities like usernames, URLs, bot commands, etc. that appear in
    the explanation
    :param open_period: Optional. Amount of time in seconds the poll will be active after creation
    :param close_date: Optional. Point in time (Unix timestamp) when the poll will be automatically closed
    """

    id: typing.Optional[str] = Field(default=None)
    question: typing.Optional[str] = Field(default=None)
    options: typing.Optional[typing.List["PollOption"]] = Field(default=None)
    total_voter_count: typing.Optional[int] = Field(default=None)
    is_closed: typing.Optional[bool] = Field(default=None)
    is_anonymous: typing.Optional[bool] = Field(default=None)
    type: typing.Optional[typing.Literal["regular", "quiz"]] = Field(default=None)
    allows_multiple_answers: typing.Optional[bool] = Field(default=None)
    correct_option_id: typing.Optional[int] = Field(default=None)
    explanation: typing.Optional[str] = Field(default=None)
    explanation_entities: typing.Optional[typing.List["MessageEntity"]] = Field(
        default=None
    )
    open_period: typing.Optional[int] = Field(default=None)
    close_date: typing.Optional[int] = Field(default=None)


class Location(BaseModel):
    """
    This object represents a point on the map.
    :param longitude: Longitude as defined by sender
    :param latitude: Latitude as defined by sender
    :param horizontal_accuracy: Optional. The radius of uncertainty for the location, measured in meters; 0-1500
    :param live_period: Optional. Time relative to the message sending date, during which the location can
    be updated; in seconds. For active live locations only.
    :param heading: Optional. The direction in which user is moving, in degrees; 1-360. For active live
    locations only.
    :param proximity_alert_radius: Optional. Maximum distance for proximity alerts about approaching another chat
    member, in meters. For sent live locations only.
    """

    longitude: typing.Optional[float] = Field(default=None)
    latitude: typing.Optional[float] = Field(default=None)
    horizontal_accuracy: typing.Optional[float] = Field(default=None)
    live_period: typing.Optional[int] = Field(default=None)
    heading: typing.Optional[int] = Field(default=None)
    proximity_alert_radius: typing.Optional[int] = Field(default=None)


class Venue(BaseModel):
    """
    This object represents a venue.
    :param location: Venue location. Can't be a live location
    :param title: Name of the venue
    :param address: Address of the venue
    :param foursquare_id: Optional. Foursquare identifier of the venue
    :param foursquare_type: Optional. Foursquare type of the venue. (For example, “arts_entertainment/default”,
    “arts_entertainment/aquarium” or “food/icecream”.)
    :param google_place_id: Optional. Google Places identifier of the venue
    :param google_place_type: Optional. Google Places type of the venue. (See supported types.)
    """

    location: typing.Optional["Location"] = Field(default=None)
    title: typing.Optional[str] = Field(default=None)
    address: typing.Optional[str] = Field(default=None)
    foursquare_id: typing.Optional[str] = Field(default=None)
    foursquare_type: typing.Optional[str] = Field(default=None)
    google_place_id: typing.Optional[str] = Field(default=None)
    google_place_type: typing.Optional[str] = Field(default=None)


class WebAppData(BaseModel):
    """
    Contains data sent from a Web App to the bot.
    :param data: The data. Be aware that a bad client can send arbitrary data in this field.
    :param button_text: Text of the web_app keyboard button, from which the Web App was opened. Be aware
    that a bad client can send arbitrary data in this field.
    """

    data: typing.Optional[str] = Field(default=None)
    button_text: typing.Optional[str] = Field(default=None)


class ProximityAlertTriggered(BaseModel):
    """
    This object represents the content of a service message, sent whenever a user in the
    chat triggers a proximity alert set by another user.
    :param traveler: User that triggered the alert
    :param watcher: User that set the alert
    :param distance: The distance between the users
    """

    traveler: typing.Optional["User"] = Field(default=None)
    watcher: typing.Optional["User"] = Field(default=None)
    distance: typing.Optional[int] = Field(default=None)


class MessageAutoDeleteTimerChanged(BaseModel):
    """
    This object represents a service message about a change in auto-delete timer
    settings.
    :param message_auto_delete_time: New auto-delete time for messages in the chat; in seconds
    """

    message_auto_delete_time: typing.Optional[int] = Field(default=None)


class VideoChatScheduled(BaseModel):
    """
    This object represents a service message about a video chat scheduled in the chat.
    :param start_date: Point in time (Unix timestamp) when the video chat is supposed to be started by a
    chat administrator
    """

    start_date: typing.Optional[int] = Field(default=None)


class VideoChatStarted(BaseModel):
    """
    This object represents a service message about a video chat started in the chat.
    Currently holds no information.
    """

    pass


class VideoChatEnded(BaseModel):
    """
    This object represents a service message about a video chat ended in the chat.
    :param duration: Video chat duration in seconds
    """

    duration: typing.Optional[int] = Field(default=None)


class VideoChatParticipantsInvited(BaseModel):
    """
    This object represents a service message about new members invited to a video chat.
    :param users: New members that were invited to the video chat
    """

    users: typing.Optional[typing.List["User"]] = Field(default=None)


class UserProfilePhotos(BaseModel):
    """
    This object represent a user's profile pictures.
    :param total_count: Total number of profile pictures the target user has
    :param photos: Requested profile pictures (in up to 4 sizes each)
    """

    total_count: typing.Optional[int] = Field(default=None)
    photos: typing.Optional[typing.List[typing.List["PhotoSize"]]] = Field(default=None)


class File(BaseModel):
    """
    This object represents a file ready to be downloaded. The file can be downloaded via
    the link https://api.telegram.org/file/bot&lt;token&gt;/&lt;file_path&gt;. It is
    guaranteed that the link will be valid for at least 1 hour. When the link expires, a
    new one can be requested by calling getFile. Maximum file size to download is 20 MB
    :param file_id: Identifier for this file, which can be used to download or reuse the file
    :param file_unique_id: Unique identifier for this file, which is supposed to be the same over time and for
    different bots. Can't be used to download or reuse the file.
    :param file_size: Optional. File size in bytes, if known
    :param file_path: Optional. File path. Use
    https://api.telegram.org/file/bot&lt;token&gt;/&lt;file_path&gt; to get the file.
    """

    file_id: typing.Optional[str] = Field(default=None)
    file_unique_id: typing.Optional[str] = Field(default=None)
    file_size: typing.Optional[int] = Field(default=None)
    file_path: typing.Optional[str] = Field(default=None)


class WebAppInfo(BaseModel):
    """
    Contains information about a Web App.
    :param url: An HTTPS URL of a Web App to be opened with additional data as specified in
    Initializing Web Apps
    """

    url: typing.Optional[str] = Field(default=None)


class ReplyKeyboardMarkup(BaseModel):
    """
    This object represents a custom keyboard with reply options (see Introduction to
    bots for details and examples).
    :param keyboard: Array of button rows, each represented by an Array of KeyboardButton objects
    :param resize_keyboard: Optional. Requests clients to resize the keyboard vertically for optimal fit (e.g.,
    make the keyboard smaller if there are just two rows of buttons). Defaults to false,
    in which case the custom keyboard is always of the same height as the app's standard
    keyboard.
    :param one_time_keyboard: Optional. Requests clients to hide the keyboard as soon as it's been used. The
    keyboard will still be available, but clients will automatically display the usual
    letter-keyboard in the chat – the user can press a special button in the input field
    to see the custom keyboard again. Defaults to false.
    :param input_field_placeholder: Optional. The placeholder to be shown in the input field when the keyboard is
    active; 1-64 characters
    :param selective: Optional. Use this parameter if you want to show the keyboard to specific users
    only. Targets: 1) users that are @mentioned in the text of the Message object; 2) if
    the bot's message is a reply (has reply_to_message_id), sender of the original
    message.   Example: A user requests to change the bot's language, bot replies to the
    request with a keyboard to select the new language. Other users in the group don't
    see the keyboard.
    """

    keyboard: typing.Optional[typing.List[typing.List["KeyboardButton"]]] = Field(
        default=None
    )
    resize_keyboard: typing.Optional[bool] = Field(default=None)
    one_time_keyboard: typing.Optional[bool] = Field(default=None)
    input_field_placeholder: typing.Optional[str] = Field(default=None)
    selective: typing.Optional[bool] = Field(default=None)


class KeyboardButton(BaseModel):
    """
    This object represents one button of the reply keyboard. For simple text buttons
    String can be used instead of this object to specify text of the button. Optional
    fields web_app, request_contact, request_location, and request_poll are mutually
    exclusive.
    :param text: Text of the button. If none of the optional fields are used, it will be sent as a
    message when the button is pressed
    :param request_contact: Optional. If True, the user's phone number will be sent as a contact when the button
    is pressed. Available in private chats only.
    :param request_location: Optional. If True, the user's current location will be sent when the button is
    pressed. Available in private chats only.
    :param request_poll: Optional. If specified, the user will be asked to create a poll and send it to the
    bot when the button is pressed. Available in private chats only.
    :param web_app: Optional. If specified, the described Web App will be launched when the button is
    pressed. The Web App will be able to send a “web_app_data” service message.
    Available in private chats only.
    """

    text: typing.Optional[str] = Field(default=None)
    request_contact: typing.Optional[bool] = Field(default=None)
    request_location: typing.Optional[bool] = Field(default=None)
    request_poll: typing.Optional["KeyboardButtonPollType"] = Field(default=None)
    web_app: typing.Optional["WebAppInfo"] = Field(default=None)


class KeyboardButtonPollType(BaseModel):
    """
    This object represents type of a poll, which is allowed to be created and sent when
    the corresponding button is pressed.
    :param type: Optional. If quiz is passed, the user will be allowed to create only polls in the
    quiz mode. If regular is passed, only regular polls will be allowed. Otherwise, the
    user will be allowed to create a poll of any type.
    """

    type: typing.Optional[str] = Field(default=None)


class ReplyKeyboardRemove(BaseModel):
    """
    Upon receiving a message with this object, Telegram clients will remove the current
    custom keyboard and display the default letter-keyboard. By default, custom
    keyboards are displayed until a new keyboard is sent by a bot. An exception is made
    for one-time keyboards that are hidden immediately after the user presses a button
    (see ReplyKeyboardMarkup).
    :param remove_keyboard: Requests clients to remove the custom keyboard (user will not be able to summon this
    keyboard; if you want to hide the keyboard from sight but keep it accessible, use
    one_time_keyboard in ReplyKeyboardMarkup)
    :param selective: Optional. Use this parameter if you want to remove the keyboard for specific users
    only. Targets: 1) users that are @mentioned in the text of the Message object; 2) if
    the bot's message is a reply (has reply_to_message_id), sender of the original
    message.   Example: A user votes in a poll, bot returns confirmation message in
    reply to the vote and removes the keyboard for that user, while still showing the
    keyboard with poll options to users who haven't voted yet.
    """

    remove_keyboard: typing.Optional[bool] = Field(default=None)
    selective: typing.Optional[bool] = Field(default=None)


class InlineKeyboardMarkup(BaseModel):
    """
    This object represents an inline keyboard that appears right next to the message it
    belongs to.
    :param inline_keyboard: Array of button rows, each represented by an Array of InlineKeyboardButton objects
    """

    inline_keyboard: typing.Optional[
        typing.List[typing.List["InlineKeyboardButton"]]
    ] = Field(default=None)


class InlineKeyboardButton(BaseModel):
    """
    This object represents one button of an inline keyboard. You must use exactly one of
    the optional fields.
    :param text: Label text on the button
    :param url: Optional. HTTP or tg:// url to be opened when the button is pressed. Links
    tg://user?id=&lt;user_id&gt; can be used to mention a user by their ID without using
    a username, if this is allowed by their privacy settings.
    :param callback_data: Optional. Data to be sent in a callback query to the bot when button is pressed,
    1-64 bytes
    :param web_app: Optional. Description of the Web App that will be launched when the user presses the
    button. The Web App will be able to send an arbitrary message on behalf of the user
    using the method answerWebAppQuery. Available only in private chats between a user
    and the bot.
    :param login_url: Optional. An HTTP URL used to automatically authorize the user. Can be used as a
    replacement for the Telegram Login Widget.
    :param switch_inline_query: Optional. If set, pressing the button will prompt the user to select one of their
    chats, open that chat and insert the bot's username and the specified inline query
    in the input field. Can be empty, in which case just the bot's username will be
    inserted.   Note: This offers an easy way for users to start using your bot in
    inline mode when they are currently in a private chat with it. Especially useful
    when combined with switch_pm… actions – in this case the user will be automatically
    returned to the chat they switched from, skipping the chat selection screen.
    :param switch_inline_query_current_chat: Optional. If set, pressing the button will insert the bot's username and the
    specified inline query in the current chat's input field. Can be empty, in which
    case only the bot's username will be inserted.   This offers a quick way for the
    user to open your bot in inline mode in the same chat – good for selecting something
    from multiple options.
    :param callback_game: Optional. Description of the game that will be launched when the user presses the
    button.   NOTE: This type of button must always be the first button in the first
    row.
    :param pay: Optional. Specify True, to send a Pay button.   NOTE: This type of button must
    always be the first button in the first row and can only be used in invoice
    messages.
    """

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
    """
    This object represents a parameter of the inline keyboard button used to
    automatically authorize a user. Serves as a great replacement for the Telegram Login
    Widget when the user is coming from Telegram. All the user needs to do is tap/click
    a button and confirm that they want to log in: Telegram apps support these buttons
    as of version 5.7. Sample bot: @discussbot
    :param url: An HTTP URL to be opened with user authorization data added to the query string when
    the button is pressed. If the user refuses to provide authorization data, the
    original URL without information about the user will be opened. The data added is
    the same as described in Receiving authorization data.   NOTE: You must always check
    the hash of the received data to verify the authentication and the integrity of the
    data as described in Checking authorization.
    :param forward_text: Optional. New text of the button in forwarded messages.
    :param bot_username: Optional. Username of a bot, which will be used for user authorization. See Setting
    up a bot for more details. If not specified, the current bot's username will be
    assumed. The url's domain must be the same as the domain linked with the bot. See
    Linking your domain to the bot for more details.
    :param request_write_access: Optional. Pass True to request the permission for your bot to send messages to the
    user.
    """

    url: typing.Optional[str] = Field(default=None)
    forward_text: typing.Optional[str] = Field(default=None)
    bot_username: typing.Optional[str] = Field(default=None)
    request_write_access: typing.Optional[bool] = Field(default=None)


class CallbackQuery(BaseModel):
    """
    This object represents an incoming callback query from a callback button in an
    inline keyboard. If the button that originated the query was attached to a message
    sent by the bot, the field message will be present. If the button was attached to a
    message sent via the bot (in inline mode), the field inline_message_id will be
    present. Exactly one of the fields data or game_short_name will be present.
    :param id: Unique identifier for this query
    :param from: Sender
    :param message: Optional. Message with the callback button that originated the query. Note that
    message content and message date will not be available if the message is too old
    :param inline_message_id: Optional. Identifier of the message sent via the bot in inline mode, that originated
    the query.
    :param chat_instance: Global identifier, uniquely corresponding to the chat to which the message with the
    callback button was sent. Useful for high scores in games.
    :param data: Optional. Data associated with the callback button. Be aware that the message, which
    originated the query, can contain no callback buttons with this data.
    :param game_short_name: Optional. Short name of a Game to be returned, serves as the unique identifier for
    the game
    """

    id: typing.Optional[str] = Field(default=None)
    from_: typing.Optional["User"] = Field(default=None, alias="from")
    message: typing.Optional["Message"] = Field(default=None)
    inline_message_id: typing.Optional[str] = Field(default=None)
    chat_instance: typing.Optional[str] = Field(default=None)
    data: typing.Optional[str] = Field(default=None)
    game_short_name: typing.Optional[str] = Field(default=None)


class ForceReply(BaseModel):
    """
    Upon receiving a message with this object, Telegram clients will display a reply
    interface to the user (act as if the user has selected the bot's message and tapped
    'Reply'). This can be extremely useful if you want to create user-friendly step-by-
    step interfaces without having to sacrifice privacy mode.
    :param force_reply: Shows reply interface to the user, as if they manually selected the bot's message
    and tapped 'Reply'
    :param input_field_placeholder: Optional. The placeholder to be shown in the input field when the reply is active;
    1-64 characters
    :param selective: Optional. Use this parameter if you want to force reply from specific users only.
    Targets: 1) users that are @mentioned in the text of the Message object; 2) if the
    bot's message is a reply (has reply_to_message_id), sender of the original message.
    """

    force_reply: typing.Optional[bool] = Field(default=None)
    input_field_placeholder: typing.Optional[str] = Field(default=None)
    selective: typing.Optional[bool] = Field(default=None)


class ChatPhoto(BaseModel):
    """
    This object represents a chat photo.
    :param small_file_id: File identifier of small (160x160) chat photo. This file_id can be used only for
    photo download and only for as long as the photo is not changed.
    :param small_file_unique_id: Unique file identifier of small (160x160) chat photo, which is supposed to be the
    same over time and for different bots. Can't be used to download or reuse the file.
    :param big_file_id: File identifier of big (640x640) chat photo. This file_id can be used only for photo
    download and only for as long as the photo is not changed.
    :param big_file_unique_id: Unique file identifier of big (640x640) chat photo, which is supposed to be the same
    over time and for different bots. Can't be used to download or reuse the file.
    """

    small_file_id: typing.Optional[str] = Field(default=None)
    small_file_unique_id: typing.Optional[str] = Field(default=None)
    big_file_id: typing.Optional[str] = Field(default=None)
    big_file_unique_id: typing.Optional[str] = Field(default=None)


class ChatInviteLink(BaseModel):
    """
    Represents an invite link for a chat.
    :param invite_link: The invite link. If the link was created by another chat administrator, then the
    second part of the link will be replaced with “…”.
    :param creator: Creator of the link
    :param creates_join_request: True, if users joining the chat via the link need to be approved by chat
    administrators
    :param is_primary: True, if the link is primary
    :param is_revoked: True, if the link is revoked
    :param name: Optional. Invite link name
    :param expire_date: Optional. Point in time (Unix timestamp) when the link will expire or has been
    expired
    :param member_limit: Optional. Maximum number of users that can be members of the chat simultaneously
    after joining the chat via this invite link; 1-99999
    :param pending_join_request_count: Optional. Number of pending join requests created using this link
    """

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
    """
    Represents the rights of an administrator in a chat.
    :param is_anonymous: True, if the user's presence in the chat is hidden
    :param can_manage_chat: True, if the administrator can access the chat event log, chat statistics, message
    statistics in channels, see channel members, see anonymous administrators in
    supergroups and ignore slow mode. Implied by any other administrator privilege
    :param can_delete_messages: True, if the administrator can delete messages of other users
    :param can_manage_video_chats: True, if the administrator can manage video chats
    :param can_restrict_members: True, if the administrator can restrict, ban or unban chat members
    :param can_promote_members: True, if the administrator can add new administrators with a subset of their own
    privileges or demote administrators that he has promoted, directly or indirectly
    (promoted by administrators that were appointed by the user)
    :param can_change_info: True, if the user is allowed to change the chat title, photo and other settings
    :param can_invite_users: True, if the user is allowed to invite new users to the chat
    :param can_post_messages: Optional. True, if the administrator can post in the channel; channels only
    :param can_edit_messages: Optional. True, if the administrator can edit messages of other users and can pin
    messages; channels only
    :param can_pin_messages: Optional. True, if the user is allowed to pin messages; groups and supergroups only
    """

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
    """
    This object contains information about one member of a chat. Currently, the
    following 6 types of chat members are supported:  ChatMemberOwner
    ChatMemberAdministrator ChatMemberMember ChatMemberRestricted ChatMemberLeft
    ChatMemberBanned
    """

    value: typing.Optional[
        typing.Union[
            "ChatMemberOwner",
            "ChatMemberAdministrator",
            "ChatMemberMember",
            "ChatMemberRestricted",
            "ChatMemberLeft",
            "ChatMemberBanned",
        ]
    ] = Field(None)


class ChatMemberOwner(BaseModel):
    """
    Represents a chat member that owns the chat and has all administrator privileges.
    :param status: The member's status in the chat, always “creator”
    :param user: Information about the user
    :param is_anonymous: True, if the user's presence in the chat is hidden
    :param custom_title: Optional. Custom title for this user
    """

    status: typing.Optional[str] = Field(default=None)
    user: typing.Optional["User"] = Field(default=None)
    is_anonymous: typing.Optional[bool] = Field(default=None)
    custom_title: typing.Optional[str] = Field(default=None)


class ChatMemberAdministrator(BaseModel):
    """
    Represents a chat member that has some additional privileges.
    :param status: The member's status in the chat, always “administrator”
    :param user: Information about the user
    :param can_be_edited: True, if the bot is allowed to edit administrator privileges of that user
    :param is_anonymous: True, if the user's presence in the chat is hidden
    :param can_manage_chat: True, if the administrator can access the chat event log, chat statistics, message
    statistics in channels, see channel members, see anonymous administrators in
    supergroups and ignore slow mode. Implied by any other administrator privilege
    :param can_delete_messages: True, if the administrator can delete messages of other users
    :param can_manage_video_chats: True, if the administrator can manage video chats
    :param can_restrict_members: True, if the administrator can restrict, ban or unban chat members
    :param can_promote_members: True, if the administrator can add new administrators with a subset of their own
    privileges or demote administrators that he has promoted, directly or indirectly
    (promoted by administrators that were appointed by the user)
    :param can_change_info: True, if the user is allowed to change the chat title, photo and other settings
    :param can_invite_users: True, if the user is allowed to invite new users to the chat
    :param can_post_messages: Optional. True, if the administrator can post in the channel; channels only
    :param can_edit_messages: Optional. True, if the administrator can edit messages of other users and can pin
    messages; channels only
    :param can_pin_messages: Optional. True, if the user is allowed to pin messages; groups and supergroups only
    :param custom_title: Optional. Custom title for this user
    """

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
    """
    Represents a chat member that has no additional privileges or restrictions.
    :param status: The member's status in the chat, always “member”
    :param user: Information about the user
    """

    status: typing.Optional[str] = Field(default=None)
    user: typing.Optional["User"] = Field(default=None)


class ChatMemberRestricted(BaseModel):
    """
    Represents a chat member that is under certain restrictions in the chat. Supergroups
    only.
    :param status: The member's status in the chat, always “restricted”
    :param user: Information about the user
    :param is_member: True, if the user is a member of the chat at the moment of the request
    :param can_change_info: True, if the user is allowed to change the chat title, photo and other settings
    :param can_invite_users: True, if the user is allowed to invite new users to the chat
    :param can_pin_messages: True, if the user is allowed to pin messages
    :param can_send_messages: True, if the user is allowed to send text messages, contacts, locations and venues
    :param can_send_media_messages: True, if the user is allowed to send audios, documents, photos, videos, video notes
    and voice notes
    :param can_send_polls: True, if the user is allowed to send polls
    :param can_send_other_messages: True, if the user is allowed to send animations, games, stickers and use inline bots
    :param can_add_web_page_previews: True, if the user is allowed to add web page previews to their messages
    :param until_date: Date when restrictions will be lifted for this user; unix time. If 0, then the user
    is restricted forever
    """

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
    """
    Represents a chat member that isn't currently a member of the chat, but may join it
    themselves.
    :param status: The member's status in the chat, always “left”
    :param user: Information about the user
    """

    status: typing.Optional[str] = Field(default=None)
    user: typing.Optional["User"] = Field(default=None)


class ChatMemberBanned(BaseModel):
    """
    Represents a chat member that was banned in the chat and can't return to the chat or
    view chat messages.
    :param status: The member's status in the chat, always “kicked”
    :param user: Information about the user
    :param until_date: Date when restrictions will be lifted for this user; unix time. If 0, then the user
    is banned forever
    """

    status: typing.Optional[str] = Field(default=None)
    user: typing.Optional["User"] = Field(default=None)
    until_date: typing.Optional[int] = Field(default=None)


class ChatMemberUpdated(BaseModel):
    """
    This object represents changes in the status of a chat member.
    :param chat: Chat the user belongs to
    :param from: Performer of the action, which resulted in the change
    :param date: Date the change was done in Unix time
    :param old_chat_member: Previous information about the chat member
    :param new_chat_member: New information about the chat member
    :param invite_link: Optional. Chat invite link, which was used by the user to join the chat; for joining
    by invite link events only.
    """

    chat: typing.Optional["Chat"] = Field(default=None)
    from_: typing.Optional["User"] = Field(default=None, alias="from")
    date: typing.Optional[int] = Field(default=None)
    old_chat_member: typing.Optional["ChatMember"] = Field(default=None)
    new_chat_member: typing.Optional["ChatMember"] = Field(default=None)
    invite_link: typing.Optional["ChatInviteLink"] = Field(default=None)


class ChatJoinRequest(BaseModel):
    """
    Represents a join request sent to a chat.
    :param chat: Chat to which the request was sent
    :param from: User that sent the join request
    :param date: Date the request was sent in Unix time
    :param bio: Optional. Bio of the user.
    :param invite_link: Optional. Chat invite link that was used by the user to send the join request
    """

    chat: typing.Optional["Chat"] = Field(default=None)
    from_: typing.Optional["User"] = Field(default=None, alias="from")
    date: typing.Optional[int] = Field(default=None)
    bio: typing.Optional[str] = Field(default=None)
    invite_link: typing.Optional["ChatInviteLink"] = Field(default=None)


class ChatPermissions(BaseModel):
    """
    Describes actions that a non-administrator user is allowed to take in a chat.
    :param can_send_messages: Optional. True, if the user is allowed to send text messages, contacts, locations
    and venues
    :param can_send_media_messages: Optional. True, if the user is allowed to send audios, documents, photos, videos,
    video notes and voice notes, implies can_send_messages
    :param can_send_polls: Optional. True, if the user is allowed to send polls, implies can_send_messages
    :param can_send_other_messages: Optional. True, if the user is allowed to send animations, games, stickers and use
    inline bots, implies can_send_media_messages
    :param can_add_web_page_previews: Optional. True, if the user is allowed to add web page previews to their messages,
    implies can_send_media_messages
    :param can_change_info: Optional. True, if the user is allowed to change the chat title, photo and other
    settings. Ignored in public supergroups
    :param can_invite_users: Optional. True, if the user is allowed to invite new users to the chat
    :param can_pin_messages: Optional. True, if the user is allowed to pin messages. Ignored in public
    supergroups
    """

    can_send_messages: typing.Optional[bool] = Field(default=None)
    can_send_media_messages: typing.Optional[bool] = Field(default=None)
    can_send_polls: typing.Optional[bool] = Field(default=None)
    can_send_other_messages: typing.Optional[bool] = Field(default=None)
    can_add_web_page_previews: typing.Optional[bool] = Field(default=None)
    can_change_info: typing.Optional[bool] = Field(default=None)
    can_invite_users: typing.Optional[bool] = Field(default=None)
    can_pin_messages: typing.Optional[bool] = Field(default=None)


class ChatLocation(BaseModel):
    """
    Represents a location to which a chat is connected.
    :param location: The location to which the supergroup is connected. Can't be a live location.
    :param address: Location address; 1-64 characters, as defined by the chat owner
    """

    location: typing.Optional["Location"] = Field(default=None)
    address: typing.Optional[str] = Field(default=None)


class BotCommand(BaseModel):
    """
    This object represents a bot command.
    :param command: Text of the command; 1-32 characters. Can contain only lowercase English letters,
    digits and underscores.
    :param description: Description of the command; 1-256 characters.
    """

    command: typing.Optional[str] = Field(default=None)
    description: typing.Optional[str] = Field(default=None)


class BotCommandScope(BaseModel):
    """
    This object represents the scope to which bot commands are applied. Currently, the
    following 7 scopes are supported:  BotCommandScopeDefault
    BotCommandScopeAllPrivateChats BotCommandScopeAllGroupChats
    BotCommandScopeAllChatAdministrators BotCommandScopeChat
    BotCommandScopeChatAdministrators BotCommandScopeChatMember
    """

    value: typing.Optional[
        typing.Union[
            "BotCommandScopeDefault",
            "BotCommandScopeAllPrivateChats",
            "BotCommandScopeAllGroupChats",
            "BotCommandScopeAllChatAdministrators",
            "BotCommandScopeChat",
            "BotCommandScopeChatAdministrators",
            "BotCommandScopeChatMember",
        ]
    ] = Field(None)


class BotCommandScopeDefault(BaseModel):
    """
    Represents the default scope of bot commands. Default commands are used if no
    commands with a narrower scope are specified for the user.
    :param type: Scope type, must be default
    """

    type: typing.Optional[str] = Field(default=None)


class BotCommandScopeAllPrivateChats(BaseModel):
    """
    Represents the scope of bot commands, covering all private chats.
    :param type: Scope type, must be all_private_chats
    """

    type: typing.Optional[str] = Field(default=None)


class BotCommandScopeAllGroupChats(BaseModel):
    """
    Represents the scope of bot commands, covering all group and supergroup chats.
    :param type: Scope type, must be all_group_chats
    """

    type: typing.Optional[str] = Field(default=None)


class BotCommandScopeAllChatAdministrators(BaseModel):
    """
    Represents the scope of bot commands, covering all group and supergroup chat
    administrators.
    :param type: Scope type, must be all_chat_administrators
    """

    type: typing.Optional[str] = Field(default=None)


class BotCommandScopeChat(BaseModel):
    """
    Represents the scope of bot commands, covering a specific chat.
    :param type: Scope type, must be chat
    :param chat_id: Unique identifier for the target chat or username of the target supergroup (in the
    format @supergroupusername)
    """

    type: typing.Optional[str] = Field(default=None)
    chat_id: typing.Optional[typing.Union[int, str]] = Field(default=None)


class BotCommandScopeChatAdministrators(BaseModel):
    """
    Represents the scope of bot commands, covering all administrators of a specific
    group or supergroup chat.
    :param type: Scope type, must be chat_administrators
    :param chat_id: Unique identifier for the target chat or username of the target supergroup (in the
    format @supergroupusername)
    """

    type: typing.Optional[str] = Field(default=None)
    chat_id: typing.Optional[typing.Union[int, str]] = Field(default=None)


class BotCommandScopeChatMember(BaseModel):
    """
    Represents the scope of bot commands, covering a specific member of a group or
    supergroup chat.
    :param type: Scope type, must be chat_member
    :param chat_id: Unique identifier for the target chat or username of the target supergroup (in the
    format @supergroupusername)
    :param user_id: Unique identifier of the target user
    """

    type: typing.Optional[str] = Field(default=None)
    chat_id: typing.Optional[typing.Union[int, str]] = Field(default=None)
    user_id: typing.Optional[int] = Field(default=None)


class MenuButton(BaseModel):
    """
    This object describes the bot's menu button in a private chat. It should be one of
    MenuButtonCommands MenuButtonWebApp MenuButtonDefault
    """

    value: typing.Optional[
        typing.Union["MenuButtonCommands", "MenuButtonWebApp", "MenuButtonDefault"]
    ] = Field(None)


class MenuButtonCommands(BaseModel):
    """
    Represents a menu button, which opens the bot's list of commands.
    :param type: Type of the button, must be commands
    """

    type: typing.Optional[str] = Field(default=None)


class MenuButtonWebApp(BaseModel):
    """
    Represents a menu button, which launches a Web App.
    :param type: Type of the button, must be web_app
    :param text: Text on the button
    :param web_app: Description of the Web App that will be launched when the user presses the button.
    The Web App will be able to send an arbitrary message on behalf of the user using
    the method answerWebAppQuery.
    """

    type: typing.Optional[str] = Field(default=None)
    text: typing.Optional[str] = Field(default=None)
    web_app: typing.Optional["WebAppInfo"] = Field(default=None)


class MenuButtonDefault(BaseModel):
    """
    Describes that no specific value for the menu button was set.
    :param type: Type of the button, must be default
    """

    type: typing.Optional[str] = Field(default=None)


class ResponseParameters(BaseModel):
    """
    Contains information about why a request was unsuccessful.
    :param migrate_to_chat_id: Optional. The group has been migrated to a supergroup with the specified identifier.
    This number may have more than 32 significant bits and some programming languages
    may have difficulty/silent defects in interpreting it. But it has at most 52
    significant bits, so a signed 64-bit integer or double-precision float type are safe
    for storing this identifier.
    :param retry_after: Optional. In case of exceeding flood control, the number of seconds left to wait
    before the request can be repeated
    """

    migrate_to_chat_id: typing.Optional[int] = Field(default=None)
    retry_after: typing.Optional[int] = Field(default=None)


class InputMedia(BaseModel):
    """
    This object represents the content of a media message to be sent. It should be one
    of  InputMediaAnimation InputMediaDocument InputMediaAudio InputMediaPhoto
    InputMediaVideo
    """

    value: typing.Optional[
        typing.Union[
            "InputMediaAnimation",
            "InputMediaDocument",
            "InputMediaAudio",
            "InputMediaPhoto",
            "InputMediaVideo",
        ]
    ] = Field(None)


class InputMediaPhoto(BaseModel):
    """
    Represents a photo to be sent.
    :param type: Type of the result, must be photo
    :param media: File to send. Pass a file_id to send a file that exists on the Telegram servers
    (recommended), pass an HTTP URL for Telegram to get a file from the Internet, or
    pass “attach://” to upload a new one using multipart/form-data under  name. More
    info on Sending Files »
    :param caption: Optional. Caption of the photo to be sent, 0-1024 characters after entities parsing
    :param parse_mode: Optional. Mode for parsing entities in the photo caption. See formatting options for
    more details.
    :param caption_entities: Optional. List of special entities that appear in the caption, which can be
    specified instead of parse_mode
    """

    type: typing.Optional[str] = Field(default=None)
    media: typing.Optional[str] = Field(default=None)
    caption: typing.Optional[str] = Field(default=None)
    parse_mode: typing.Optional[str] = Field(default=None)
    caption_entities: typing.Optional[typing.List["MessageEntity"]] = Field(
        default=None
    )


class InputMediaVideo(BaseModel):
    """
    Represents a video to be sent.
    :param type: Type of the result, must be video
    :param media: File to send. Pass a file_id to send a file that exists on the Telegram servers
    (recommended), pass an HTTP URL for Telegram to get a file from the Internet, or
    pass “attach://” to upload a new one using multipart/form-data under  name. More
    info on Sending Files »
    :param thumb: Optional. Thumbnail of the file sent; can be ignored if thumbnail generation for the
    file is supported server-side. The thumbnail should be in JPEG format and less than
    200 kB in size. A thumbnail's width and height should not exceed 320. Ignored if the
    file is not uploaded using multipart/form-data. Thumbnails can't be reused and can
    be only uploaded as a new file, so you can pass “attach://” if the thumbnail was
    uploaded using multipart/form-data under . More info on Sending Files »
    :param caption: Optional. Caption of the video to be sent, 0-1024 characters after entities parsing
    :param parse_mode: Optional. Mode for parsing entities in the video caption. See formatting options for
    more details.
    :param caption_entities: Optional. List of special entities that appear in the caption, which can be
    specified instead of parse_mode
    :param width: Optional. Video width
    :param height: Optional. Video height
    :param duration: Optional. Video duration in seconds
    :param supports_streaming: Optional. Pass True, if the uploaded video is suitable for streaming
    """

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
    """
    Represents an animation file (GIF or H.264/MPEG-4 AVC video without sound) to be
    sent.
    :param type: Type of the result, must be animation
    :param media: File to send. Pass a file_id to send a file that exists on the Telegram servers
    (recommended), pass an HTTP URL for Telegram to get a file from the Internet, or
    pass “attach://” to upload a new one using multipart/form-data under  name. More
    info on Sending Files »
    :param thumb: Optional. Thumbnail of the file sent; can be ignored if thumbnail generation for the
    file is supported server-side. The thumbnail should be in JPEG format and less than
    200 kB in size. A thumbnail's width and height should not exceed 320. Ignored if the
    file is not uploaded using multipart/form-data. Thumbnails can't be reused and can
    be only uploaded as a new file, so you can pass “attach://” if the thumbnail was
    uploaded using multipart/form-data under . More info on Sending Files »
    :param caption: Optional. Caption of the animation to be sent, 0-1024 characters after entities
    parsing
    :param parse_mode: Optional. Mode for parsing entities in the animation caption. See formatting options
    for more details.
    :param caption_entities: Optional. List of special entities that appear in the caption, which can be
    specified instead of parse_mode
    :param width: Optional. Animation width
    :param height: Optional. Animation height
    :param duration: Optional. Animation duration in seconds
    """

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
    """
    Represents an audio file to be treated as music to be sent.
    :param type: Type of the result, must be audio
    :param media: File to send. Pass a file_id to send a file that exists on the Telegram servers
    (recommended), pass an HTTP URL for Telegram to get a file from the Internet, or
    pass “attach://” to upload a new one using multipart/form-data under  name. More
    info on Sending Files »
    :param thumb: Optional. Thumbnail of the file sent; can be ignored if thumbnail generation for the
    file is supported server-side. The thumbnail should be in JPEG format and less than
    200 kB in size. A thumbnail's width and height should not exceed 320. Ignored if the
    file is not uploaded using multipart/form-data. Thumbnails can't be reused and can
    be only uploaded as a new file, so you can pass “attach://” if the thumbnail was
    uploaded using multipart/form-data under . More info on Sending Files »
    :param caption: Optional. Caption of the audio to be sent, 0-1024 characters after entities parsing
    :param parse_mode: Optional. Mode for parsing entities in the audio caption. See formatting options for
    more details.
    :param caption_entities: Optional. List of special entities that appear in the caption, which can be
    specified instead of parse_mode
    :param duration: Optional. Duration of the audio in seconds
    :param performer: Optional. Performer of the audio
    :param title: Optional. Title of the audio
    """

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
    """
    Represents a general file to be sent.
    :param type: Type of the result, must be document
    :param media: File to send. Pass a file_id to send a file that exists on the Telegram servers
    (recommended), pass an HTTP URL for Telegram to get a file from the Internet, or
    pass “attach://” to upload a new one using multipart/form-data under  name. More
    info on Sending Files »
    :param thumb: Optional. Thumbnail of the file sent; can be ignored if thumbnail generation for the
    file is supported server-side. The thumbnail should be in JPEG format and less than
    200 kB in size. A thumbnail's width and height should not exceed 320. Ignored if the
    file is not uploaded using multipart/form-data. Thumbnails can't be reused and can
    be only uploaded as a new file, so you can pass “attach://” if the thumbnail was
    uploaded using multipart/form-data under . More info on Sending Files »
    :param caption: Optional. Caption of the document to be sent, 0-1024 characters after entities
    parsing
    :param parse_mode: Optional. Mode for parsing entities in the document caption. See formatting options
    for more details.
    :param caption_entities: Optional. List of special entities that appear in the caption, which can be
    specified instead of parse_mode
    :param disable_content_type_detection: Optional. Disables automatic server-side content type detection for files uploaded
    using multipart/form-data. Always True, if the document is sent as part of an album.
    """

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
    """
    This object represents the contents of a file to be uploaded. Must be posted using
    multipart/form-data in the usual way that files are uploaded via the browser.
    """

    pass


class Sticker(BaseModel):
    """
    This object represents a sticker.
    :param file_id: Identifier for this file, which can be used to download or reuse the file
    :param file_unique_id: Unique identifier for this file, which is supposed to be the same over time and for
    different bots. Can't be used to download or reuse the file.
    :param width: Sticker width
    :param height: Sticker height
    :param is_animated: True, if the sticker is animated
    :param is_video: True, if the sticker is a video sticker
    :param thumb: Optional. Sticker thumbnail in the .WEBP or .JPG format
    :param emoji: Optional. Emoji associated with the sticker
    :param set_name: Optional. Name of the sticker set to which the sticker belongs
    :param mask_position: Optional. For mask stickers, the position where the mask should be placed
    :param file_size: Optional. File size in bytes
    """

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
    """
    This object represents a sticker set.
    :param name: Sticker set name
    :param title: Sticker set title
    :param is_animated: True, if the sticker set contains animated stickers
    :param is_video: True, if the sticker set contains video stickers
    :param contains_masks: True, if the sticker set contains masks
    :param stickers: List of all set stickers
    :param thumb: Optional. Sticker set thumbnail in the .WEBP, .TGS, or .WEBM format
    """

    name: typing.Optional[str] = Field(default=None)
    title: typing.Optional[str] = Field(default=None)
    is_animated: typing.Optional[bool] = Field(default=None)
    is_video: typing.Optional[bool] = Field(default=None)
    contains_masks: typing.Optional[bool] = Field(default=None)
    stickers: typing.Optional[typing.List["Sticker"]] = Field(default=None)
    thumb: typing.Optional["PhotoSize"] = Field(default=None)


class MaskPosition(BaseModel):
    """
    This object describes the position on faces where a mask should be placed by
    default.
    :param point: The part of the face relative to which the mask should be placed. One of “forehead”,
    “eyes”, “mouth”, or “chin”.
    :param x_shift: Shift by X-axis measured in widths of the mask scaled to the face size, from left to
    right. For example, choosing -1.0 will place mask just to the left of the default
    mask position.
    :param y_shift: Shift by Y-axis measured in heights of the mask scaled to the face size, from top to
    bottom. For example, 1.0 will place the mask just below the default mask position.
    :param scale: Mask scaling coefficient. For example, 2.0 means double size.
    """

    point: typing.Optional[typing.Literal["forehead", "eyes", "mouth", "chin"]] = Field(
        default=None
    )
    x_shift: typing.Optional[float] = Field(default=None)
    y_shift: typing.Optional[float] = Field(default=None)
    scale: typing.Optional[float] = Field(default=None)


class InlineQuery(BaseModel):
    """
    This object represents an incoming inline query. When the user sends an empty query,
    your bot could return some default or trending results.
    :param id: Unique identifier for this query
    :param from: Sender
    :param query: Text of the query (up to 256 characters)
    :param offset: Offset of the results to be returned, can be controlled by the bot
    :param chat_type: Optional. Type of the chat, from which the inline query was sent. Can be either
    “sender” for a private chat with the inline query sender, “private”, “group”,
    “supergroup”, or “channel”. The chat type should be always known for requests sent
    from official clients and most third-party clients, unless the request was sent from
    a secret chat
    :param location: Optional. Sender location, only for bots that request user location
    """

    id: typing.Optional[str] = Field(default=None)
    from_: typing.Optional["User"] = Field(default=None, alias="from")
    query: typing.Optional[str] = Field(default=None)
    offset: typing.Optional[str] = Field(default=None)
    chat_type: typing.Optional[
        typing.Literal["sender", "private", "group", "supergroup", "channel"]
    ] = Field(default=None)
    location: typing.Optional["Location"] = Field(default=None)


class InlineQueryResult(BaseModel):
    """
    This object represents one result of an inline query. Telegram clients currently
    support results of the following 20 types:  InlineQueryResultCachedAudio
    InlineQueryResultCachedDocument InlineQueryResultCachedGif
    InlineQueryResultCachedMpeg4Gif InlineQueryResultCachedPhoto
    InlineQueryResultCachedSticker InlineQueryResultCachedVideo
    InlineQueryResultCachedVoice InlineQueryResultArticle InlineQueryResultAudio
    InlineQueryResultContact InlineQueryResultGame InlineQueryResultDocument
    InlineQueryResultGif InlineQueryResultLocation InlineQueryResultMpeg4Gif
    InlineQueryResultPhoto InlineQueryResultVenue InlineQueryResultVideo
    InlineQueryResultVoice
    """

    value: typing.Optional[
        typing.Union[
            "InlineQueryResultCachedAudio",
            "InlineQueryResultCachedDocument",
            "InlineQueryResultCachedGif",
            "InlineQueryResultCachedMpeg4Gif",
            "InlineQueryResultCachedPhoto",
            "InlineQueryResultCachedSticker",
            "InlineQueryResultCachedVideo",
            "InlineQueryResultCachedVoice",
            "InlineQueryResultArticle",
            "InlineQueryResultAudio",
            "InlineQueryResultContact",
            "InlineQueryResultGame",
            "InlineQueryResultDocument",
            "InlineQueryResultGif",
            "InlineQueryResultLocation",
            "InlineQueryResultMpeg4Gif",
            "InlineQueryResultPhoto",
            "InlineQueryResultVenue",
            "InlineQueryResultVideo",
            "InlineQueryResultVoice",
        ]
    ] = Field(None)


class InlineQueryResultArticle(BaseModel):
    """
    Represents a link to an article or web page.
    :param type: Type of the result, must be article
    :param id: Unique identifier for this result, 1-64 Bytes
    :param title: Title of the result
    :param input_message_content: Content of the message to be sent
    :param reply_markup: Optional. Inline keyboard attached to the message
    :param url: Optional. URL of the result
    :param hide_url: Optional. Pass True, if you don't want the URL to be shown in the message
    :param description: Optional. Short description of the result
    :param thumb_url: Optional. Url of the thumbnail for the result
    :param thumb_width: Optional. Thumbnail width
    :param thumb_height: Optional. Thumbnail height
    """

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
    """
    Represents a link to a photo. By default, this photo will be sent by the user with
    optional caption. Alternatively, you can use input_message_content to send a message
    with the specified content instead of the photo.
    :param type: Type of the result, must be photo
    :param id: Unique identifier for this result, 1-64 bytes
    :param photo_url: A valid URL of the photo. Photo must be in JPEG format. Photo size must not exceed
    5MB
    :param thumb_url: URL of the thumbnail for the photo
    :param photo_width: Optional. Width of the photo
    :param photo_height: Optional. Height of the photo
    :param title: Optional. Title for the result
    :param description: Optional. Short description of the result
    :param caption: Optional. Caption of the photo to be sent, 0-1024 characters after entities parsing
    :param parse_mode: Optional. Mode for parsing entities in the photo caption. See formatting options for
    more details.
    :param caption_entities: Optional. List of special entities that appear in the caption, which can be
    specified instead of parse_mode
    :param reply_markup: Optional. Inline keyboard attached to the message
    :param input_message_content: Optional. Content of the message to be sent instead of the photo
    """

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
    """
    Represents a link to an animated GIF file. By default, this animated GIF file will
    be sent by the user with optional caption. Alternatively, you can use
    input_message_content to send a message with the specified content instead of the
    animation.
    :param type: Type of the result, must be gif
    :param id: Unique identifier for this result, 1-64 bytes
    :param gif_url: A valid URL for the GIF file. File size must not exceed 1MB
    :param gif_width: Optional. Width of the GIF
    :param gif_height: Optional. Height of the GIF
    :param gif_duration: Optional. Duration of the GIF in seconds
    :param thumb_url: URL of the static (JPEG or GIF) or animated (MPEG4) thumbnail for the result
    :param thumb_mime_type: Optional. MIME type of the thumbnail, must be one of “image/jpeg”, “image/gif”, or
    “video/mp4”. Defaults to “image/jpeg”
    :param title: Optional. Title for the result
    :param caption: Optional. Caption of the GIF file to be sent, 0-1024 characters after entities
    parsing
    :param parse_mode: Optional. Mode for parsing entities in the caption. See formatting options for more
    details.
    :param caption_entities: Optional. List of special entities that appear in the caption, which can be
    specified instead of parse_mode
    :param reply_markup: Optional. Inline keyboard attached to the message
    :param input_message_content: Optional. Content of the message to be sent instead of the GIF animation
    """

    type: typing.Optional[str] = Field(default=None)
    id: typing.Optional[str] = Field(default=None)
    gif_url: typing.Optional[str] = Field(default=None)
    gif_width: typing.Optional[int] = Field(default=None)
    gif_height: typing.Optional[int] = Field(default=None)
    gif_duration: typing.Optional[int] = Field(default=None)
    thumb_url: typing.Optional[str] = Field(default=None)
    thumb_mime_type: typing.Optional[
        typing.Literal["image/jpeg", "image/gif", "video/mp4"]
    ] = Field(default=None)
    title: typing.Optional[str] = Field(default=None)
    caption: typing.Optional[str] = Field(default=None)
    parse_mode: typing.Optional[str] = Field(default=None)
    caption_entities: typing.Optional[typing.List["MessageEntity"]] = Field(
        default=None
    )
    reply_markup: typing.Optional["InlineKeyboardMarkup"] = Field(default=None)
    input_message_content: typing.Optional["InputMessageContent"] = Field(default=None)


class InlineQueryResultMpeg4Gif(BaseModel):
    """
    Represents a link to a video animation (H.264/MPEG-4 AVC video without sound). By
    default, this animated MPEG-4 file will be sent by the user with optional caption.
    Alternatively, you can use input_message_content to send a message with the
    specified content instead of the animation.
    :param type: Type of the result, must be mpeg4_gif
    :param id: Unique identifier for this result, 1-64 bytes
    :param mpeg4_url: A valid URL for the MP4 file. File size must not exceed 1MB
    :param mpeg4_width: Optional. Video width
    :param mpeg4_height: Optional. Video height
    :param mpeg4_duration: Optional. Video duration in seconds
    :param thumb_url: URL of the static (JPEG or GIF) or animated (MPEG4) thumbnail for the result
    :param thumb_mime_type: Optional. MIME type of the thumbnail, must be one of “image/jpeg”, “image/gif”, or
    “video/mp4”. Defaults to “image/jpeg”
    :param title: Optional. Title for the result
    :param caption: Optional. Caption of the MPEG-4 file to be sent, 0-1024 characters after entities
    parsing
    :param parse_mode: Optional. Mode for parsing entities in the caption. See formatting options for more
    details.
    :param caption_entities: Optional. List of special entities that appear in the caption, which can be
    specified instead of parse_mode
    :param reply_markup: Optional. Inline keyboard attached to the message
    :param input_message_content: Optional. Content of the message to be sent instead of the video animation
    """

    type: typing.Optional[str] = Field(default=None)
    id: typing.Optional[str] = Field(default=None)
    mpeg4_url: typing.Optional[str] = Field(default=None)
    mpeg4_width: typing.Optional[int] = Field(default=None)
    mpeg4_height: typing.Optional[int] = Field(default=None)
    mpeg4_duration: typing.Optional[int] = Field(default=None)
    thumb_url: typing.Optional[str] = Field(default=None)
    thumb_mime_type: typing.Optional[
        typing.Literal["image/jpeg", "image/gif", "video/mp4"]
    ] = Field(default=None)
    title: typing.Optional[str] = Field(default=None)
    caption: typing.Optional[str] = Field(default=None)
    parse_mode: typing.Optional[str] = Field(default=None)
    caption_entities: typing.Optional[typing.List["MessageEntity"]] = Field(
        default=None
    )
    reply_markup: typing.Optional["InlineKeyboardMarkup"] = Field(default=None)
    input_message_content: typing.Optional["InputMessageContent"] = Field(default=None)


class InlineQueryResultVideo(BaseModel):
    """
    Represents a link to a page containing an embedded video player or a video file. By
    default, this video file will be sent by the user with an optional caption.
    Alternatively, you can use input_message_content to send a message with the
    specified content instead of the video. If an InlineQueryResultVideo message
    contains an embedded video (e.g., YouTube), you must replace its content using
    input_message_content.
    :param type: Type of the result, must be video
    :param id: Unique identifier for this result, 1-64 bytes
    :param video_url: A valid URL for the embedded video player or video file
    :param mime_type: Mime type of the content of video url, “text/html” or “video/mp4”
    :param thumb_url: URL of the thumbnail (JPEG only) for the video
    :param title: Title for the result
    :param caption: Optional. Caption of the video to be sent, 0-1024 characters after entities parsing
    :param parse_mode: Optional. Mode for parsing entities in the video caption. See formatting options for
    more details.
    :param caption_entities: Optional. List of special entities that appear in the caption, which can be
    specified instead of parse_mode
    :param video_width: Optional. Video width
    :param video_height: Optional. Video height
    :param video_duration: Optional. Video duration in seconds
    :param description: Optional. Short description of the result
    :param reply_markup: Optional. Inline keyboard attached to the message
    :param input_message_content: Optional. Content of the message to be sent instead of the video. This field is
    required if InlineQueryResultVideo is used to send an HTML-page as a result (e.g., a
    YouTube video).
    """

    type: typing.Optional[str] = Field(default=None)
    id: typing.Optional[str] = Field(default=None)
    video_url: typing.Optional[str] = Field(default=None)
    mime_type: typing.Optional[typing.Literal["text/html", "video/mp4"]] = Field(
        default=None
    )
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
    """
    Represents a link to an MP3 audio file. By default, this audio file will be sent by
    the user. Alternatively, you can use input_message_content to send a message with
    the specified content instead of the audio.
    :param type: Type of the result, must be audio
    :param id: Unique identifier for this result, 1-64 bytes
    :param audio_url: A valid URL for the audio file
    :param title: Title
    :param caption: Optional. Caption, 0-1024 characters after entities parsing
    :param parse_mode: Optional. Mode for parsing entities in the audio caption. See formatting options for
    more details.
    :param caption_entities: Optional. List of special entities that appear in the caption, which can be
    specified instead of parse_mode
    :param performer: Optional. Performer
    :param audio_duration: Optional. Audio duration in seconds
    :param reply_markup: Optional. Inline keyboard attached to the message
    :param input_message_content: Optional. Content of the message to be sent instead of the audio
    """

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
    """
    Represents a link to a voice recording in an .OGG container encoded with OPUS. By
    default, this voice recording will be sent by the user. Alternatively, you can use
    input_message_content to send a message with the specified content instead of the
    the voice message.
    :param type: Type of the result, must be voice
    :param id: Unique identifier for this result, 1-64 bytes
    :param voice_url: A valid URL for the voice recording
    :param title: Recording title
    :param caption: Optional. Caption, 0-1024 characters after entities parsing
    :param parse_mode: Optional. Mode for parsing entities in the voice message caption. See formatting
    options for more details.
    :param caption_entities: Optional. List of special entities that appear in the caption, which can be
    specified instead of parse_mode
    :param voice_duration: Optional. Recording duration in seconds
    :param reply_markup: Optional. Inline keyboard attached to the message
    :param input_message_content: Optional. Content of the message to be sent instead of the voice recording
    """

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
    """
    Represents a link to a file. By default, this file will be sent by the user with an
    optional caption. Alternatively, you can use input_message_content to send a message
    with the specified content instead of the file. Currently, only .PDF and .ZIP files
    can be sent using this method.
    :param type: Type of the result, must be document
    :param id: Unique identifier for this result, 1-64 bytes
    :param title: Title for the result
    :param caption: Optional. Caption of the document to be sent, 0-1024 characters after entities
    parsing
    :param parse_mode: Optional. Mode for parsing entities in the document caption. See formatting options
    for more details.
    :param caption_entities: Optional. List of special entities that appear in the caption, which can be
    specified instead of parse_mode
    :param document_url: A valid URL for the file
    :param mime_type: Mime type of the content of the file, either “application/pdf” or “application/zip”
    :param description: Optional. Short description of the result
    :param reply_markup: Optional. Inline keyboard attached to the message
    :param input_message_content: Optional. Content of the message to be sent instead of the file
    :param thumb_url: Optional. URL of the thumbnail (JPEG only) for the file
    :param thumb_width: Optional. Thumbnail width
    :param thumb_height: Optional. Thumbnail height
    """

    type: typing.Optional[str] = Field(default=None)
    id: typing.Optional[str] = Field(default=None)
    title: typing.Optional[str] = Field(default=None)
    caption: typing.Optional[str] = Field(default=None)
    parse_mode: typing.Optional[str] = Field(default=None)
    caption_entities: typing.Optional[typing.List["MessageEntity"]] = Field(
        default=None
    )
    document_url: typing.Optional[str] = Field(default=None)
    mime_type: typing.Optional[
        typing.Literal["application/pdf", "application/zip"]
    ] = Field(default=None)
    description: typing.Optional[str] = Field(default=None)
    reply_markup: typing.Optional["InlineKeyboardMarkup"] = Field(default=None)
    input_message_content: typing.Optional["InputMessageContent"] = Field(default=None)
    thumb_url: typing.Optional[str] = Field(default=None)
    thumb_width: typing.Optional[int] = Field(default=None)
    thumb_height: typing.Optional[int] = Field(default=None)


class InlineQueryResultLocation(BaseModel):
    """
    Represents a location on a map. By default, the location will be sent by the user.
    Alternatively, you can use input_message_content to send a message with the
    specified content instead of the location.
    :param type: Type of the result, must be location
    :param id: Unique identifier for this result, 1-64 Bytes
    :param latitude: Location latitude in degrees
    :param longitude: Location longitude in degrees
    :param title: Location title
    :param horizontal_accuracy: Optional. The radius of uncertainty for the location, measured in meters; 0-1500
    :param live_period: Optional. Period in seconds for which the location can be updated, should be between
    60 and 86400.
    :param heading: Optional. For live locations, a direction in which the user is moving, in degrees.
    Must be between 1 and 360 if specified.
    :param proximity_alert_radius: Optional. For live locations, a maximum distance for proximity alerts about
    approaching another chat member, in meters. Must be between 1 and 100000 if
    specified.
    :param reply_markup: Optional. Inline keyboard attached to the message
    :param input_message_content: Optional. Content of the message to be sent instead of the location
    :param thumb_url: Optional. Url of the thumbnail for the result
    :param thumb_width: Optional. Thumbnail width
    :param thumb_height: Optional. Thumbnail height
    """

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
    """
    Represents a venue. By default, the venue will be sent by the user. Alternatively,
    you can use input_message_content to send a message with the specified content
    instead of the venue.
    :param type: Type of the result, must be venue
    :param id: Unique identifier for this result, 1-64 Bytes
    :param latitude: Latitude of the venue location in degrees
    :param longitude: Longitude of the venue location in degrees
    :param title: Title of the venue
    :param address: Address of the venue
    :param foursquare_id: Optional. Foursquare identifier of the venue if known
    :param foursquare_type: Optional. Foursquare type of the venue, if known. (For example,
    “arts_entertainment/default”, “arts_entertainment/aquarium” or “food/icecream”.)
    :param google_place_id: Optional. Google Places identifier of the venue
    :param google_place_type: Optional. Google Places type of the venue. (See supported types.)
    :param reply_markup: Optional. Inline keyboard attached to the message
    :param input_message_content: Optional. Content of the message to be sent instead of the venue
    :param thumb_url: Optional. Url of the thumbnail for the result
    :param thumb_width: Optional. Thumbnail width
    :param thumb_height: Optional. Thumbnail height
    """

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
    """
    Represents a contact with a phone number. By default, this contact will be sent by
    the user. Alternatively, you can use input_message_content to send a message with
    the specified content instead of the contact.
    :param type: Type of the result, must be contact
    :param id: Unique identifier for this result, 1-64 Bytes
    :param phone_number: Contact's phone number
    :param first_name: Contact's first name
    :param last_name: Optional. Contact's last name
    :param vcard: Optional. Additional data about the contact in the form of a vCard, 0-2048 bytes
    :param reply_markup: Optional. Inline keyboard attached to the message
    :param input_message_content: Optional. Content of the message to be sent instead of the contact
    :param thumb_url: Optional. Url of the thumbnail for the result
    :param thumb_width: Optional. Thumbnail width
    :param thumb_height: Optional. Thumbnail height
    """

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
    """
    Represents a Game.
    :param type: Type of the result, must be game
    :param id: Unique identifier for this result, 1-64 bytes
    :param game_short_name: Short name of the game
    :param reply_markup: Optional. Inline keyboard attached to the message
    """

    type: typing.Optional[str] = Field(default=None)
    id: typing.Optional[str] = Field(default=None)
    game_short_name: typing.Optional[str] = Field(default=None)
    reply_markup: typing.Optional["InlineKeyboardMarkup"] = Field(default=None)


class InlineQueryResultCachedPhoto(BaseModel):
    """
    Represents a link to a photo stored on the Telegram servers. By default, this photo
    will be sent by the user with an optional caption. Alternatively, you can use
    input_message_content to send a message with the specified content instead of the
    photo.
    :param type: Type of the result, must be photo
    :param id: Unique identifier for this result, 1-64 bytes
    :param photo_file_id: A valid file identifier of the photo
    :param title: Optional. Title for the result
    :param description: Optional. Short description of the result
    :param caption: Optional. Caption of the photo to be sent, 0-1024 characters after entities parsing
    :param parse_mode: Optional. Mode for parsing entities in the photo caption. See formatting options for
    more details.
    :param caption_entities: Optional. List of special entities that appear in the caption, which can be
    specified instead of parse_mode
    :param reply_markup: Optional. Inline keyboard attached to the message
    :param input_message_content: Optional. Content of the message to be sent instead of the photo
    """

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
    """
    Represents a link to an animated GIF file stored on the Telegram servers. By
    default, this animated GIF file will be sent by the user with an optional caption.
    Alternatively, you can use input_message_content to send a message with specified
    content instead of the animation.
    :param type: Type of the result, must be gif
    :param id: Unique identifier for this result, 1-64 bytes
    :param gif_file_id: A valid file identifier for the GIF file
    :param title: Optional. Title for the result
    :param caption: Optional. Caption of the GIF file to be sent, 0-1024 characters after entities
    parsing
    :param parse_mode: Optional. Mode for parsing entities in the caption. See formatting options for more
    details.
    :param caption_entities: Optional. List of special entities that appear in the caption, which can be
    specified instead of parse_mode
    :param reply_markup: Optional. Inline keyboard attached to the message
    :param input_message_content: Optional. Content of the message to be sent instead of the GIF animation
    """

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
    """
    Represents a link to a video animation (H.264/MPEG-4 AVC video without sound) stored
    on the Telegram servers. By default, this animated MPEG-4 file will be sent by the
    user with an optional caption. Alternatively, you can use input_message_content to
    send a message with the specified content instead of the animation.
    :param type: Type of the result, must be mpeg4_gif
    :param id: Unique identifier for this result, 1-64 bytes
    :param mpeg4_file_id: A valid file identifier for the MP4 file
    :param title: Optional. Title for the result
    :param caption: Optional. Caption of the MPEG-4 file to be sent, 0-1024 characters after entities
    parsing
    :param parse_mode: Optional. Mode for parsing entities in the caption. See formatting options for more
    details.
    :param caption_entities: Optional. List of special entities that appear in the caption, which can be
    specified instead of parse_mode
    :param reply_markup: Optional. Inline keyboard attached to the message
    :param input_message_content: Optional. Content of the message to be sent instead of the video animation
    """

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
    """
    Represents a link to a sticker stored on the Telegram servers. By default, this
    sticker will be sent by the user. Alternatively, you can use input_message_content
    to send a message with the specified content instead of the sticker.
    :param type: Type of the result, must be sticker
    :param id: Unique identifier for this result, 1-64 bytes
    :param sticker_file_id: A valid file identifier of the sticker
    :param reply_markup: Optional. Inline keyboard attached to the message
    :param input_message_content: Optional. Content of the message to be sent instead of the sticker
    """

    type: typing.Optional[str] = Field(default=None)
    id: typing.Optional[str] = Field(default=None)
    sticker_file_id: typing.Optional[str] = Field(default=None)
    reply_markup: typing.Optional["InlineKeyboardMarkup"] = Field(default=None)
    input_message_content: typing.Optional["InputMessageContent"] = Field(default=None)


class InlineQueryResultCachedDocument(BaseModel):
    """
    Represents a link to a file stored on the Telegram servers. By default, this file
    will be sent by the user with an optional caption. Alternatively, you can use
    input_message_content to send a message with the specified content instead of the
    file.
    :param type: Type of the result, must be document
    :param id: Unique identifier for this result, 1-64 bytes
    :param title: Title for the result
    :param document_file_id: A valid file identifier for the file
    :param description: Optional. Short description of the result
    :param caption: Optional. Caption of the document to be sent, 0-1024 characters after entities
    parsing
    :param parse_mode: Optional. Mode for parsing entities in the document caption. See formatting options
    for more details.
    :param caption_entities: Optional. List of special entities that appear in the caption, which can be
    specified instead of parse_mode
    :param reply_markup: Optional. Inline keyboard attached to the message
    :param input_message_content: Optional. Content of the message to be sent instead of the file
    """

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
    """
    Represents a link to a video file stored on the Telegram servers. By default, this
    video file will be sent by the user with an optional caption. Alternatively, you can
    use input_message_content to send a message with the specified content instead of
    the video.
    :param type: Type of the result, must be video
    :param id: Unique identifier for this result, 1-64 bytes
    :param video_file_id: A valid file identifier for the video file
    :param title: Title for the result
    :param description: Optional. Short description of the result
    :param caption: Optional. Caption of the video to be sent, 0-1024 characters after entities parsing
    :param parse_mode: Optional. Mode for parsing entities in the video caption. See formatting options for
    more details.
    :param caption_entities: Optional. List of special entities that appear in the caption, which can be
    specified instead of parse_mode
    :param reply_markup: Optional. Inline keyboard attached to the message
    :param input_message_content: Optional. Content of the message to be sent instead of the video
    """

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
    """
    Represents a link to a voice message stored on the Telegram servers. By default,
    this voice message will be sent by the user. Alternatively, you can use
    input_message_content to send a message with the specified content instead of the
    voice message.
    :param type: Type of the result, must be voice
    :param id: Unique identifier for this result, 1-64 bytes
    :param voice_file_id: A valid file identifier for the voice message
    :param title: Voice message title
    :param caption: Optional. Caption, 0-1024 characters after entities parsing
    :param parse_mode: Optional. Mode for parsing entities in the voice message caption. See formatting
    options for more details.
    :param caption_entities: Optional. List of special entities that appear in the caption, which can be
    specified instead of parse_mode
    :param reply_markup: Optional. Inline keyboard attached to the message
    :param input_message_content: Optional. Content of the message to be sent instead of the voice message
    """

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
    """
    Represents a link to an MP3 audio file stored on the Telegram servers. By default,
    this audio file will be sent by the user. Alternatively, you can use
    input_message_content to send a message with the specified content instead of the
    audio.
    :param type: Type of the result, must be audio
    :param id: Unique identifier for this result, 1-64 bytes
    :param audio_file_id: A valid file identifier for the audio file
    :param caption: Optional. Caption, 0-1024 characters after entities parsing
    :param parse_mode: Optional. Mode for parsing entities in the audio caption. See formatting options for
    more details.
    :param caption_entities: Optional. List of special entities that appear in the caption, which can be
    specified instead of parse_mode
    :param reply_markup: Optional. Inline keyboard attached to the message
    :param input_message_content: Optional. Content of the message to be sent instead of the audio
    """

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
    """
    This object represents the content of a message to be sent as a result of an inline
    query. Telegram clients currently support the following 5 types:
    InputTextMessageContent InputLocationMessageContent InputVenueMessageContent
    InputContactMessageContent InputInvoiceMessageContent
    """

    value: typing.Optional[
        typing.Union[
            "InputTextMessageContent",
            "InputLocationMessageContent",
            "InputVenueMessageContent",
            "InputContactMessageContent",
            "InputInvoiceMessageContent",
        ]
    ] = Field(None)


class InputTextMessageContent(BaseModel):
    """
    Represents the content of a text message to be sent as the result of an inline
    query.
    :param message_text: Text of the message to be sent, 1-4096 characters
    :param parse_mode: Optional. Mode for parsing entities in the message text. See formatting options for
    more details.
    :param entities: Optional. List of special entities that appear in message text, which can be
    specified instead of parse_mode
    :param disable_web_page_preview: Optional. Disables link previews for links in the sent message
    """

    message_text: typing.Optional[str] = Field(default=None)
    parse_mode: typing.Optional[str] = Field(default=None)
    entities: typing.Optional[typing.List["MessageEntity"]] = Field(default=None)
    disable_web_page_preview: typing.Optional[bool] = Field(default=None)


class InputLocationMessageContent(BaseModel):
    """
    Represents the content of a location message to be sent as the result of an inline
    query.
    :param latitude: Latitude of the location in degrees
    :param longitude: Longitude of the location in degrees
    :param horizontal_accuracy: Optional. The radius of uncertainty for the location, measured in meters; 0-1500
    :param live_period: Optional. Period in seconds for which the location can be updated, should be between
    60 and 86400.
    :param heading: Optional. For live locations, a direction in which the user is moving, in degrees.
    Must be between 1 and 360 if specified.
    :param proximity_alert_radius: Optional. For live locations, a maximum distance for proximity alerts about
    approaching another chat member, in meters. Must be between 1 and 100000 if
    specified.
    """

    latitude: typing.Optional[float] = Field(default=None)
    longitude: typing.Optional[float] = Field(default=None)
    horizontal_accuracy: typing.Optional[float] = Field(default=None)
    live_period: typing.Optional[int] = Field(default=None)
    heading: typing.Optional[int] = Field(default=None)
    proximity_alert_radius: typing.Optional[int] = Field(default=None)


class InputVenueMessageContent(BaseModel):
    """
    Represents the content of a venue message to be sent as the result of an inline
    query.
    :param latitude: Latitude of the venue in degrees
    :param longitude: Longitude of the venue in degrees
    :param title: Name of the venue
    :param address: Address of the venue
    :param foursquare_id: Optional. Foursquare identifier of the venue, if known
    :param foursquare_type: Optional. Foursquare type of the venue, if known. (For example,
    “arts_entertainment/default”, “arts_entertainment/aquarium” or “food/icecream”.)
    :param google_place_id: Optional. Google Places identifier of the venue
    :param google_place_type: Optional. Google Places type of the venue. (See supported types.)
    """

    latitude: typing.Optional[float] = Field(default=None)
    longitude: typing.Optional[float] = Field(default=None)
    title: typing.Optional[str] = Field(default=None)
    address: typing.Optional[str] = Field(default=None)
    foursquare_id: typing.Optional[str] = Field(default=None)
    foursquare_type: typing.Optional[str] = Field(default=None)
    google_place_id: typing.Optional[str] = Field(default=None)
    google_place_type: typing.Optional[str] = Field(default=None)


class InputContactMessageContent(BaseModel):
    """
    Represents the content of a contact message to be sent as the result of an inline
    query.
    :param phone_number: Contact's phone number
    :param first_name: Contact's first name
    :param last_name: Optional. Contact's last name
    :param vcard: Optional. Additional data about the contact in the form of a vCard, 0-2048 bytes
    """

    phone_number: typing.Optional[str] = Field(default=None)
    first_name: typing.Optional[str] = Field(default=None)
    last_name: typing.Optional[str] = Field(default=None)
    vcard: typing.Optional[str] = Field(default=None)


class InputInvoiceMessageContent(BaseModel):
    """
    Represents the content of an invoice message to be sent as the result of an inline
    query.
    :param title: Product name, 1-32 characters
    :param description: Product description, 1-255 characters
    :param payload: Bot-defined invoice payload, 1-128 bytes. This will not be displayed to the user,
    use for your internal processes.
    :param provider_token: Payment provider token, obtained via Botfather
    :param currency: Three-letter ISO 4217 currency code, see more on currencies
    :param prices: Price breakdown, a JSON-serialized list of components (e.g. product price, tax,
    discount, delivery cost, delivery tax, bonus, etc.)
    :param max_tip_amount: Optional. The maximum accepted amount for tips in the smallest units of the currency
    (integer, not float/double). For example, for a maximum tip of US$ 1.45 pass
    max_tip_amount = 145. See the exp parameter in currencies.json, it shows the number
    of digits past the decimal point for each currency (2 for the majority of
    currencies). Defaults to 0
    :param suggested_tip_amounts: Optional. A JSON-serialized array of suggested amounts of tip in the smallest units
    of the currency (integer, not float/double). At most 4 suggested tip amounts can be
    specified. The suggested tip amounts must be positive, passed in a strictly
    increased order and must not exceed max_tip_amount.
    :param provider_data: Optional. A JSON-serialized object for data about the invoice, which will be shared
    with the payment provider. A detailed description of the required fields should be
    provided by the payment provider.
    :param photo_url: Optional. URL of the product photo for the invoice. Can be a photo of the goods or a
    marketing image for a service. People like it better when they see what they are
    paying for.
    :param photo_size: Optional. Photo size
    :param photo_width: Optional. Photo width
    :param photo_height: Optional. Photo height
    :param need_name: Optional. Pass True, if you require the user's full name to complete the order
    :param need_phone_number: Optional. Pass True, if you require the user's phone number to complete the order
    :param need_email: Optional. Pass True, if you require the user's email address to complete the order
    :param need_shipping_address: Optional. Pass True, if you require the user's shipping address to complete the
    order
    :param send_phone_number_to_provider: Optional. Pass True, if user's phone number should be sent to provider
    :param send_email_to_provider: Optional. Pass True, if user's email address should be sent to provider
    :param is_flexible: Optional. Pass True, if the final price depends on the shipping method
    """

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
    """
    Represents a result of an inline query that was chosen by the user and sent to their
    chat partner.
    :param result_id: The unique identifier for the result that was chosen
    :param from: The user that chose the result
    :param location: Optional. Sender location, only for bots that require user location
    :param inline_message_id: Optional. Identifier of the sent inline message. Available only if there is an
    inline keyboard attached to the message. Will be also received in callback queries
    and can be used to edit the message.
    :param query: The query that was used to obtain the result
    """

    result_id: typing.Optional[str] = Field(default=None)
    from_: typing.Optional["User"] = Field(default=None, alias="from")
    location: typing.Optional["Location"] = Field(default=None)
    inline_message_id: typing.Optional[str] = Field(default=None)
    query: typing.Optional[str] = Field(default=None)


class SentWebAppMessage(BaseModel):
    """
    Contains information about an inline message sent by a Web App on behalf of a user.
    :param inline_message_id: Optional. Identifier of the sent inline message. Available only if there is an
    inline keyboard attached to the message.
    """

    inline_message_id: typing.Optional[str] = Field(default=None)


class LabeledPrice(BaseModel):
    """
    This object represents a portion of the price for goods or services.
    :param label: Portion label
    :param amount: Price of the product in the smallest units of the currency (integer, not
    float/double). For example, for a price of US$ 1.45 pass amount = 145. See the exp
    parameter in currencies.json, it shows the number of digits past the decimal point
    for each currency (2 for the majority of currencies).
    """

    label: typing.Optional[str] = Field(default=None)
    amount: typing.Optional[int] = Field(default=None)


class Invoice(BaseModel):
    """
    This object contains basic information about an invoice.
    :param title: Product name
    :param description: Product description
    :param start_parameter: Unique bot deep-linking parameter that can be used to generate this invoice
    :param currency: Three-letter ISO 4217 currency code
    :param total_amount: Total price in the smallest units of the currency (integer, not float/double). For
    example, for a price of US$ 1.45 pass amount = 145. See the exp parameter in
    currencies.json, it shows the number of digits past the decimal point for each
    currency (2 for the majority of currencies).
    """

    title: typing.Optional[str] = Field(default=None)
    description: typing.Optional[str] = Field(default=None)
    start_parameter: typing.Optional[str] = Field(default=None)
    currency: typing.Optional[str] = Field(default=None)
    total_amount: typing.Optional[int] = Field(default=None)


class ShippingAddress(BaseModel):
    """
    This object represents a shipping address.
    :param country_code: ISO 3166-1 alpha-2 country code
    :param state: State, if applicable
    :param city: City
    :param street_line1: First line for the address
    :param street_line2: Second line for the address
    :param post_code: Address post code
    """

    country_code: typing.Optional[str] = Field(default=None)
    state: typing.Optional[str] = Field(default=None)
    city: typing.Optional[str] = Field(default=None)
    street_line1: typing.Optional[str] = Field(default=None)
    street_line2: typing.Optional[str] = Field(default=None)
    post_code: typing.Optional[str] = Field(default=None)


class OrderInfo(BaseModel):
    """
    This object represents information about an order.
    :param name: Optional. User name
    :param phone_number: Optional. User's phone number
    :param email: Optional. User email
    :param shipping_address: Optional. User shipping address
    """

    name: typing.Optional[str] = Field(default=None)
    phone_number: typing.Optional[str] = Field(default=None)
    email: typing.Optional[str] = Field(default=None)
    shipping_address: typing.Optional["ShippingAddress"] = Field(default=None)


class ShippingOption(BaseModel):
    """
    This object represents one shipping option.
    :param id: Shipping option identifier
    :param title: Option title
    :param prices: List of price portions
    """

    id: typing.Optional[str] = Field(default=None)
    title: typing.Optional[str] = Field(default=None)
    prices: typing.Optional[typing.List["LabeledPrice"]] = Field(default=None)


class SuccessfulPayment(BaseModel):
    """
    This object contains basic information about a successful payment.
    :param currency: Three-letter ISO 4217 currency code
    :param total_amount: Total price in the smallest units of the currency (integer, not float/double). For
    example, for a price of US$ 1.45 pass amount = 145. See the exp parameter in
    currencies.json, it shows the number of digits past the decimal point for each
    currency (2 for the majority of currencies).
    :param invoice_payload: Bot specified invoice payload
    :param shipping_option_id: Optional. Identifier of the shipping option chosen by the user
    :param order_info: Optional. Order info provided by the user
    :param telegram_payment_charge_id: Telegram payment identifier
    :param provider_payment_charge_id: Provider payment identifier
    """

    currency: typing.Optional[str] = Field(default=None)
    total_amount: typing.Optional[int] = Field(default=None)
    invoice_payload: typing.Optional[str] = Field(default=None)
    shipping_option_id: typing.Optional[str] = Field(default=None)
    order_info: typing.Optional["OrderInfo"] = Field(default=None)
    telegram_payment_charge_id: typing.Optional[str] = Field(default=None)
    provider_payment_charge_id: typing.Optional[str] = Field(default=None)


class ShippingQuery(BaseModel):
    """
    This object contains information about an incoming shipping query.
    :param id: Unique query identifier
    :param from: User who sent the query
    :param invoice_payload: Bot specified invoice payload
    :param shipping_address: User specified shipping address
    """

    id: typing.Optional[str] = Field(default=None)
    from_: typing.Optional["User"] = Field(default=None, alias="from")
    invoice_payload: typing.Optional[str] = Field(default=None)
    shipping_address: typing.Optional["ShippingAddress"] = Field(default=None)


class PreCheckoutQuery(BaseModel):
    """
    This object contains information about an incoming pre-checkout query.
    :param id: Unique query identifier
    :param from: User who sent the query
    :param currency: Three-letter ISO 4217 currency code
    :param total_amount: Total price in the smallest units of the currency (integer, not float/double). For
    example, for a price of US$ 1.45 pass amount = 145. See the exp parameter in
    currencies.json, it shows the number of digits past the decimal point for each
    currency (2 for the majority of currencies).
    :param invoice_payload: Bot specified invoice payload
    :param shipping_option_id: Optional. Identifier of the shipping option chosen by the user
    :param order_info: Optional. Order info provided by the user
    """

    id: typing.Optional[str] = Field(default=None)
    from_: typing.Optional["User"] = Field(default=None, alias="from")
    currency: typing.Optional[str] = Field(default=None)
    total_amount: typing.Optional[int] = Field(default=None)
    invoice_payload: typing.Optional[str] = Field(default=None)
    shipping_option_id: typing.Optional[str] = Field(default=None)
    order_info: typing.Optional["OrderInfo"] = Field(default=None)


class PassportData(BaseModel):
    """
    Contains information about Telegram Passport data shared with the bot by the user.
    :param data: Array with information about documents and other Telegram Passport elements that was
    shared with the bot
    :param credentials: Encrypted credentials required to decrypt the data
    """

    data: typing.Optional[typing.List["EncryptedPassportElement"]] = Field(default=None)
    credentials: typing.Optional["EncryptedCredentials"] = Field(default=None)


class PassportFile(BaseModel):
    """
    This object represents a file uploaded to Telegram Passport. Currently all Telegram
    Passport files are in JPEG format when decrypted and don't exceed 10MB.
    :param file_id: Identifier for this file, which can be used to download or reuse the file
    :param file_unique_id: Unique identifier for this file, which is supposed to be the same over time and for
    different bots. Can't be used to download or reuse the file.
    :param file_size: File size in bytes
    :param file_date: Unix time when the file was uploaded
    """

    file_id: typing.Optional[str] = Field(default=None)
    file_unique_id: typing.Optional[str] = Field(default=None)
    file_size: typing.Optional[int] = Field(default=None)
    file_date: typing.Optional[int] = Field(default=None)


class EncryptedPassportElement(BaseModel):
    """
    Contains information about documents or other Telegram Passport elements shared with
    the bot by the user.
    :param type: Element type. One of “personal_details”, “passport”, “driver_license”,
    “identity_card”, “internal_passport”, “address”, “utility_bill”, “bank_statement”,
    “rental_agreement”, “passport_registration”, “temporary_registration”,
    “phone_number”, “email”.
    :param data: Optional. Base64-encoded encrypted Telegram Passport element data provided by the
    user, available for “personal_details”, “passport”, “driver_license”,
    “identity_card”, “internal_passport” and “address” types. Can be decrypted and
    verified using the accompanying EncryptedCredentials.
    :param phone_number: Optional. User's verified phone number, available only for “phone_number” type
    :param email: Optional. User's verified email address, available only for “email” type
    :param files: Optional. Array of encrypted files with documents provided by the user, available
    for “utility_bill”, “bank_statement”, “rental_agreement”, “passport_registration”
    and “temporary_registration” types. Files can be decrypted and verified using the
    accompanying EncryptedCredentials.
    :param front_side: Optional. Encrypted file with the front side of the document, provided by the user.
    Available for “passport”, “driver_license”, “identity_card” and “internal_passport”.
    The file can be decrypted and verified using the accompanying EncryptedCredentials.
    :param reverse_side: Optional. Encrypted file with the reverse side of the document, provided by the
    user. Available for “driver_license” and “identity_card”. The file can be decrypted
    and verified using the accompanying EncryptedCredentials.
    :param selfie: Optional. Encrypted file with the selfie of the user holding a document, provided by
    the user; available for “passport”, “driver_license”, “identity_card” and
    “internal_passport”. The file can be decrypted and verified using the accompanying
    EncryptedCredentials.
    :param translation: Optional. Array of encrypted files with translated versions of documents provided by
    the user. Available if requested for “passport”, “driver_license”, “identity_card”,
    “internal_passport”, “utility_bill”, “bank_statement”, “rental_agreement”,
    “passport_registration” and “temporary_registration” types. Files can be decrypted
    and verified using the accompanying EncryptedCredentials.
    :param hash: Base64-encoded element hash for using in PassportElementErrorUnspecified
    """

    type: typing.Optional[
        typing.Literal[
            "personal_details",
            "passport",
            "driver_license",
            "identity_card",
            "internal_passport",
            "address",
            "utility_bill",
            "bank_statement",
            "rental_agreement",
            "passport_registration",
            "temporary_registration",
            "phone_number",
            "email",
        ]
    ] = Field(default=None)
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
    """
    Contains data required for decrypting and authenticating EncryptedPassportElement.
    See the Telegram Passport Documentation for a complete description of the data
    decryption and authentication processes.
    :param data: Base64-encoded encrypted JSON-serialized data with unique user's payload, data
    hashes and secrets required for EncryptedPassportElement decryption and
    authentication
    :param hash: Base64-encoded data hash for data authentication
    :param secret: Base64-encoded secret, encrypted with the bot's public RSA key, required for data
    decryption
    """

    data: typing.Optional[str] = Field(default=None)
    hash: typing.Optional[str] = Field(default=None)
    secret: typing.Optional[str] = Field(default=None)


class PassportElementError(BaseModel):
    """
    This object represents an error in the Telegram Passport element which was submitted
    that should be resolved by the user. It should be one of:
    PassportElementErrorDataField PassportElementErrorFrontSide
    PassportElementErrorReverseSide PassportElementErrorSelfie PassportElementErrorFile
    PassportElementErrorFiles PassportElementErrorTranslationFile
    PassportElementErrorTranslationFiles PassportElementErrorUnspecified
    """

    value: typing.Optional[
        typing.Union[
            "PassportElementErrorDataField",
            "PassportElementErrorFrontSide",
            "PassportElementErrorReverseSide",
            "PassportElementErrorSelfie",
            "PassportElementErrorFile",
            "PassportElementErrorFiles",
            "PassportElementErrorTranslationFile",
            "PassportElementErrorTranslationFiles",
            "PassportElementErrorUnspecified",
        ]
    ] = Field(None)


class PassportElementErrorDataField(BaseModel):
    """
    Represents an issue in one of the data fields that was provided by the user. The
    error is considered resolved when the field's value changes.
    :param source: Error source, must be data
    :param type: The section of the user's Telegram Passport which has the error, one of
    “personal_details”, “passport”, “driver_license”, “identity_card”,
    “internal_passport”, “address”
    :param field_name: Name of the data field which has the error
    :param data_hash: Base64-encoded data hash
    :param message: Error message
    """

    source: typing.Optional[str] = Field(default=None)
    type: typing.Optional[
        typing.Literal[
            "personal_details",
            "passport",
            "driver_license",
            "identity_card",
            "internal_passport",
            "address",
        ]
    ] = Field(default=None)
    field_name: typing.Optional[str] = Field(default=None)
    data_hash: typing.Optional[str] = Field(default=None)
    message: typing.Optional[str] = Field(default=None)


class PassportElementErrorFrontSide(BaseModel):
    """
    Represents an issue with the front side of a document. The error is considered
    resolved when the file with the front side of the document changes.
    :param source: Error source, must be front_side
    :param type: The section of the user's Telegram Passport which has the issue, one of “passport”,
    “driver_license”, “identity_card”, “internal_passport”
    :param file_hash: Base64-encoded hash of the file with the front side of the document
    :param message: Error message
    """

    source: typing.Optional[str] = Field(default=None)
    type: typing.Optional[
        typing.Literal[
            "passport", "driver_license", "identity_card", "internal_passport"
        ]
    ] = Field(default=None)
    file_hash: typing.Optional[str] = Field(default=None)
    message: typing.Optional[str] = Field(default=None)


class PassportElementErrorReverseSide(BaseModel):
    """
    Represents an issue with the reverse side of a document. The error is considered
    resolved when the file with reverse side of the document changes.
    :param source: Error source, must be reverse_side
    :param type: The section of the user's Telegram Passport which has the issue, one of
    “driver_license”, “identity_card”
    :param file_hash: Base64-encoded hash of the file with the reverse side of the document
    :param message: Error message
    """

    source: typing.Optional[str] = Field(default=None)
    type: typing.Optional[typing.Literal["driver_license", "identity_card"]] = Field(
        default=None
    )
    file_hash: typing.Optional[str] = Field(default=None)
    message: typing.Optional[str] = Field(default=None)


class PassportElementErrorSelfie(BaseModel):
    """
    Represents an issue with the selfie with a document. The error is considered
    resolved when the file with the selfie changes.
    :param source: Error source, must be selfie
    :param type: The section of the user's Telegram Passport which has the issue, one of “passport”,
    “driver_license”, “identity_card”, “internal_passport”
    :param file_hash: Base64-encoded hash of the file with the selfie
    :param message: Error message
    """

    source: typing.Optional[str] = Field(default=None)
    type: typing.Optional[
        typing.Literal[
            "passport", "driver_license", "identity_card", "internal_passport"
        ]
    ] = Field(default=None)
    file_hash: typing.Optional[str] = Field(default=None)
    message: typing.Optional[str] = Field(default=None)


class PassportElementErrorFile(BaseModel):
    """
    Represents an issue with a document scan. The error is considered resolved when the
    file with the document scan changes.
    :param source: Error source, must be file
    :param type: The section of the user's Telegram Passport which has the issue, one of
    “utility_bill”, “bank_statement”, “rental_agreement”, “passport_registration”,
    “temporary_registration”
    :param file_hash: Base64-encoded file hash
    :param message: Error message
    """

    source: typing.Optional[str] = Field(default=None)
    type: typing.Optional[
        typing.Literal[
            "utility_bill",
            "bank_statement",
            "rental_agreement",
            "passport_registration",
            "temporary_registration",
        ]
    ] = Field(default=None)
    file_hash: typing.Optional[str] = Field(default=None)
    message: typing.Optional[str] = Field(default=None)


class PassportElementErrorFiles(BaseModel):
    """
    Represents an issue with a list of scans. The error is considered resolved when the
    list of files containing the scans changes.
    :param source: Error source, must be files
    :param type: The section of the user's Telegram Passport which has the issue, one of
    “utility_bill”, “bank_statement”, “rental_agreement”, “passport_registration”,
    “temporary_registration”
    :param file_hashes: List of base64-encoded file hashes
    :param message: Error message
    """

    source: typing.Optional[str] = Field(default=None)
    type: typing.Optional[
        typing.Literal[
            "utility_bill",
            "bank_statement",
            "rental_agreement",
            "passport_registration",
            "temporary_registration",
        ]
    ] = Field(default=None)
    file_hashes: typing.Optional[typing.List[str]] = Field(default=None)
    message: typing.Optional[str] = Field(default=None)


class PassportElementErrorTranslationFile(BaseModel):
    """
    Represents an issue with one of the files that constitute the translation of a
    document. The error is considered resolved when the file changes.
    :param source: Error source, must be translation_file
    :param type: Type of element of the user's Telegram Passport which has the issue, one of
    “passport”, “driver_license”, “identity_card”, “internal_passport”, “utility_bill”,
    “bank_statement”, “rental_agreement”, “passport_registration”,
    “temporary_registration”
    :param file_hash: Base64-encoded file hash
    :param message: Error message
    """

    source: typing.Optional[str] = Field(default=None)
    type: typing.Optional[
        typing.Literal[
            "passport",
            "driver_license",
            "identity_card",
            "internal_passport",
            "utility_bill",
            "bank_statement",
            "rental_agreement",
            "passport_registration",
            "temporary_registration",
        ]
    ] = Field(default=None)
    file_hash: typing.Optional[str] = Field(default=None)
    message: typing.Optional[str] = Field(default=None)


class PassportElementErrorTranslationFiles(BaseModel):
    """
    Represents an issue with the translated version of a document. The error is
    considered resolved when a file with the document translation change.
    :param source: Error source, must be translation_files
    :param type: Type of element of the user's Telegram Passport which has the issue, one of
    “passport”, “driver_license”, “identity_card”, “internal_passport”, “utility_bill”,
    “bank_statement”, “rental_agreement”, “passport_registration”,
    “temporary_registration”
    :param file_hashes: List of base64-encoded file hashes
    :param message: Error message
    """

    source: typing.Optional[str] = Field(default=None)
    type: typing.Optional[
        typing.Literal[
            "passport",
            "driver_license",
            "identity_card",
            "internal_passport",
            "utility_bill",
            "bank_statement",
            "rental_agreement",
            "passport_registration",
            "temporary_registration",
        ]
    ] = Field(default=None)
    file_hashes: typing.Optional[typing.List[str]] = Field(default=None)
    message: typing.Optional[str] = Field(default=None)


class PassportElementErrorUnspecified(BaseModel):
    """
    Represents an issue in an unspecified place. The error is considered resolved when
    new data is added.
    :param source: Error source, must be unspecified
    :param type: Type of element of the user's Telegram Passport which has the issue
    :param element_hash: Base64-encoded element hash
    :param message: Error message
    """

    source: typing.Optional[str] = Field(default=None)
    type: typing.Optional[str] = Field(default=None)
    element_hash: typing.Optional[str] = Field(default=None)
    message: typing.Optional[str] = Field(default=None)


class Game(BaseModel):
    """
    This object represents a game. Use BotFather to create and edit games, their short
    names will act as unique identifiers.
    :param title: Title of the game
    :param description: Description of the game
    :param photo: Photo that will be displayed in the game message in chats.
    :param text: Optional. Brief description of the game or high scores included in the game message.
    Can be automatically edited to include current high scores for the game when the bot
    calls setGameScore, or manually edited using editMessageText. 0-4096 characters.
    :param text_entities: Optional. Special entities that appear in text, such as usernames, URLs, bot
    commands, etc.
    :param animation: Optional. Animation that will be displayed in the game message in chats. Upload via
    BotFather
    """

    title: typing.Optional[str] = Field(default=None)
    description: typing.Optional[str] = Field(default=None)
    photo: typing.Optional[typing.List["PhotoSize"]] = Field(default=None)
    text: typing.Optional[str] = Field(default=None)
    text_entities: typing.Optional[typing.List["MessageEntity"]] = Field(default=None)
    animation: typing.Optional["Animation"] = Field(default=None)


class CallbackGame(BaseModel):
    """
    A placeholder, currently holds no information. Use BotFather to set up your game.
    """

    pass


class GameHighScore(BaseModel):
    """
    This object represents one row of the high scores table for a game.
    :param position: Position in high score table for the game
    :param user: User
    :param score: Score
    """

    position: typing.Optional[int] = Field(default=None)
    user: typing.Optional["User"] = Field(default=None)
    score: typing.Optional[int] = Field(default=None)


for v in locals().copy().values():
    if inspect.isclass(v) and issubclass(v, BaseModel):
        v.update_forward_refs()

__all__ = (
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
