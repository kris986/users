import json

from .base_methods import BaseMethod
import requests
from ..set_urls import DOREGISTER


class Registration(BaseMethod):

    def sent_registration_request(self, email, password, name):
        result = requests.post(self.api_path(), data={
            "email": email,
            "password": password,
            "name": name
        })
        return result

    def should_be_full_answer(self, response_data):
        pass
        response_result = json.loads(response_data.text)
        assert response_result['name'] is True, 'Name of new user IS NOT correct'

    def should_be_requare_fields_response_body(self, response, posted_user_email, posted_user_name):
        response_result = json.loads(response.text)
        assert response_result['name'] == posted_user_name, 'Name of new user IS NOT correct'
        assert response_result[
                   'avatar'] == 'http://users.bugred.ru//tmp/default_avatar.jpg', 'Name of new user IS NOT correct'
        assert response_result['password'] is not None, 'Name of new user IS NOT correct'
        assert response_result['birthday'] == 0, 'Name of new user IS NOT correct'
        assert response_result['email'] == posted_user_email, 'Name of new user IS NOT correct'
        assert response_result['gender'] == '', 'Name of new user IS NOT correct'
        assert response_result['date_start'] == 0, 'Name of new user IS NOT correct'
        assert response_result['hobby'] == '', 'Name of new user IS NOT correct'

    def should_be_error_msg_non_unique_field(self, response, non_unique_field):
        response_result = json.loads(response.text)
        assert 'type' in response_result, 'There is not requared type field'
        assert response_result['type'] == 'error', 'Error IS NOT arise, but it must'
        assert non_unique_field in response_result['message'], 'There IS NOT details in the Error message'
