import boto3
import os, time, json, uuid, sys, random, string
import traceback

#TABLE_NAME = os.environ['TableName']
#PAYLOAD_SIZE = os.environ['PayloadSize']
TABLE_NAME= "traffic_test"

payload = {'size':10000, 'body': 'this is the body'}


dynamodb = boto3.resource('dynamodb')
table = dynamodb.Table(TABLE_NAME)

def _response(body):
    response = {
        'statusCode': 200,
        'body': body,
        'headers': {
            'Content-Type': 'application/json',
            'Access-Control-Allow-Origin': '*'
        },
    }
  
    return response

def get_random_string(length):
    # choose from all lowercase letter
    letters = string.ascii_lowercase
    result_str = ''.join(random.choice(letters) for i in range(length))
    return result_str
   

def _build_payload_with_size(size):
   
   print('building payload')
   payload['size'] = size 
   payload['body'] = get_random_string(size)

def _build_payload(size):        
   
   if size != payload['size']:
    _build_payload_with_size(size)
   
    
   
def put(event, context):  
  try:
    size = int(json.loads(event['body'])['size'])
    print(size)
    _build_payload(size)
    pk = str(uuid.uuid4())
    sk = str(uuid.uuid4())  


    data = table.put_item(    
        Item={
            'PK': pk, 
            'SK': sk, 
            'Name':'testing',
            'Size': size,
            'TTL':  int(str( time.time()).split('.')[0]) + 60 * 10,
            'Body': payload['body']

        }
    )

    return _response('Item created successfully')
  except Exception as e:
        traceback.print_exception(*sys.exc_info())
        print(e)

def get(event, context):

   data = table.get_item(    
        Key={'PK':'STR111', 'SK':''}
   )
   print(data)
   return _response( json.dumps(data))
   
   