import unittest
import json

from bitbucket_webhooks_router import event_schemas


class TestSchemaParsing(unittest.TestCase):

    def test_repo_push(self):
        with open("tests/sample_data/repo_push.json") as f:
            data = json.load(f)
        obj = event_schemas.RepoPush.load(data) 
        self.assertEqual(obj.actor.nickname, "mukundvis")
        self.assertEqual(obj.repository.name, "webhook-test-project")
