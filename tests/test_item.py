import os
import unittest
import json
from tempfile import TemporaryDirectory
from datetime import datetime
import dateutil

from pystac import *
from pystac.utils import is_absolute_href
from tests.utils import (TestCases, RANDOM_GEOM, RANDOM_BBOX, test_to_from_dict)


class ItemTest(unittest.TestCase):
    def test_to_from_dict(self):
        m = TestCases.get_path('data-files/itemcollections/sample-item-collection.json')
        with open(m) as f:
            item_dict = json.load(f)['features'][0]
        
        test_to_from_dict(self, Item, item_dict)
        item = Item.from_dict(item_dict)
        self.assertEqual(item.get_self_href(), 'http://cool-sat.com/catalog/CS3-20160503_132130_04/CS3-20160503_132130_04.json')

        # test asset creation additional field(s)
        self.assertEqual(item.assets['analytic'].properties['product'], 'http://cool-sat.com/catalog/products/analytic.json')
        self.assertIsNone(item.assets['thumbnail'].properties)
            
        
