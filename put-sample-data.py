import boto3
from boto3.dynamodb.conditions import Key
import sys
from boto3 import resource
import json

dynamodb_resource = resource('dynamodb')


def main():
	table = dynamodb_resource.Table("doorman-dixonaws-data")

	sys.stdout.write('Inserting data into Dynamo table doorman-dixonaws-data... ')
	dictRow = {}
	dictRow['FaceId'] = "f35dc12b-8507-4412-a3d7-99455a3f710c"
	dictRow[
		'data'] = "{'name': 'John Dough', 'email': 'john@dough.com', 'mobile': '8888675309', 'cmdc_resident': 'false'}"

	response = table.put_item(Item=dictRow)

	if (response['ResponseMetadata']['HTTPStatusCode']) == 200:
		print("Insert successful, (RequestId: " + response['ResponseMetadata']['RequestId'] + ")")
	else:
		print(
			"Something went wrong: response code " + response['ResponseMetadata']['HTTPStatusCode'] + " from DynamoDB")

	print('Getting item from Dynamo table...')

	response = table.get_item(Key={'FaceId': 'f35dc12b-8507-4412-a3d7-99455a3f710c'})

	print(json.dumps(response['Item']['data'], indent=4, separators=(',', ': ')))


# this doesnt work because property name are expected in double quotes
# dictItem=json.loads(response['Item']['data'])


main()
