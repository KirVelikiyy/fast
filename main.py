from enum import Enum
from datetime import datetime

from fastapi import FastAPI
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


app = FastAPI()


@app.post("/language-cards/")
async def create_lang_card(lang_card: LangCard):
    card_dict = lang_card.dict()
    card_dict.update({"datetime": datetime.now()})
    return card_dict
