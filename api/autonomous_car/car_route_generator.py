import json
import os
import random

ROUTE_DIRECTORY = os.path.join(os.path.dirname(__file__), 'fixtures')


def _open_config(path):
    with open(path) as config_file:
        json_contents = json.load(config_file)
    return json_contents


def _get_file_contents_or_raise_exception(filename):
    try:
        file_with_path = os.path.join(ROUTE_DIRECTORY, filename)
        return _open_config(file_with_path)
    except Exception:
        raise FileNotFoundError(
            f"Route with the name '{filename}' was not found."
        )


def get_car_route(route_name='empty_route'):
    route_filename = f'{route_name}.json'
    return _get_file_contents_or_raise_exception(route_filename)


def get_random_route():
    all_route_filenames = os.listdir(ROUTE_DIRECTORY)
    random_route_filename = random.choice(all_route_filenames)
    return _get_file_contents_or_raise_exception(random_route_filename)

