import json

from bitbucket_webhooks_router import event_schemas


with open("sample_data/repo_push.json", "r") as f:
    data = json.load(f)
    push_schema = event_schemas.RepoPush()
    loaded = push_schema.load(data)
    print(loaded)
