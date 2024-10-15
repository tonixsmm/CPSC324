# Imports the Google Cloud client library
from google.cloud import storage

# Instantiates a client
storage_client = storage.Client()

# The name for the new bucket
bucket_name = "bucket2"

# Creates the new bucket
bucket = storage_client.create_bucket(bucket_name, location="us-west1")

print(f"Bucket {bucket.name} created.")