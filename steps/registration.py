import json

from .base_methods import BaseMethod
import requests
from ..set_urls import DOREGISTER


class Registration(BaseMethod):

    def sent_registration_request(self, email, password, name):
        result = requests.post(self.api_path(DOREGISTER), data={
            "email": email,
            "password": password,
            "name": name
        })
        return result

    def should_be_full_answer(self, response_data):
        pass
        response_result = json.loads(response_data.text)
        assert response_result['name'] is True, 'Name of new user IS NOT correct'
        # {
        #     "name": "name-11102019-16-50-42-814505",
        #     "avatar": "http://users.bugred.ru//tmp/default_avatar.jpg",
        #     "password": "3c9909afec25354d551dae21590bb26e38d53f2173b8d3dc3eee4c047e7ab1c1eb8b85103e3be7ba613b31bb5c9c36214dc9f14a42fd7a2fdb84856bca5c44c2",
        #     "birthday": 0,
        #     "email": "11102019-16-50-42-814505@test.test",
        #     "gender": "",
        #     "date_start": 0,
        #     "hobby": ""
        # }

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
        assert response_result['type'] == 'error', 'Error IS NOT arise, but it must'
        assert non_unique_field in response_result['message'], 'There IS NOT details in the Error message'

        # {
        #     "type": "error",
        #     "message": " email 11.08.2019-23-06-59@test.test уже есть в базе"
        # }
