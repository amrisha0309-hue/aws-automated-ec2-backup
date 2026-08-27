import boto3
from datetime import datetime

ec2 = boto3.client('ec2')

def lambda_handler(event, context):

    volume_id = 'vol-0937230e2f44c1bc6'  # Fixed: removed leading space

    response = ec2.create_snapshot(
        VolumeId=volume_id,
        Description=f'Automated backup {datetime.now()}'
    )

    return {
        'statusCode': 200,
        'snapshot_id': response['SnapshotId']
    }
