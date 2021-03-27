import boto3
import sys
import json

def getRegionList ():
    # Return a list of AWS Regions to scan for an instance
    ec2 = boto3.client('ec2')

    regionList = ec2.describe_regions()
    return regionList['Regions']

def scanForInstance (region, instance):
    ec2 = boto3.client('ec2', region_name=region)
    try:
        instance_details = ec2.describe_instances (
            InstanceIds=[
                instance
            ]
        )
        # If we are successful then we have the instacne for the region.
        return True
    except:
        return False

def listInstances (region):
    ec2 = boto3.client('ec2', region_name=region)
    try:
        instance_details = ec2.describe_instances ()
        if (len(instance_details['Reservations']) == 0):
            return False
        print ('Region : ' + region)
        for r in instance_details['Reservations']:
            for i in r['Instances']:
                print ('     InstanceId: ' + i['InstanceId'])
        return True
    except:
        return False



instance_id = ""
#print ('args len = ', len(sys.argv))

if (len(sys.argv) == 1):
    print ('EC2 Instance Finder')
    print ('Ussage: python3 FindInstance [command] [arg]')
    print ('FindInstance instance Instance-id')
    print ('\t Locate an instance by instance-id accross all regions')

region_list = getRegionList ()

if (sys.argv[1] == "instance"):
    if (len(sys.argv) == 2):
        # No instance id was provided
        print ('You must provide an instance ID')
        print ('Ussage FindInstance instance Instance-id')
    else:
        instance_id = sys.argv[2]
        print ('Finding instance id: ' + instance_id)

        for region in region_list:
            found_instance = scanForInstance (region['RegionName'], instance_id)
            if (found_instance):
                print ('Found instance id: ' + instance_id + ' in region ' + region['RegionName'])
                print ('https://' + region['RegionName'] + '.console.aws.amazon.com/ec2/v2/home?region=' + region['RegionName'] + '#Instances:search=' + instance_id)

elif (sys.argv[1] == "list"):
    for region in region_list:
        listInstances (region['RegionName'])

#print ('Region List: ')
#list_of_regions = getRegionList ()
#for region in list_of_regions:
#    print (region['RegionName'])
