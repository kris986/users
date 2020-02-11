from datetime import datetime

from ..steps.base_methods import BaseMethod
from ..steps.registration import Registration
from ..set_urls import DOREGISTER


class TestRegistration:

    registration = Registration(DOREGISTER)

    def test_registration_valid_data(self):
        user_data = self.registration.generator_user_data()
        response = self.registration.sent_registration_request(email=user_data['user_email'],
                                                               password=user_data['password'],
                                                               name=user_data['user_name'])
        self.registration.should_be_status_code_200(response)
        self.registration.should_be_requare_fields_response_body(response, user_data['user_email'],
                                                                 user_data['user_name'])

    def test_fail_registration_with_duplicate_email(self):
        user_data = self.registration.generator_user_data()
        user_email_for_reuse = user_data['user_email']
        response = self.registration.sent_registration_request(email=user_email_for_reuse,
                                                               password=user_data['password'],
                                                               name=user_data['user_name'])
        self.registration.should_be_status_code_200(response)
        self.registration.should_be_requare_fields_response_body(response, posted_user_email=user_email_for_reuse,
                                                                 posted_user_name=user_data['user_name'])
        user_data = self.registration.generator_user_data()
        response_non_unique_email = self.registration.sent_registration_request(email=user_email_for_reuse,
                                                                                password=user_data['password'],
                                                                                name=user_data['user_name'])
        self.registration.should_be_status_code_200(response_non_unique_email)
        self.registration.should_be_error_msg_non_unique_field(response_non_unique_email, user_email_for_reuse)

    def test_fail_registration_with_duplicate_user_name(self):
        user_data = self.registration.generator_user_data()
        user_name_for_reuse = user_data['user_name']
        response = self.registration.sent_registration_request(email=user_data['user_email'],
                                                               password=user_data['password'],
                                                               name=user_name_for_reuse)
        self.registration.should_be_status_code_200(response)
        self.registration.should_be_requare_fields_response_body(response, posted_user_email=user_data['user_email'],
                                                                 posted_user_name=user_name_for_reuse)
        user_data = self.registration.generator_user_data()
        response_non_unique_name = self.registration.sent_registration_request(email=user_data['user_email'],
                                                                               password=user_data['password'],
                                                                               name=user_name_for_reuse)
        self.registration.should_be_status_code_200(response_non_unique_name)
        self.registration.should_be_error_msg_non_unique_field(response_non_unique_name, user_name_for_reuse)
