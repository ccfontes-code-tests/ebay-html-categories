ebay_html_categories
==========
HTML printing of eBay product categories.

### Install
----------
```
At least Python 3.5 is needed.

pip3 install xmltodict fn
```

### Usage
----------
```
% ./bin/categories --rebuild
% ./bin/categories --rebuild
% ./bin/categories --render 179281
% ./bin/categories --render 179022
% ls ./assets/179281.html
179281.html
% ls ./assets/179022.html
179022.html
% ./bin/categories --render 6666666666
No category with ID: 6666666666
```

### Run tests
----------
```
./ebay_html_categories/test/test_categories.py
```
