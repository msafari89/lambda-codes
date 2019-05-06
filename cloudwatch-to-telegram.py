# Wrote this to send notifications about CodePipeline to a specific telegram channel using a bot. Can be changed based on needs.
# It receives cloudwatch events as input, formats them based on needs and outputs them to the telegram channel using API. This is a work in progress.

import boto3
import json
from botocore.vendored import requests

def telegram_bot_sendtext(bot_message):
    
    bot_token = ''
    bot_chatID = ''
    URL = 'https://api.telegram.org/bot{0}/sendMessage?chat_id={1}&parse_mode=Markdown&text={2}'.format(bot_token, bot_chatID, bot_message)

    response = requests.get(URL)
    rjson = response.json()

    return rjson

def lambda_handler(event, context):
    rj = json.dumps(event)
    message = json.loads(rj)
    pipeline_name = str(message['detail']['pipeline'])
    stage_name = str(message['detail']['stage'])
    stage_status = str(message['detail']['state'])
    
    telegram_bot_sendtext("**Name:** {0}\nStage: {1}\nStatus: {2}".format(pipeline_name, stage_name, stage_status))
    return {
        'statusCode': 200
    }
