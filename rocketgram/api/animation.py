# Copyright (C) 2015-2022 by Vd.
# This file is part of Rocketgram, the modern Telegram bot framework.
# Rocketgram is released under the MIT License (see LICENSE).


from dataclasses import dataclass
from typing import Optional

from .photo_size import PhotoSize


@dataclass(frozen=True)
class Animation:
    """\
    Represents Animation object:
    https://core.telegram.org/bots/api#animation
    """

    file_id: str
    file_unique_id: str
    width: str
    height: str
    duration: str
    thumb: Optional[PhotoSize]
    file_name: Optional[str]
    mime_type: Optional[str]
    file_size: Optional[int]

    @classmethod
    def parse(cls, data: dict) -> Optional['Animation']:
        if data is None:
            return None

        return cls(data['file_id'], data['file_unique_id'], data['width'], data['height'], data['duration'],
                   PhotoSize.parse(data.get('thumb')), data.get('file_name'),
                   data.get('mime_type'), data.get('file_size'))
