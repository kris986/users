import json

import allure
import requests

from users.steps.base_methods import BaseMethod


class CreateCompany(BaseMethod):

    @allure.step
    def sent_create_company_request(self, company_name, company_type, company_users, email_owner):
        self.response = requests.post(self.api_path(), data={
            'company_name': company_name,
            'company_type': company_type,
            'company_users': company_users,
            'email_owner': email_owner
        })
        return self.response

    @allure.step(title='Checking response body')
    def should_be_required_fields_response_body(self, company_name, company_type, company_users, email_owner=None):
        response_result = json.loads(self.response.text)
        assert response_result['type'] == 'success', \
            f'company WAS NOT created successfully\nMessage from body: {response_result["message"]}'
        assert response_result['company']['name'] == company_name, 'Name of new user IS NOT correct'
        assert response_result[
                   'avatar'] == 'http://users.bugred.ru//tmp/default_avatar.jpg', 'Name of company IS NOT correct'
        assert response_result['company']['company_type'] == company_type, 'company_type IS NOT correct'
        assert response_result['company']['company_users'] == company_users, 'e-mails of added users IS/ARE NOT correct'
