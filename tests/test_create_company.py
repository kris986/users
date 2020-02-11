import pytest

from ..set_urls import CREATE_COMPANY
from ..steps.create_company import CreateCompany


class TestCreateCompany:
    create_company = CreateCompany(CREATE_COMPANY)

    def test_create_company_valid_values(self):
        result = self.create_company.sent_create_company_request(company_name="Алкоголики и тунеядцы",
                                                        company_type="ООО",
                                                        company_users=["test_anna@gmail.com", "mrak20@list.ru"],
                                                        email_owner="aa+1@mail.com")
        self.create_company.should_be_status_code_200(result)
