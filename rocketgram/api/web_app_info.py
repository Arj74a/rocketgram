# Copyright (C) 2015-2022 by Vd.
# This file is part of Rocketgram, the modern Telegram bot framework.
# Rocketgram is released under the MIT License (see LICENSE).


from dataclasses import dataclass
from typing import Optional, Dict


@dataclass(frozen=True)
class WebAppInfo:
    """\
    Represents WebAppInfo keyboard object:
    https://core.telegram.org/bots/api#webappinfo
    """

    url: str

    @classmethod
    def parse(cls, data: Optional[Dict]) -> Optional['WebAppInfo']:
        if data is None:
            return None

        return cls(url=data['url'])
