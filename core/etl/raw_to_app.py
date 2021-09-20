import csv,json
import pandas as pd

def raw_to_app(table_name,url_json):
    with open(url_json) as f:
        data = json.loads(f.read())

    ###Map detailed table
    data_raw = [row["data_raw"] for row in data]

    #Export the columns of transactions needed
    df_transactions =  pd.json_normalize(data_raw,'transactions')
    df_ids=df_transactions.filter(['id','order_id'],axis=1).astype(int)

    #Export the columns of data_raw needed
    df_draw = pd.json_normalize(data_raw)
    df_price=df_draw.filter(['user_id','total_price_usd','total_price'],axis=1).astype({'user_id':int,'total_price_usd':float,'total_price':float})

    #Export the columns of general json
    df = pd.json_normalize(data)
    df_creation=df.filter(['creation_ts'],axis=1)
    df_creation=pd.to_datetime(df_creation.creation_ts)


    df_dim=pd.concat([df_ids,df_price,df_creation],axis=1)
    df_dim=df_dim.rename(columns={'order_id': 'order_number'})
    df_dim.to_parquet('../db/app/dim_'+table_name+'.gzip',
                compression='gzip') 
 
    ###Metrics table
    df_orders=df_transactions.filter(['created_at','order_id','amount'],axis=1).astype({'order_id':int,'amount':float})

    df_orders['created_at']=pd.to_datetime(df_orders['created_at']).dt.date

    df_metrics=df_orders.groupby('created_at', as_index=False).agg({'order_id':'count','amount': 'sum'})
    df_metrics=df_metrics.rename(columns={'created_at': 'creation_dt', 'order_id': 'total_orders_qty','amount':'total_sales_amount'})

    df_metrics.to_parquet('../db/app/agg_'+table_name+'.gzip',
                compression='gzip') 

