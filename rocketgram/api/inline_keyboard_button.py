# Copyright (C) 2015-2022 by Vd.
# This file is part of Rocketgram, the modern Telegram bot framework.
# Rocketgram is released under the MIT License (see LICENSE).


from dataclasses import dataclass
from typing import Optional, Dict

from .login_url import LoginUrl
from .web_app_info import WebAppInfo


@dataclass(frozen=True)
class InlineKeyboardButton:
    """\
    Represents InlineKeyboardButton keyboard object:
    https://core.telegram.org/bots/api#inlinekeyboardbutton
    """

    text: str
    url: Optional[str] = None
    login_url: Optional[LoginUrl] = None
    callback_data: Optional[str] = None
    web_app: Optional[WebAppInfo] = None
    switch_inline_query: Optional[str] = None
    switch_inline_query_current_chat: Optional[str] = None
    callback_game: Optional[str] = None
    pay: Optional[bool] = None

    @classmethod
    def parse(cls, data: Optional[Dict]) -> Optional['InlineKeyboardButton']:
        if data is None:
            return None

        return cls(data['text'], data.get('url'), LoginUrl.parse(data.get('login_url')), data.get('callback_data'),
                   WebAppInfo.parse(data.get('web_app')), data.get('switch_inline_query'),
                   data.get('switch_inline_query_current_chat'), data.get('callback_game'), data.get('pay'))
