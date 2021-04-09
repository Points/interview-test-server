import random

from api.autonomous_car import car_route_generator
from api.utils import naptime


def get_reliable_car_route(route_endpoint_name):
    route_filename = route_endpoint_name.lower().replace('-', '_')
    return car_route_generator.get_car_route(route_filename)


def get_unreliable_car_route():
    naptime()

    # Be Evil
    roulette = random.randint(1, 3)
    print(f'Database roulette {roulette}')
    if roulette == 3:
        raise Exception("Database not found!")
    return car_route_generator.get_random_route()
