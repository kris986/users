from datetime import datetime

import allure
import pytest

from .set_urls import DOREGISTER
from .steps.registration import Registration

gen_unique_part = datetime.now().strftime("%d.%m.%Y-%H-%M-%S-%f")


@allure.step
@pytest.fixture(scope='module')
def creating_new_user():
    """ Module Fixture. Creator new user in system """
    registration = Registration()
    user_data = registration.generator_user_data()
    registration.sent_registration_request(email=user_data['user_email'],
                                           password=user_data['password'],
                                           name=user_data['user_name'])
    yield user_data
