# coding: utf-8
import json
from datetime import datetime, timedelta
from slack import Slack
import zlib
import base64

SLACK_INCOMING_WEBHOOK_URL = 'https://hooks.slack.com/services/XXXXXXXXXX'
#SLACK_USERNAME = 'CloudWatchLogs'
#SLACK_EMOJI = ':ghost:'
#SLACK_CHANNEL = '#slack_channel'

def lambda_handler(event, context):
    # cloudwatchlogs
    print 'event: ' + json.dumps(event, indent=2)
    data = zlib.decompress(base64.b64decode(event['awslogs']['data']), 16+zlib.MAX_WBITS)
    data_json = json.loads(data)
    print 'data: ' + json.dumps(data_json, indent=2)

    # slack setting
    slack = Slack(SLACK_INCOMING_WEBHOOK_URL)
    slack.username = SLACK_USERNAME
    slack.icon_emoji = SLACK_EMOJI
    slack.channel = SLACK_CHANNEL

    # generate post text
    for log in data_json["logEvents"]:
        log_json = json.loads(json.dumps(log, ensure_ascii=False))
        print 'log: ' + json.dumps(log_json, indent=2)
        date_jp = datetime.fromtimestamp(int(str(log_json["timestamp"])[:10])) + timedelta(hours=9)
        fields = []
        fields.append({'title': 'Time' ,'value': date_jp.strftime('%Y-%m-%d %H:%M:%S') ,'short': True})
        fields.append({'title': 'Owner' ,'value': data_json['owner'] ,'short': True})
        fields.append({'title': 'LogGroup' ,'value': data_json['logGroup'] ,'short': True})
        fields.append({'title': 'LogStream' ,'value': data_json['logStream'] ,'short': True})
        fields.append({'title': 'EventId' ,'value': log_json['id'] ,'short': True})
        fields.append({'title': 'SubscriptionFilters' ,'value': ''.join(data_json["subscriptionFilters"]) ,'short': True})
        text = []
        text.append({
            'title': 'CloudWatchLogs', 
            'color': 'danger', 
            'fallback': log_json['message'], 
            'pretext': log_json['message'], 
            'fields': fields
            })

        # post to slack
        slack.attachments = text
        slack.post()

