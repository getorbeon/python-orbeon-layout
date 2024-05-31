import json
from pathlib import Path
from draw.main import draw


def get_context_example_data():
    data = {}
    data_address = Path(__file__).parent.joinpath('draw').joinpath('data_1.json')
    with data_address.open('r', encoding='utf8') as json_data:
        data = json.load(json_data)
        json_data.close()
    return data


if __name__ == '__main__':
    context = get_context_example_data()
    draw(context, True)