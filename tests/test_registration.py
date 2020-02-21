from ..steps.registration import Registration


class TestRegistration:
    registration = Registration()

    def test_registration_valid_data(self):
        user_data = self.registration.generator_user_data()
        self.registration.sent_registration_request(email=user_data['user_email'],
                                                    password=user_data['password'],
                                                    name=user_data['user_name'])
        self.registration.should_be_status_code_200()
        self.registration.should_be_required_fields_response_body(user_data['user_email'],
                                                                  user_data['user_name'])

    def test_fail_registration_with_duplicate_email(self):
        user_data = self.registration.generator_user_data()
        user_email_for_reuse = user_data['user_email']
        self.registration.sent_registration_request(email=user_email_for_reuse,
                                                    password=user_data['password'],
                                                    name=user_data['user_name'])
        self.registration.should_be_status_code_200()
        self.registration.should_be_required_fields_response_body(posted_user_email=user_email_for_reuse,
                                                                  posted_user_name=user_data['user_name'])
        user_data = self.registration.generator_user_data()
        self.registration.sent_registration_request(email=user_email_for_reuse,
                                                    password=user_data['password'],
                                                    name=user_data['user_name'])
        self.registration.should_be_status_code_200()
        self.registration.should_be_error_msg_non_unique_field(user_email_for_reuse)

    def test_fail_registration_with_duplicate_user_name(self):
        user_data = self.registration.generator_user_data()
        user_name_for_reuse = user_data['user_name']
        self.registration.sent_registration_request(email=user_data['user_email'],
                                                    password=user_data['password'],
                                                    name=user_name_for_reuse)
        self.registration.should_be_status_code_200()
        self.registration.should_be_required_fields_response_body(posted_user_email=user_data['user_email'],
                                                                  posted_user_name=user_name_for_reuse)
        user_data = self.registration.generator_user_data()
        self.registration.sent_registration_request(email=user_data['user_email'],
                                                    password=user_data['password'],
                                                    name=user_name_for_reuse)
        self.registration.should_be_status_code_200()
        self.registration.should_be_error_msg_non_unique_field(user_name_for_reuse)
