from google.cloud import storage

storage_client = storage.Client()

bucket_name = "cnguyen4_cpsc324_hw1_bucket1"

bucket1 = storage_client.create_bucket(bucket_name, location="us-west1")

print(f"Bucket {bucket1.name} created.")