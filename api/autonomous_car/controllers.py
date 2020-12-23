import random

from api.autonomous_car import autonomous_car
from api.utils import naptime


def is_valid_status(status):
    return status.upper() in autonomous_car.STATUS_LIST


def get_reliable_car_route():
    return autonomous_car.get_random_route()


def get_unreliable_car_route(status):
    naptime()

    # Be Evil
    roulette = random.randint(1, 3)
    print(f'Database roulette {roulette}')
    if roulette == 3:
        raise Exception("Database not found!")
    return autonomous_car.get_car_route(status)
