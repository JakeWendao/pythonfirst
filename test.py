#!/usr/bin/env python
# -*-coding:utf-8-*-

# author:jakewendao

from selenium import webdriver
import unittest
import sys

class TestLogin(unittest.TestCase):

    
    def setUp(self):
        self.driver = webdriver.Firefox()

    def test_b(self):
        self.driver.get("http://www.baidu.com")
        title = self.driver.title
        print title
    def tearDown(self):
        self.driver.close()
    def test_a(self):
        self.driver.get("http://www.baidu.com")
        title = self.driver.title
        print title*2
        print 233


if __name__ == '__main__':
    unittest.main(verbosity=2)