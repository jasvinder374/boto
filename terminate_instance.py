#!/usr/bin/env python
''' It should run like terminate_instances.py i-0c34e5ec790618146 '''
import sys
import boto3
ec2 = boto3.resource('ec2')
for instance_id in sys.argv[1:]:
    instance = ec2.Instance(instance_id)
    response = instance.terminate()
    print response
