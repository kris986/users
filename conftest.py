import pytest

from users.set_urls import DOREGISTER
from users.steps.registration import Registration


@pytest.fixture
def creating_new_user():
    registration = Registration(DOREGISTER)
    user_data = registration.generator_user_data()
    registration.sent_registration_request(email=user_data['user_email'], password=user_data['password'],
                                           name=user_data['user_name'])
    return user_data
