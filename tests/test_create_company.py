import pytest

from ..set_urls import CREATE_COMPANY
from ..steps.create_company import CreateCompany


class TestCreateCompany:
    create_company = CreateCompany(CREATE_COMPANY)

    def test_create_company_valid_values(self):
        self.create_company.sent_create_company_request()
