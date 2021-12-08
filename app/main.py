# -*- coding: utf-8 -*-
from random import choice
from werkzeug import datastructures
from flask import Flask, request

from app.quotes import QUOTES


app = Flask(__name__)
DEFAULT_LANGUAGE = "pt-br"


def __get_language__(accept_languages: datastructures.LanguageAccept) -> str:
    lang = accept_languages.best
    if lang is None:
        lang = DEFAULT_LANGUAGE
    else:
        lang = lang.lower()

    if lang not in ["pt-br", "en-us"]:
        return DEFAULT_LANGUAGE

    return lang


def __get_quote__(lang: str) -> str:
    return choice(QUOTES[lang])


@app.route("/")
def get_quote():
    # Getting desired language. If not informed or not supported, will default to whatever is set in DEFAULT_LANGUAGE.
    lang = __get_language__(request.accept_languages)

    # Getting random quote.
    quote = __get_quote__(lang)

    # Return quote.
    return quote
