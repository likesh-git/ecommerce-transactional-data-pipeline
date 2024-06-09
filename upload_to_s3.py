import boto3
import datetime

current_date = datetime.datetime.now()

s3 = boto3.client("s3")
bucket_name = "ecommerce-transactional-data"


def upload_to_s3(filename, current_date):
    """Uploads a CSV file to S3 with Hive-style partitioning"""
    # Extract year, month, day from current_date
    year = current_date.year
    month = current_date.month
    day = current_date.day
    file_path = f"transactions/year={year}/month={month}/day={day}/{filename}"  # Hive-style partitioning
    s3.upload_file(f'{filename}', bucket_name, file_path)
    print(f"File uploaded to S3 Bucket {bucket_name}/{file_path}")
    return

upload_to_s3("transactions_2024-06-8.csv", current_date)
print("Uploaded")