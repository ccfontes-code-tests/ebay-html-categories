#!/usr/bin/python

import sys, os
my_path = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, my_path + '/../')

import unittest
from categories import *

# fixtures

page_category_land = {'CategoryID': 10542,
                      'BestOfferEnabled': 'true',
                      'CategoryLevel': 2,
                      'CategoryName': 'Land'}

formated_category_name = {'CategoryName': '&nbsp;&nbsp;&nbsp;&nbsp;Land'}

formated_page_category_land = {**page_category_land, **formated_category_name}

non_page_category_land = {'LeafCategory': 'true', 'LSD': 'true'}

category_land = {**page_category_land, **non_page_category_land}

class test_categories(unittest.TestCase):
    def test_remove_non_page_category_keys(self):
        res = remove_non_page_category_keys(category_land)
        return self.assertEqual(page_category_land, res)

    def test_format_category_keys(self):
        res = format_category_keys(page_category_land)
        return self.assertEqual(res, formated_page_category_land)

if __name__ == '__main__':
    with unittest.main() as main: pass