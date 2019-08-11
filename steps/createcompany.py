import requests

from set_urls import go_to_url
from set_urls import CREATE_COMPANY as create_company_path
from datetime import datetime
import random


class CreateCompany:

    @staticmethod
    def create_new_company():
        now = datetime.now().strftime("%H%M%S")
        company_name = 'Company number ' + now
        company_type = random.choice(['ИП', 'ООО', 'ОАО'])
        email_owner = 'kris986@mail.ru'
        print(company_type)
        print(company_name)
        return company_name, company_type, email_owner

    def create_company(self, company_name, company_type, email_owner):
        url_method = go_to_url(create_company_path)
        new_company_params = {
            "company_name": company_name,
            "company_type": company_type,
            "company_users": ["test_anna@gmail.com", "mrak20@list.ru"],
            "email_owner": email_owner
        }
        result = requests.post(url_method, params=new_company_params)
        return new_company_params, result


CreateCompany.create_new_company()
