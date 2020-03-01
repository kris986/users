import json
from os.path import join, dirname

import allure
from datetime import datetime
from urllib.parse import urljoin

import requests
from jsonschema import validate, ValidationError

from ..set_urls import API_URL


class BaseMethod:
    response = None

    def __init__(self, method, schema_filename):
        self.method = method
        self.schema_filename = schema_filename

    def api_path(self):
        method_url = urljoin(API_URL, self.method)
        return method_url

    @allure.step
    def post_request(self, **kwargs):
        self.response = requests.post(self.api_path(), verify=False,  **kwargs)
        return self.response

    @allure.step
    def generator_user_data(self):
        """ Generator unique user's data """
        gen_unique_part = datetime.now().strftime("%d.%m.%Y-%H-%M-%S-%f")
        user_email = f'{gen_unique_part}@test.test'
        user_name = f'Name-{gen_unique_part}'
        password = f'PASS{gen_unique_part}'
        user_data = {'user_email': user_email,
                     'user_name': user_name,
                     'password': password}
        return user_data

    def should_be_status_code_200(self):
        assert self.response.status_code == 200, 'Status code IS NOT 200 ok'

    def should_be_status_code_401(self):
        assert self.response.status_code == 401, 'Status code IS NOT 401'

    def should_be_status_code_403(self):
        assert self.response.status_code == 403, 'Status code IS NOT 403'

    def should_be_error_msg_for_error_field(self, error_field: str):
        response_result = json.loads(self.response.text)
        assert 'type' in response_result, 'There is not required type field'
        assert response_result['type'] == 'error', 'Error IS NOT arise, but it should'
        assert error_field in response_result['message'], 'There ARE NOT details in the Error message'

    @allure.step
    def should_be_valid_json_schema(self):
        assert self._json_schema_is_valid(), 'JSON scheme of response is not valid'

    def _json_schema_is_valid(self) -> bool:
        schema = self.__load_json_schema()
        try:
            validate(json.loads(self.response.text), schema)
            return True
        except ValidationError:
            return False

    def __load_json_schema(self):
        """ Loads the given schema file """

        relative_path = join('schemas', self.schema_filename)
        absolute_path = join(dirname(__file__), relative_path)

        with open(absolute_path) as schema_file:
            return json.loads(schema_file.read())
