# Copyright (C) 2015-2022 by Vd.
# This file is part of Rocketgram, the modern Telegram bot framework.
# Rocketgram is released under the MIT License (see LICENSE).


from enum import auto

from .utils import EnumAutoName


class ChatType(EnumAutoName):
    private = auto()
    group = auto()
    supergroup = auto()
    channel = auto()
    sender = auto()
    unknown = auto()
