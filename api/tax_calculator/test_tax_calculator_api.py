import os
import json

brackets_dir = os.path.join(os.path.dirname(__file__), 'fixtures')

def _get_brackets(tax_year):
  
    filename = f'tax-brackets--{tax_year}.json'
    file_with_path = os.path.join(brackets_dir, filename)

    with open(file_with_path) as config_file:
        json_contents = json.load(config_file)
        config_file.close()

    return json_contents


def test_basic_route(client): 
  resp = client.get('/tax-calculator/')
  brackets = _get_brackets('2022')
  assert resp.json == {'tax_brackets': brackets}
