import random

from api.autonomous_car import autonomous_car
from api.utils import naptime


def get_reliable_car_route():
    return autonomous_car.get_car_route()


def get_unreliable_car_route():
    naptime()

    # Be Evil
    roulette = random.randint(1, 3)
    print(f'Database roulette {roulette}')
    if roulette == 3:
        raise Exception("Database not found!")
    return autonomous_car.get_car_route(get_random=True)
