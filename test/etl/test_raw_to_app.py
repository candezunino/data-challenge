from core.etl.raw_to_app import raw_to_app
import pandas as pd
import numpy as np
import datetime
import json
import os
import unittest


class TestCSVtoJSON(unittest.TestCase):
    def test_main_execution(self):
        
        """This will test if the tables are parquet type and the number of columns and types are correct"""
        
     #   raw_to_app('test_table', '../../db/raw/unknown.json')
        TYPES_TO_CHECK={'id':np.integer,'order_number':np.integer,'user_id':np.integer,'total_price_usd':np.float64,'total_price':np.float64,'creation_ts':pd.Timestamp}

        df_dim=pd.read_parquet('../../db/app/dim_table4.gzip')
        self.assertEqual(len(df_dim.columns), 6)

        for k,i in TYPES_TO_CHECK.items():
           self.assertTrue(isinstance(df_dim.iloc[0][k], i))

        TYPES_TO_CHECK_AGG={'creation_dt':datetime.date,'total_orders_qty':np.integer,'total_sales_amount':np.float64}

        df_agg=pd.read_parquet('../../db/app/agg_table4.gzip')
        self.assertEqual(len(df_agg.columns), 3)

        for k,i in TYPES_TO_CHECK_AGG.items():
           self.assertTrue(isinstance(df_agg.iloc[0][k], i))

if __name__ == "__main__":
    unittest.main()