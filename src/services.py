from typing import Dict
import json as _json

def get_all_quotes() -> Dict:
    with open("quotes.json") as events_file:
        data = _json.load(events_file)

    return data