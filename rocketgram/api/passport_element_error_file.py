# Copyright (C) 2015-2022 by Vd.
# This file is part of Rocketgram, the modern Telegram bot framework.
# Rocketgram is released under the MIT License (see LICENSE).


from dataclasses import dataclass, field

from .encrypted_passport_element_type import EncryptedPassportElementType
from .passport_element_error import PassportElementError


@dataclass(frozen=True)
class PassportElementErrorFile(PassportElementError):
    """\
    Represents PassportElementErrorFile object:
    https://core.telegram.org/bots/api#passportelementerrorfile
    """

    source: str = field(init=False, default='file')

    type: EncryptedPassportElementType
    file_hash: str
    message: str
