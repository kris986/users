import requests
from nose.tools import assert_equals, assert_is_not_none, assert_equal, assert_in
from unittest import TestCase
from steps.doRegister import DoRegister
from set_urls import go_to_url, UI_URL


class BasicTestCase(TestCase):
    registration = DoRegister()

    def test_registration_new_user(self):
        email = self.registration.create_new_user()[0]
        name = self.registration.create_new_user()[1]
        password = self.registration.create_new_user()[2]
        registration_request = self.registration.do_register(email, name, password)
        assert_equals(registration_request[1].status_code, 200, 'Status code is not 200 OK')
        assert_equals(registration_request[1].json()['email'], email, 'Email is not equal')
        assert_equals(registration_request[1].json()['name'], name, 'Name is not equal')
        assert_in('avatar', registration_request[1].json(), 'There isn\'t avatar')
        assert_is_not_none(registration_request[1].json()['password'], 'There isn\'t password')
        assert_in('birthday', registration_request[1].json(), 'There isn\'t birthday')
        assert_in('gender', registration_request[1].json(), 'There isn\'t gender')
        assert_in('date_start', registration_request[1].json(), 'There isn\'t date_start')
        assert_in('hobby', registration_request[1].json(), 'There isn\'t hobby')

    def test_create_double_email(self):
        email = self.registration.create_new_user()[0]
        name = self.registration.create_new_user()[1]
        password = self.registration.create_new_user()[2]
        self.registration.do_register(email, name, password)
        double_registration_request = self.registration.do_register(email, name, password)
        assert_equals(double_registration_request[1].status_code, 200, 'Status code is not 200 OK')
        assert_equals(double_registration_request[1].json()['message'], ' email ' + email + ' уже есть в базе',
                      'Error message is wrong')
        assert_equal(double_registration_request[1].json()['type'], 'error', 'Error message is not correct')

    def test_create_double_name(self):
        email = self.registration.create_new_user()[0]
        name = self.registration.create_new_user()[1]
        password = self.registration.create_new_user()[2]
        self.registration.do_register(email, name, password)
        email = self.registration.create_new_user()[0]
        double_registration_name = self.registration.do_register(email, name, password)
        assert_equals(double_registration_name[1].status_code, 200, 'Status code is not 200 OK')
        assert_equals(double_registration_name[1].json()['message'], ' Текущее ФИО ' + name + ' уже есть в базе',
                      'Error message is wrong')
        assert_equal(double_registration_name[1].json()['type'], 'error', 'Error message is not correct')

    def test_new_user_on_ui(self):
        email = self.registration.create_new_user()[0]
        name = self.registration.create_new_user()[1]
        password = self.registration.create_new_user()[2]
        self.registration.do_register(email, name, password)
        main_html = requests.get(go_to_url(url=UI_URL)).text
        assert_in(email, main_html)
