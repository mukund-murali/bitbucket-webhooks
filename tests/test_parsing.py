import json

from bitbucket_webhooks_router import event_schemas


def test_repo_push():
    with open("tests/sample_data/repo_push.json") as f:
        data = json.load(f)
    obj = event_schemas.RepoPush.load(data)
    assert obj.actor.nickname == "mukundvis"
    assert obj.repository.name == "webhook-test-project"
