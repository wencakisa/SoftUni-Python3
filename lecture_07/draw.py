import sys
import os
from typing import List
from turtle import Turtle, done as turtle_done

from json.decoder import JSONDecodeError
from yaml import YAMLError

from lecture_07.loaders import Loader, JSONLoader, YAMLoader
from lecture_07.figures.base import Figure
from lecture_07.figures.simple import Circle, Rectangle, Square
from lecture_07.figures.polygon import Triangle, Polygon

LOADERS_EXTENSIONS = {
    '.json': JSONLoader,
    '.yaml': YAMLoader
}

FIGURE_TYPES = {
    'circle': Circle,
    'triangle': Triangle,
    'rectangle': Rectangle,
    'square': Square,
    'polygon': Polygon
}


def main():
    try:
        if len(sys.argv) < 2:
            print('Usage: {} <figures_filename>'.format(sys.argv[0]))
            return 2

        loader = get_loader(figures_filename=sys.argv[1])
        figures = load_figures(loader)
        draw_figures(figures)
    except JSONDecodeError as jde:
        print('Failed to parse JSON: {}'.format(str(jde)))
        return 1
    except YAMLError as ye:
        print('Failed to parse YAML: {}'.format(str(ye)))
        return 1
    except Exception as e:
        print('Error: {}'.format(e))
        return 1

    return 0


def get_loader(figures_filename: str) -> Loader:
    filename, extension = os.path.splitext(figures_filename)

    if extension in LOADERS_EXTENSIONS:
        loader = LOADERS_EXTENSIONS[extension](figures_filename)
    else:
        raise ValueError('Unsupported file format: {}'.format(extension))

    return loader


def load_figures(loader: Loader) -> List[Figure]:
    figures = []

    for figure_info in loader.load_data():
        figure_type = figure_info['type']

        if figure_type in FIGURE_TYPES:
            figure_instance = FIGURE_TYPES[figure_type](**figure_info)
            figures.append(figure_instance)
        else:
            raise ValueError('Figure not supported: {}'.format(figure_type))

    return figures


def draw_figures(figures: List[Figure]):
    t = Turtle()

    for figure in figures:
        figure.draw(t)

    turtle_done()

if __name__ == '__main__':
    sys.exit(main())
