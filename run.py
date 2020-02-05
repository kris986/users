#!/usr/bin/env python
# -*- coding: utf-8 -*-
import pytest

pytest.main(['-s', '--tb=line', '--junitxml=test-results/junit.xml', 'tests'])
