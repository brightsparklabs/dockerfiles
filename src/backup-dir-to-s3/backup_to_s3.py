#!/usr/bin/env python3
# # -*- coding: utf-8 -*-

"""
Script to tar & gzip a directory, and upload the result to S3.
________________________________________________________________________________
Created by brightSPARK Labs
www.brightsparklabs.com
"""

# standard libraries
import os
from pathlib import Path
import tarfile
import tempfile

# vendor libraries
import boto3

# ------------------------------------------------------------------------------
# CONSTANTS
# ------------------------------------------------------------------------------

# Default directory to back up to S3
DEFAULT_DIRECTORY_TO_BACKUP: Path = Path("/backup")

# ------------------------------------------------------------------------------
# FUNCTIONS
# ------------------------------------------------------------------------------

def tar_backup_directory(directory_to_backup: Path, output_filename: str):
    """Tar and gzip a given directory, and return the Path to the output file.

    Args:
        directory_to_backup (str): The directory to tar and gzip.

    Returns:
        Path: Path to the gzip file containing the input directory.
    """

    output_directory = tempfile.mkdtemp()
    output_file = Path(output_directory).joinpath(output_filename)

    with tarfile.open(output_file, "w:gz") as tgz:
        tgz.add(directory_to_backup, arcname=os.path.basename(directory_to_backup))

    return output_file

def upload_to_s3(file_to_upload: Path, s3_upload_path: str, s3_bucket_name: str, s3_access_key: str, s3_secret_access_key: str):
    """Uploads a file to S3.

    Args:
        file_to_upload (Path): Path to the file to upload to S3.
        s3_upload_path (str): The path in S3 to store the file.
        s3_bucket_name (str): Name of the S3 bucket to store the file.
        s3_access_key (str): AWS access key to upload to the bucket.
        s3_secret_access_key (str): AWS secret access key to upload to the bucket.
    """
    s3_client = boto3.client('s3', aws_access_key_id=s3_access_key, aws_secret_access_key=s3_secret_access_key)
    s3_client.upload_file(file_to_upload, s3_bucket_name, s3_upload_path)

def main():
    backup_file = tar_backup_directory(DEFAULT_DIRECTORY_TO_BACKUP)

if __name__ == "__main__":
    main()
