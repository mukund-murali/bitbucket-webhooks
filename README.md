# bitbucket-webhooks-router
 
[![Build Status](https://travis-ci.com/mukund-murali/bitbucket-webhooks-router.svg?branch=master)](https://travis-ci.com/mukund-murali/bitbucket-webhooks-router)

Routes bitbucket webhook [event payloads](https://confluence.atlassian.com/bitbucket/event-payloads-740262817.html) to easily consumable decorators.


## Installation

```
$ pip install bb-hooks-router
```

## Quickstart

```python
from bitbucket_webhooks_router import decorators
from bitbucket_webhooks_router import router
from flask import Flask
from flask import request

app = Flask(__name__)


@app.route("/hooks", methods=["POST"])
def bb_webhooks_handler():
    router.route(request.headers["X-Event-Key"], request.json)
    return ("", 204)


@decorators.handle_repo_push
def _handle_repo_push(event):
    print(f"One or more commits pushed to: {event.repository.name}"
```

[Here](https://github.com/mukund-murali/bitbucket-webhooks-router/tree/master/examples/sample_flask_app) is the full example.


## Bitbucket events supported

* repo:push
* pullrequest:created
* pullrequest:updated
* pullrequest:approved
* pullrequest:unapproved
* pullrequest:fulfilled
* pullrequest:rejected


## Links

[PyPI](https://pypi.org/project/bb-hooks-router/)
