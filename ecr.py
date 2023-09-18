import boto3
aws_region = 'ap-northeast-1'

ecr_client = boto3.client("ecr", region_name=aws_region)

repository_name = "my-first-cloud-native-repo"
response = ecr_client.create_repository(repositoryName = repository_name)

repository_uri = response['repository']['repositoryUri']
print(repository_uri)