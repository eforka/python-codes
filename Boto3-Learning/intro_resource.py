import boto3 

iam = boto3.resource('iam')
policy_iterator = iam.policies.all()
print(policy_iterator)