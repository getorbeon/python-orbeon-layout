from draw.main import draw
from draw.data import get_context_example_data


if __name__ == '__main__':
    context = get_context_example_data('data_1.json')
    draw(context)