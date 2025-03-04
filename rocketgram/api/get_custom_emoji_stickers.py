# Copyright (C) 2015-2022 by Vd.
# This file is part of Rocketgram, the modern Telegram bot framework.
# Rocketgram is released under the MIT License (see LICENSE).


from dataclasses import dataclass
from typing import List

from .request import Request
from .sticker import Sticker
from ..context import context


@dataclass(frozen=True)
class GetCustomEmojiStickers(Request):
    """\
    Represents GetCustomEmojiStickers request object:
    https://core.telegram.org/bots/api#getcustomemojistickers
    """

    custom_emoji_ids: List[str]

    def parse_result(self, data) -> List[Sticker]:
        assert isinstance(data, list), "Should be list."
        return [Sticker.parse(r) for r in data]

    async def send(self) -> List[Sticker]:
        res = await context.bot.send(self)
        return res.result
