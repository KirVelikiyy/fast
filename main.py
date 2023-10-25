from datetime import datetime
from typing import Annotated

from fastapi import FastAPI, Query
from models import LangCard


app = FastAPI()


@app.post("/language-cards/")
async def create_lang_card(lang_card: LangCard):
    card_dict = lang_card.model_dump()
    card_dict.update({"datetime": datetime.now()})
    return card_dict


@app.get("/language-cards/")
async def read_lang_cards(
        q: Annotated[
            str | None,
            Query(
                min_length=5,
                max_length=50,
                description="Query string for the test Annotated Query validation",
                pattern="^query$"
            ),
        ] = None
):
    lang_card = LangCard(
        original_lang="russian",
        translation_lang="english",
        word="слово",
        translation="word"
    )
    results = {"items": [{"item_id": "Foo", "lang_card": lang_card.model_dump()}]}
    if q:
        results.update({"q": q})
    return results
