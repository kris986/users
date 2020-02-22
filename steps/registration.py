import json

import allure
import requests

from .base_methods import BaseMethod
from ..set_urls import DOREGISTER


class Registration(BaseMethod):

    def __init__(self, method=DOREGISTER):
        self.method = method

    @allure.step(title='Sending POST request for Registration')
    def sent_registration_request(self, email, password, name):
        self.response = requests.post(self.api_path(), data={
            "email": email,
            "password": password,
            "name": name
        })
        return self.response

    def should_be_full_answer(self):
        response_result = json.loads(self.response.text)
        assert response_result['name'] is True, 'Name of new user IS NOT correct'

    @allure.step(title='Checking response body [Registration]')
    def should_be_required_fields_response_body(self, posted_user_email, posted_user_name):
        response_result = json.loads(self.response.text)
        assert response_result['name'] == posted_user_name, 'Name of new user IS NOT correct'
        assert response_result[
                   'avatar'] == 'http://users.bugred.ru//tmp/default_avatar.jpg', 'Name of new user IS NOT correct'
        assert response_result['password'] is not None, 'Name of new user IS NOT correct'
        assert response_result['birthday'] == 0, 'Name of new user IS NOT correct'
        assert response_result['email'] == posted_user_email, 'Name of new user IS NOT correct'
        assert response_result['gender'] == '', 'Name of new user IS NOT correct'
        assert response_result['date_start'] == 0, 'Name of new user IS NOT correct'
        assert response_result['hobby'] == '', 'Name of new user IS NOT correct'

    @allure.step(title='Checking response body [Registration | non unique field]')
    def should_be_error_msg_non_unique_field(self, non_unique_field):
        response_result = json.loads(self.response.text)
        assert 'type' in response_result, 'There is not requared type field'
        assert response_result['type'] == 'error', 'Error IS NOT arise, but it must'
        assert non_unique_field in response_result['message'], 'There IS NOT details in the Error message'
