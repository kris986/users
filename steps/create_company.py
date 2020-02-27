import json

import allure

from ..set_urls import CREATE_COMPANY
from ..steps.base_methods import BaseMethod


class CreateCompany(BaseMethod):

    def __init__(self, method=CREATE_COMPANY):
        self.method = method

    @allure.step(title='Checking response body')
    def should_be_required_fields_response_body(self, company_name, company_type, company_users, email_owner=None):
        response_result = json.loads(self.response.text)
        assert response_result['type'] == 'success', \
            f'company WAS NOT created successfully\nMessage from body: {response_result["message"]}'
        assert response_result['id_company'] is not None and isinstance(
            response_result['id_company'], int), 'There is non correct response_result "id_company"'
        assert response_result['company']['name'] == company_name, 'Name of new user IS NOT correct'
        assert response_result['company']['type'] == company_type, 'company_type IS NOT correct'
        assert response_result['company']['users'] == company_users, 'e-mails of added users IS/ARE NOT correct'
