import os
import random

from api import utils

SUCCESS_STATUS = 'SUCCESS'
FAILURE_STATUS = 'FAILURE'
EMPTY_STATUS = 'EMPTY'

STATUS_LIST = [SUCCESS_STATUS, FAILURE_STATUS, EMPTY_STATUS]

CAR_ROUTES = {
    SUCCESS_STATUS: [
        'successful_car_route_no_obsticals.json',
        'successful_car_route_with_obstacales.json',
    ],
    FAILURE_STATUS: [
        'failure_car_route_out_of_bounds.json',
    ],
    EMPTY_STATUS: [
        'empty_car_route.json',
    ],
}

ROUTE_DIRECTORY = os.path.join(os.path.dirname(__file__), 'fixtures')


def get_empty_route():
    return CAR_ROUTES[EMPTY_STATUS]


def get_random_route():
    random_status = random.choice(STATUS_LIST)
    return get_random_car_route_from_status(random_status)


def get_random_car_route_from_status(status):
    route_status = status.upper()
    try:
        route_list = CAR_ROUTES[route_status]
        filename = random.choice(route_list)
        file_with_path = os.path.join(ROUTE_DIRECTORY, filename)
        return utils.get_json_contents_from_resource_file(file_with_path)
    except IndexError:
        raise ValueError(
            f'Invalid route status \'{route_status}\' is invalid.'
        )
    except FileNotFoundError:
        raise ValueError(
            f'Automated car route with status \'{route_status}\' was not found.'
        )
