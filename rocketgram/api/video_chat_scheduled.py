# Copyright (C) 2015-2022 by Vd.
# This file is part of Rocketgram, the modern Telegram bot framework.
# Rocketgram is released under the MIT License (see LICENSE).


from dataclasses import dataclass
from datetime import datetime
from typing import Optional


@dataclass(frozen=True)
class VideoChatScheduled:
    """\
    Represents VideoChatScheduled object:
    https://core.telegram.org/bots/api#videochatscheduled
    """

    start_date: datetime

    @classmethod
    def parse(cls, data: dict) -> Optional['VideoChatScheduled']:
        if data is None:
            return None

        start_date = datetime.utcfromtimestamp(data['start_date']) if 'start_date' in data else None

        return cls(start_date)
