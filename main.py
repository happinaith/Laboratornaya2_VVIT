from typing import Union

import wikipedia
from pydantic import BaseModel
from fastapi import FastAPI

app = FastAPI()


class WikiPage(BaseModel):
    Title: str
    Description: str
    Content: str
    URL: str

class question(BaseModel):
    quest: str


@app.get("/{zapros}")
def poisk_page(zapros: str):
    npage = wikipedia.search(zapros, results = 1)
    return wikipedia.page(npage, auto_suggest=True).URL

@app.get("/{zapros}/description")
def get_descr(zapros: str, sentenc_num: int):
    return wikipedia.summary(zapros, sentences = sentenc_num)

@app.post("/pages")
def add_wiki(quest_input: question):
    FoundPage = wikipedia.search(quest_input.quest, results = 1)
    return WikiPage(Title=wikipedia.page(FoundPage).title, Description=wikipedia.summary(FoundPage, sentences = 2), Content=wikipedia.page(FoundPage).content, URL=wikipedia.page(FoundPage).URL)