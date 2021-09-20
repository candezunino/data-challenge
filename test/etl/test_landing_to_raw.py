from core.etl.landing_to_raw import landing_to_raw
import json
import os
import unittest


class TestLandingtoRaw(unittest.TestCase):
    def test_main_execution(self):
        
        """This will test that the columns that should be reparsed have been reparsed succesfully"""
        
        landing_to_raw('../../db/landing/ecommerce/factory14/orders/839012383812.csv', 'test.json')

        
        with open('test.json', 'r') as f:
            data = json.load(f)
            # For the first data waw, transactions is a list of a single element    
            first_transaction = data[0]['data_raw']['transactions']
            self.assertTrue(isinstance(first_transaction, list))
            self.assertEqual(len(first_transaction), 1)


    def tearDown(self):
        os.remove('test.json')

if __name__ == '__main__':
    unittest.main()