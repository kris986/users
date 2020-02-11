import requests

from users.steps.base_methods import BaseMethod


class CreateCompany(BaseMethod):

    def sent_create_company_request(self, company_name, company_type, company_users, email_owner):
        result = requests.post(self.api_path(), data={
            'company_name': company_name,
            'company_type': company_type,
            'company_users': company_users,
            'email_owner': email_owner
        })
        return result

    # {
    #     "company_name": "Алкоголики и тунеядцы",
    #     "company_type": "ООО",
    #     "company_users": ["test_anna@gmail.com", "mrak20@list.ru"],
    #     "email_owner": "aa+1@mail.com"
    # }

    def should_be_full_response(self, **kwargs):
        pass

    # {
    #     "type": "success",
    #     "id_company": 63,
    #     "company": {
    #         "name": "Алкоголики и тунеядцы",
    #         "type": "ООО",
    #         "inn": "",
    #         "ogrn": "",
    #         "kpp": "",
    #         "phone": "",
    #         "adress": "",
    #         "users": [
    #             "test_anna@gmail.com",
    #             "mrak20@list.ru"
    #         ]
    #     }
    # }
