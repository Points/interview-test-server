import os
import json
import pytest 

routes_dir = os.path.join(os.path.dirname(__file__), 'fixtures')

def _get_routes(route_name):
  
    filename = f'{route_name}.json'
    file_with_path = os.path.join(routes_dir, filename)

    with open(file_with_path) as config_file:
        json_contents = json.load(config_file)
        config_file.close()

    return json_contents


def test_empty_route(client): 
  resp = client.get('autonomous-car/routes/empty-route/')
  empty_route = _get_routes('empty_route')
  assert resp.json == {'route': empty_route}


@pytest.mark.parametrize(
    'api_route,route_details',
    [
        ('empty-route', 'empty_route'),
        ('success-no-obstacles', 'success_no_obstacles'),
        ('success-with-obstacles', 'success_with_obstacles'),
        ('failure-hits-obstacle', 'failure_hits_obstacle'),
        ('failure-out-of-bounds', 'failure_out_of_bounds'),
    ],
)
def test_routes_match_fixtures(client, api_route, route_details):
  resp = client.get(f'autonomous-car/routes/{api_route}/')
  final_route = _get_routes(route_details)
  assert resp.json == {'route': final_route}
