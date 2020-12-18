import json
import random
import time


def random_nap_time():
    sleep_time = random.randint(0, 5)
    time.sleep(sleep_time)


def perform_evil_roulette():
    roulette = random.randint(1, 3)
    print(f'Database roulette {roulette}')
    if roulette == 3:
        raise Exception("Database not found!")


def get_json_contents_from_resource_file(file_path):
    with open(file_path) as config_file:
        json_contents = json.load(config_file)

    return json_contents
