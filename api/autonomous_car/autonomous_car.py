import json
import os
import random

DEFAULT_CAR_ROUTE_FILENAME = 'successful_car_route_no_obstacles.json'

CAR_ROUTE_FILENAMES = [
    DEFAULT_CAR_ROUTE_FILENAME,
    'successful_car_route_with_obstacles.json',
    'failure_car_route_out_of_bounds.json',
    'empty_car_route.json',
]

ROUTE_DIRECTORY = os.path.join(os.path.dirname(__file__), 'fixtures')


def _open_config(filename):

    with open(filename) as config_file:
        json_contents = json.load(config_file)

    return json_contents


def get_car_route(get_random=False):
    route_file_name = random.choice(CAR_ROUTE_FILENAMES) if get_random else DEFAULT_CAR_ROUTE_FILENAME
    file_with_path = os.path.join(ROUTE_DIRECTORY, route_file_name)
    return _open_config(file_with_path)
