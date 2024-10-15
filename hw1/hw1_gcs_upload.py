from google.cloud import storage

storage_client = storage.Client()

# ask for bucket name
bucket_name = input("Enter a name for the new bucket: ")

is_bucket_exist = False
for bucket_item in storage_client.list_buckets():
    if bucket_name == bucket_item.name:
        print(f"Bucket {bucket_name} already exists.")
        bucket1 = storage_client.get_bucket(bucket_name)
        is_bucket_exist = True
        break

if not is_bucket_exist:
    print(f"Creating bucket {bucket_name}...")
    bucket1 = storage_client.create_bucket(bucket_name, location="us-west1")
    print(f"Bucket {bucket1.name} created.")

# ask for file name
file_name = input("Enter the name of the file to upload: ")

while file_name in storage_client.list_blobs(bucket1):
    print(f"File {file_name} already exists.")
    file_name = input("Enter the name of the file to upload: ")

print(f"Uploading file {file_name}...")
blob = bucket1.blob(file_name)
blob.upload_from_filename(file_name)
print(f"File {file_name} uploaded.")

# list all files in the bucket
for file in bucket1.list_blobs():
    print(file)