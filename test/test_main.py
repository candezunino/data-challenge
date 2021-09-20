from core.main import main
from core.etl.landing_to_raw import landing_to_raw
from core.etl.raw_to_app import raw_to_app
import json
import os
import unittest


class TestMainFunction(unittest.TestCase):
    def test_main_execution(self):
        
        """This will test if the files were created correctly"""
        
        main('../db/landing/ecommerce/factory14/orders/839012383812.csv', 'tableTest')
        PATH = '../db/app/dim_tableTest.gzip'

        if os.path.isfile(PATH) and os.access(PATH, os.R_OK):
            print("File exists and is readable")
        else:
             print("Either the file is missing or not readable")
        

if __name__ == '__main__':
    unittest.main()