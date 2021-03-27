# FileTools
Repository for small file tools projects.

# Purpose
These file tools were created by me to suit certain use cases I had,
and to learn Python as I go. If you find them useful, be my guest and grab them.
The code is likely not going to be the best way to accomplish something, but it
serves the purpose of me figuring it out as I go.

# RetrieveFiles
This copies from a source tree to a destination tree.
Builds the directory structure as it goes.
Cleans (deletes) the source tree as the files are moved.
Skips directories that start with a .

# FindInstance
This is used to scan your AWS Account for a specific instance ID and let you know what region
the instance is in. Or to scan through your AWS Account and list all the instances by region.

FindInstance instance i-123456789
To search through all regions in your account for the specified instance.

```
FindInstance.py instance i-123456789
Finding instance id: i-123456789
Found instance id: i-123456789 in region us-east-2
https://us-east-2.console.aws.amazon.com/ec2/v2/home?region=us-east-2#Instances:search=i-123456789
```
or

FindInstance list
To search through all regions in your account, and list the instances in each region.

```
python3 FindInstance.py list
Region : us-east-2
     InstanceId: i-123456789
```
