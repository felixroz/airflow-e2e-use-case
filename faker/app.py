from custom_provider import MarketProvider

import boto3
from deltalake.writer import write_deltalake
import datetime
import json
from faker import Faker
import numpy as np
import pandas as pd 
import os


fake = Faker()
fake.add_provider(MarketProvider)

os.environ['AWS_S3_ALLOW_UNSAFE_RENAME'] = 'true'

MINIO_USER = os.getenv('MINIO_USER')
MINIO_KEY = os.getenv('MINIO_KEY')
MINIO_ENDPOINT_URL = os.getenv('MINIO_ENDPOINT_URL')

s3 = boto3.client(
    's3', 
    endpoint_url=MINIO_ENDPOINT_URL, 
    aws_access_key_id=MINIO_USER, 
    aws_secret_access_key=MINIO_KEY
)

complete_name = fake.name()
complete_name_split = complete_name.split(' ')
first_name = ' '.join(complete_name_split[::-1])
last_name = complete_name_split[-1]
email = fake.email()
item = fake.product()
item_quantity = np.random.randint(low=0,high=10)


dict_record = {
    "first_name":first_name,
    "last_name":last_name,
    "email":email,
    "item":item,
    "item_quantity":item_quantity
}

json_record = json.dumps(dict_record)

dt = datetime.datetime.now()
dt_str = dt.strftime("%Y_%-m_%-d_%-H_%-M_%-S_%f")[:-3]


bucket_name = 'landing'
file_path = f"/market_random_data/json/"
file_name = f"market_{dt_str}.json"
object_key = file_path + file_name

response = s3.put_object(
    Bucket=bucket_name, 
    Key=object_key, 
    Body = json_record
)

# Check if the response was successful
if response['ResponseMetadata']['HTTPStatusCode'] == 200:
    print('JSON file written to S3 successfully!')
else:
    print('Failed to write JSON file to S3.')
