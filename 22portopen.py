import sys
import boto
from boto import ec2
connection=ec2.connect_to_region("us-east-1")
sg=connection.get_all_security_groups()
 
def getTag(instanceId):
 
    reservations=connection.get_all_instances(filters={'instance_id':instanceId})
    for res in reservations:
        for instance in res.instances:
            return instance.tags['Name']
 
try:
 
    for securityGroup in sg:
       for rule in securityGroup.rules:
           global instanceId;
           if rule.to_port == '22'  and '0.0.0.0/0' in str(rule.grants):
                           for instanceid in securityGroup.instances():
                                 instanceId=str(instanceid)
                                 print "Port 22 open for all IP:"
                                 print " SecurityGroupName: %s --> Instance Name: %s" %(securityGroup.name,  getTag(instanceId.split(':')[1]))
 
except :
    print 'Some Error occurred : '
    print sys.exc_info()
