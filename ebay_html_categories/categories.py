#!/usr/bin/python

import sys
import xmltodict
from html import *
# fn.py
from fn.uniform import map
from fn import F

def str_indent(s, level):
    return '&nbsp;' * (level-1) * 4 + s

def remove_non_page_category_keys(category_dict):
    return {k: v for k,v in category_dict.items()
            if k not in ['LeafCategory', 'LSD']}

def apply_defaults_to_category_keys(category_dict):
    category_dict.setdefault('BestOfferEnabled', 'false')
    return category_dict

def format_category_keys(category_dict):
    new_category_dict = category_dict.copy()
    new_category_dict['CategoryLevel'] = int(new_category_dict['CategoryLevel']) # todo remove this when using db
    new_category_dict['CategoryID'] = int(new_category_dict['CategoryID']) # todo remove this when using db
    lvl = new_category_dict['CategoryLevel']
    new_category_dict['CategoryName'] = str_indent(new_category_dict['CategoryName'], lvl)
    return new_category_dict

def select_category_slice(category_dicts, category_id):
    start_idx = next(idx for idx,category_dict in enumerate(category_dicts)
                     if int(category_dict['CategoryID']) == category_id)
    end_idx = next(idx for idx,category_dict in enumerate(category_dicts[start_idx+1:])
                   if int(category_dict['CategoryLevel']) == 1)
    end_idx += start_idx
    return category_dicts[start_idx:end_idx]

def xml2dict_categories():
    with open('categories.xml') as xml_file:
        return xmltodict.parse(xml_file.read())['GetCategoriesResponse']['CategoryArray']['Category']

def render_category_tree(category_id):
    category_dicts = xml2dict_categories()
    category_dicts = select_category_slice(category_dicts, category_id)
    category_ops = F(format_category_keys) << remove_non_page_category_keys << apply_defaults_to_category_keys
    category_dicts = map(category_ops, category_dicts)
    with open('assets/' + str(category_id) + '.html', 'w') as html_categories_file:
        html_categories_file.write(ebay_categories_page(category_dicts))
        
if __name__ == '__main__':

    if sys.argv[1] == '--rebuild':
        from subprocess import check_output
        categories_xml = check_output(['./get_categories.sh']).decode('utf-8')
        with open('categories.xml', 'w') as categories_xml_file:
            categories_xml_file.write(categories_xml)

    elif sys.argv[1] == '--render':
        render_category_tree(int(sys.argv[2]))

    else: print(xml2dict_categories())
