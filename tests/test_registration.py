from datetime import datetime

from ..steps.registration import Registration
from ..set_urls import DOREGISTER


class TestRegistration:
    registration = Registration(DOREGISTER)

    def test_rgstrtn_valid_data(self):
        gen_unique_part = datetime.now().strftime("%d.%m.%Y-%H-%M-%S-%f")
        user_email = f'{gen_unique_part}@test.test'
        user_name = f'Name-{gen_unique_part}'
        password = f'PASS{gen_unique_part}'
        response = self.registration.sent_registration_request(email=user_email, password=password, name=user_name)
        self.registration.should_be_status_code_200(response)
        self.registration.should_be_requare_fields_response_body(response, user_email, user_name)

    def test_double_email(self):
        pass
    # 200 OK
    # {
    #     "type": "error",
    #     "message": " email 11.08.2019-23-06-59@test.test уже есть в базе"
    # }


    def test_non_unique_user_name(self):
        pass
        # 200 ok
        # {
        #     "type": "error",
        #     "message": " Текущее ФИО name уже есть в базе"
        # }
