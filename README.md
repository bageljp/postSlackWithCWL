[![Code Climate](https://codeclimate.com/github/bageljp/postSlackWithCWL/badges/gpa.svg)](https://codeclimate.com/github/bageljp/postSlackWithCWL)
[![Test Coverage](https://codeclimate.com/github/bageljp/postSlackWithCWL/badges/coverage.svg)](https://codeclimate.com/github/bageljp/postSlackWithCWL/coverage)
[![Issue Count](https://codeclimate.com/github/bageljp/postSlackWithCWL/badges/issue_count.svg)](https://codeclimate.com/github/bageljp/postSlackWithCWL)

# About

CloudWatchLogs to Slack

![CloudWatchLogs to Slack.com](https://raw.githubusercontent.com/bageljp/postSlackWithCWL/master/img/slack.png "CloudWatchLogs to Slack.com")

# Installation

### Slack.com settings

[Slak.com Incoming Webhooks](https://api.slack.com/incoming-webhooks)

### Setup

```
pip -r requirements-dev.txt

# slack setting
vi function.py
```

### Deploy

using lambda-uploader.  
https://github.com/rackerlabs/lambda-uploader

```
# lambda-uploader setting
vi lambda.json

# lambda upload
lambda-uploader
```

or zip file upload.

```
./build.sh
# and upload zip file from AWS ManagementConsole.
```

# Test

```
python test.py
```
