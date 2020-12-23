import json
import os
import random

SUCCESS_STATUS = 'SUCCESS'
FAILURE_STATUS = 'FAILURE'
EMPTY_STATUS = 'EMPTY'

STATUS_LIST = [SUCCESS_STATUS, FAILURE_STATUS, EMPTY_STATUS]

CAR_ROUTES = {
    SUCCESS_STATUS: [
        'successful_car_route_no_obstacles.json',
        'successful_car_route_with_obstacles.json',
    ],
    FAILURE_STATUS: [
        'failure_car_route_out_of_bounds.json',
    ],
    EMPTY_STATUS: [
        'empty_car_route.json',
    ],
}

ROUTE_DIRECTORY = os.path.join(os.path.dirname(__file__), 'fixtures')


def _open_config(filename):

    with open(filename) as config_file:
        json_contents = json.load(config_file)

    return json_contents


def get_car_route(status):
    route_status = status.upper()
    try:
        route_list = CAR_ROUTES[route_status]
        filename = random.choice(route_list)
        file_with_path = os.path.join(ROUTE_DIRECTORY, filename)
        return _open_config(file_with_path)
    except KeyError:
        raise KeyError(
            f'Automated car route with status \'{route_status}\' was not found.'
        )


def get_random_route():
    random_status = random.choice(STATUS_LIST)
    return get_car_route(random_status)
