from collections import OrderedDict #to order the dictionary like the given example
import csv,json

def landing_to_raw(url_csv,url_json):

    KEYS_TO_REPARSE = ["billing_address", "client_details", "customer", 
                        "fulfillments", "line_items", "payment_details", 
                        "shipping_address", "shipping_lines", "transactions"]

    result=OrderedDict()
    data=[]

    #Open CSV file. Only Read access.
    with open(url_csv,'r') as csvFile:
        reader = csv.DictReader(csvFile)
        for row in reader:
            
            # Parse the keys that I need to and are not empty
            new_line = {k: json.loads(v) if k in KEYS_TO_REPARSE and v != "" else v for k, v in row.items()}

            #Removes the metadata and saves it in a new index with the names that we need (the cols should always be the same).
            ## I use pop so the data_raw can have data of the rest of the columns, without the metadata
            ##it doesn't matter if the columns change.
            result["daton_user_id"] = new_line.pop('_job_batch_id')
            result["daton_batch_runtime"] = new_line.pop('_job_batch_runtime')
            result["daton_batch_id"] = new_line.pop('_job_user_id')
            result["creation_ts"] = new_line.pop('updated_at')
            result["data_raw"] = new_line

            #Order the dictionary so it can be like the example
            result.move_to_end('data_raw',last=False)
            data.append(result)
        
        
    #Open TXT file. Write access. It starts appending the dictionaries in the first iteration.
    with open(url_json,'w') as jsonFile:
        json.dump(data, jsonFile)

