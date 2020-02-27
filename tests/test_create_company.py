# coding=utf-8
import json
from datetime import datetime

import pytest
from requests.auth import HTTPBasicAuth

from ..steps.create_company import CreateCompany

gen_unique_part = datetime.now().strftime("%d.%m.%Y-%H-%M-%S-%f")


@pytest.mark.create_company
class TestCreateCompany:
    create_company = CreateCompany()

    @pytest.mark.parametrize('company_type', ['ИП', 'ООО', 'ОАО'], ids=['IP', 'OOO', 'OAO'])
    def test_create_company_valid_values(self, creating_new_user, company_type):
        company_name = f"Test company {gen_unique_part}"
        company_users = [f'{creating_new_user["user_email"]}']
        email_owner = creating_new_user['user_email']
        self.create_company.post_request(data=json.dumps({
            'company_name': company_name,
            'company_type': company_type,
            'company_users': company_users,
            'email_owner': email_owner
        }), auth=HTTPBasicAuth(email_owner, creating_new_user['password']))
        self.create_company.should_be_status_code_200()
        self.create_company.should_be_required_fields_response_body(company_name, company_type, company_users)

    @pytest.mark.parametrize('company_type', [' ',
                                              '\t',
                                              'ОАО1',
                                              'WTF'],
                             ids=['string with space sigh', 'sigh of tab', 'OAO1', 'WTF'])
    def test_create_company_invalid_company_type(self, creating_new_user, company_type):
        company_name = f"Test company {gen_unique_part}"
        company_users = ['secundus@mail.com', 'primus@mail.com']
        email_owner = creating_new_user['user_email']
        self.create_company.post_request(data=json.dumps({
            'company_name': company_name,
            'company_type': company_type,
            'company_users': company_users,
            'email_owner': email_owner
        }), auth=HTTPBasicAuth(email_owner, creating_new_user['password']))
        self.create_company.should_be_status_code_200()
        self.create_company.should_be_error_msg_for_error_field(company_type)
