#!/bin/bash

# Define the directory containing files to be uploaded
backup_folder="/home/ubuntu/backup"

# Define the S3 bucket name
s3_bucket="rds-geetanj-backup"

# Assume IAM role and upload files to S3 bucket
aws s3 cp "$backup_folder" s3://"$s3_bucket" --recursive

# Check if upload was successful
if [ $? -eq 0 ]; then
    echo "Files successfully uploaded to S3 bucket $s3_bucket"
else
    echo "Error uploading files to S3 bucket $s3_bucket"
fi

#* * * * * /home/ubuntu/backup/s3_backup.sh