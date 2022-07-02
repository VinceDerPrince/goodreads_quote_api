from typing import Dict
import json as _json
from random import randint

def get_all_quotes() -> Dict:
    with open("quotes.json") as quotes_file:
        data = _json.load(quotes_file)

    return data

def get_random_quote() -> Dict:
    quotes = get_all_quotes()
    rand_page = randint(0,99)
    rand_quote = randint(0,29)
   
    return quotes[f"{rand_page}"]["content"][f"{rand_quote}"]