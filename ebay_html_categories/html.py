from string import Template
# fn.py
from operator import add
from fn.uniform import map, reduce

table_border_style = 'border:1px solid black;'

def table_row(row_dict):
    row_dict['style'] = 'style="' + table_border_style + 'text-align:center;"'
    return Template('<tr > \
    	             <td $style > $CategoryID </td> \
                     <td $style > $BestOfferEnabled </td> \
                     <td $style > $CategoryLevel </td> \
                     <td > $CategoryName </td> \
                     </tr>').substitute(row_dict)

def table_rows(row_dicts):
    return reduce(add, map(table_row, row_dicts))

def table(row_dicts):
    style = 'style="' + table_border_style + '"'
    return Template('<table $style > \
                     <tr > \
                     <th $style >ID</th> \
                     <th $style >Best Offer</th> \
                     <th $style >Level</th> \
                     <th $style >Name</th> \
                     </tr> \
                     $rows \
                     </table>').substitute(dict(rows=table_rows(row_dicts),
                     	                        style=style))

def page_layout(body):
    return Template('<html> \
    	             <head></head> \
    	             <body> \
    	             <div align=center> <h1>eBay category tree</h1> </div> \
    	             <div align=center> $body </div> \
    	             </body> \
    	             </html>').substitute(dict(body=body))

def ebay_categories_page(category_dicts):
    return page_layout(table(category_dicts))
