from enum import Enum
from pydantic import BaseModel


class Language(Enum):
    russian = 'russian'
    english = 'english'
    german = 'german'


class LangCard(BaseModel):
    description: str | None = None
    original_lang: Language
    translation_lang: Language
    word: str
    translation: str
