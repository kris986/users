from datetime import datetime

from ..steps.registration import Registration
from ..set_urls import DOREGISTER


class TestRegistration:
    registration = Registration(DOREGISTER)
    gen_unique_part = datetime.now().strftime("%d.%m.%Y-%H-%M-%S-%f")
    user_email = f'{gen_unique_part}@test.test'
    user_name = f'Name-{gen_unique_part}'
    password = f'PASS{gen_unique_part}'

    def test_rgstrtn_valid_data(self):
        response = self.registration.sent_registration_request(email=self.user_email, password=self.password,
                                                               name=self.user_name)
        self.registration.should_be_status_code_200(response)
        self.registration.should_be_requare_fields_response_body(response, self.user_email, self.user_name)

    def test_double_email(self):
        user_email_for_reuse = self.user_email
        response = self.registration.sent_registration_request(email=user_email_for_reuse,
                                                               password=self.password,
                                                               name=self.user_name)
        self.registration.should_be_status_code_200(response)
        self.registration.should_be_requare_fields_response_body(response, self.user_email, self.user_name)
        response_non_unique_email = self.registration.sent_registration_request(email=user_email_for_reuse,
                                                                                password=self.password,
                                                                                name=self.user_name)
        self.registration.should_be_status_code_200(response_non_unique_email)
        self.registration.should_be_error_msg_non_unique_field(response_non_unique_email, user_email_for_reuse)

    def test_non_unique_user_name(self):
        pass
        # 200 ok
        # {
        #     "type": "error",
        #     "message": " Текущее ФИО name уже есть в базе"
        # }
