import pandas as pd 
import pymongo
import json

DATA_FILE_URL = "https://raw.githubusercontent.com/avnyadav/sensor-fault-detection/main/aps_failure_training_set1.csv"

if __name__== "__main__":
    df = pd.read_csv(DATA_FILE_URL)
    print(f"number of rows and columns {df.shape}")
    df.reset_index(drop = True, inplace = True)
    json_record = list(json.loads(df.T.to_json()).values())


    client = pymongo.MongoClient("mongodb://localhost:27017/neurolabDB")
    DATABASE_NAME = "aps"
    COLLECTION_NAME = "sensor"
    client[DATABASE_NAME][COLLECTION_NAME].insert_many(json_record)