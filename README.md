# About

CloudWatchLogs to Slack

# Installation

### Slack.com settings

[Slak.com Incoming Webhooks](https://api.slack.com/incoming-webhooks)

### Setup

```
pip -r requirements-dev.txt

# slack setting
vi function.py

# lambda-uploader setting
vi lambda.json

# lambda upload
lambda-uploader
# or ./build.sh and upload zip file from AWS ManagementConsole
```

# Test

```
python test.py
```
