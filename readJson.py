# importing json and boto3(aws python) module
import json
import boto3

# Opening JSON file
f = open('C:\\Users\\hp\Downloads\\New folder\\data.json', 'r')

# loading json to data
data = json.load(f)

# logging credentials
client = boto3.resource('sqs', region_name='us-east-2',
                        aws_access_key_id="",
                        aws_secret_access_key="")

# Accesing the queue
queue = client.get_queue_by_name(QueueName='JsonMessage')

# running the loop to acess all user's data
for user in data['Users:']:

    body = user['UserName'] + "\n" + user['UserId'] + \
        "\n" + user['RegisterationCode']

    # sending message to SQS
    queue.send_message(MessageBody=body)

# printing json to terminal
    print(user)

f.close()
