#!/usr/bin/env python
# -*- coding: UTF-8 -*-
import pytest

if __name__ == "__main__":
    pytest.main(['-s', '-v', '-m','cart', '--reruns', '0', '--reruns-delay', '5', '--html=./output/report/report.html', "--self-contained-html", "--alluredir=./output/allure_reports"])
