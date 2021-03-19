# Copyright (C) 2015-2021 by Vd.
# This file is part of Rocketgram, the modern Telegram bot framework.
# Rocketgram is released under the MIT License (see LICENSE).


from dataclasses import dataclass


@dataclass(frozen=True)
class InputMessageContent:
    """\
    Represents InputMessageContent object:
    https://core.telegram.org/bots/api#inputmessagecontent
    """
