# bitbucket-webhooks
 
[![Build Status](https://travis-ci.com/mukund-murali/bitbucket-webhooks.svg?branch=master)](https://travis-ci.com/mukund-murali/bitbucket-webhooks)

Python library that makes bitbucket webhook API [event payloads](https://confluence.atlassian.com/bitbucket/event-payloads-740262817.html) available via decorators with payload serialized into python objects.


## Installation

```
$ pip install bitbucket-webhooks
```

## Quickstart

```python
from flask import Flask
from flask import request

from bitbucket_webhooks import event_schemas
from bitbucket_webhooks import hooks
from bitbucket_webhooks import router

app = Flask(__name__)


@app.route("/hooks", methods=["POST"])
def bb_webhooks_handler():
    router.route(request.headers["X-Event-Key"], request.json)
    return ("", 204)


@hooks.repo_push
def _handle_repo_push(event: event_schemas.RepoPush):
    print(f"One or more commits pushed to: {event.repository.name}"
```

[Here](https://github.com/mukund-murali/bitbucket-webhooks/tree/master/examples/sample_flask_app) is the full example.


## Webhook events supported

* repo:push
* pullrequest:created
* pullrequest:updated
* pullrequest:approved
* pullrequest:unapproved
* pullrequest:fulfilled
* pullrequest:rejected
* pullrequest:comment_created
* pullrequest:comment_updated
* pullrequest:comment_deleted
