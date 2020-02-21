# coding=utf-8
from datetime import datetime

import pytest

from ..steps.create_company import CreateCompany

gen_unique_part = datetime.now().strftime("%d.%m.%Y-%H-%M-%S-%f")


class TestCreateCompany:
    create_company = CreateCompany()

    @pytest.mark.xfail(reason='There is bug in API')
    @pytest.mark.parametrize('company_type', ['ИП', 'ООО', 'ОАО'])
    def test_create_company_valid_values(self, creating_new_user, company_type):
        company_name = f"Test company {gen_unique_part}"
        company_users = ['secundus@mail.com', 'primus@mail.com']
        email_owner = creating_new_user['user_email']
        self.create_company.sent_create_company_request(company_name=company_name,
                                                        company_type=company_type,
                                                        company_users=company_users,
                                                        email_owner=email_owner)
        self.create_company.should_be_status_code_200()
        self.create_company.should_be_required_fields_response_body(company_name, company_type, company_users)

    @pytest.mark.parametrize('company_type', [' ', '\t', 'ОАО1', 'WTF'])
    def test_create_company_invalid_company_type(self, creating_new_user, company_type):
        company_name = f"Test company {gen_unique_part}"
        company_users = ['secundus@mail.com', 'primus@mail.com']
        email_owner = creating_new_user['user_email']
        self.create_company.sent_create_company_request(company_name=company_name,
                                                        company_type=company_type,
                                                        company_users=company_users,
                                                        email_owner=email_owner)
        self.create_company.should_be_status_code_200()
        self.create_company.should_be_error_msg_for_error_field(company_type)
