import boto3

s3 = boto3.client("s3")

bucket = "attendancecicdsource6389"

s3.upload_file("app.zip", bucket, "app.zip")

print("Uploaded")