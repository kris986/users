#!/usr/bin/env python
# -*- coding: utf-8 -*-
import pytest


# pytest.main(['--setup-show', '-s', '--tb=line', '--junitxml=test-results/junit.xml', '--alluredir=/test-results/my_allure_results', 'tests'])
pytest.main(['--setup-show', '-s', '--tb=line', '--alluredir=test-results/my_allure_results', 'tests'])
