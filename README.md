# bitbucket-webhooks-router
 
[![Build Status](https://travis-ci.com/mukund-murali/bitbucket-webhooks-router.svg?branch=master)](https://travis-ci.com/mukund-murali/bitbucket-webhooks-router)

Routes bitbucket webhook [event payloads](https://confluence.atlassian.com/bitbucket/event-payloads-740262817.html) to easily consumable decorators.

Checkout the [example](https://github.com/mukund-murali/bitbucket-webhooks-router/tree/master/examples/sample_flask_app) flask app that handles bitbucket hooks using this library.

## Installation

```
$ pip install bb-hooks-router
```

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
