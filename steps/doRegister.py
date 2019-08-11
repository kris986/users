# -*- coding: utf-8 -*-

import requests
from set_urls import go_to_url
from set_urls import REGISTER_PATH as register_path
from datetime import datetime


class DoRegister:

    @staticmethod
    def create_new_user():
        now = datetime.now().strftime("%d.%m.%Y-%H-%M-%S")
        email = now + '@test.test'
        name = 'User_' + now
        password = '1234567'
        return email, name, password

    def do_register(self, email, name, password):
        url_method = go_to_url(register_path)
        new_user_params = {
            "email": email,
            "name": name,
            "password": password
        }
        result = requests.post(url_method, params=new_user_params)
        return new_user_params, result
