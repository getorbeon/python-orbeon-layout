import json
from pathlib import Path


def get_context_example_data(filename):
    data = {}
    data_address = Path(__file__).parent.joinpath(filename)
    with data_address.open('r', encoding='utf8') as json_data:
        data = json.load(json_data)
        json_data.close()
    return data