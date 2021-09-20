# Solution

## Content Index
* [Github](#Github)
* [Jupyter Notebook](#Jupyter-Notebook)
* [Landing to Raw Pipeline](#Landing-to-Raw-Pipeline)
* [Raw to App Pipeline](#Raw-to-App-Pipeline)
* [Main execution](#Main-execution)
* [Unit test](#Unit-test)




## Github
> To clone or not to clone, that is the question.

I got a permission error when I tried to clone the following repository `git@gitlab.com:factory14/data-team/data-challenge.git`. So, I created a new one in my personal github and pushed the .zip folder that I received by email. 
To clone the repository `git clone git@github.com:candezunino/data-challenge.git`

## Jupyter Notebook
First I started working with Jupyter Notebook to get familiar with the files and language. In order to work with Jupyter and Github I had to converted the files in HTML format with `jupyter nbconvert --to html notebook_name.ipynb`
I attached everything related in the *notebook* folder.


### Landing to Raw Pipeline
> Be careful with the strings that are supposed to be lists!

I had to reparse some keys to convert the whole CSV in a json format, so I analized which ones had a string that was supposed to be a list, and I converted them. Then I extracted the data that I needed for each key, and changed the order so it can be like the example.
Other way to do this is to create a dictionary that the key is the old name column such as `_job_batch_id` and the value the new one `daton_user_id`, and with a dict comprehension load the items.

I use Python 3.

## Raw to App Pipeline  
In this step I just normalized the json, created a dataframe with the needed columns and data types and exported it to a parquet table.
> If you want to run `raw_to_app.py` you have to change the variable `path` with `'../../db/app/'` because now the variable is set for the execution of the main.

I use Pandas.

## Main execution:
Access to `core` folder and run `python main.py 'csv_url' 'table_parquet_name'` it will execute `landing_to_raw` and `raw_to_app`

e.g `python main.py '../db/landing/ecommerce/factory14/orders/839012383812.csv' 'orders'`

## Unit test:
In your terminal first set the path `export PYTHONPATH="main_url"`

Then you can run the unit test ` python test_main.py `

