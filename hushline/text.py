from __future__ import annotations

import re
import unicodedata

from unidecode import unidecode


def sort_key(value: str) -> str:
    normalized = unicodedata.normalize("NFKC", value.strip())
    return unidecode(normalized).casefold()


def slugify(value: str) -> str:
    normalized = sort_key(value)
    return re.sub(r"[^a-z0-9]+", "-", normalized).strip("-")
