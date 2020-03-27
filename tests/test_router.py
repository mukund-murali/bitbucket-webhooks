import json

import pytest

from bitbucket_webhooks_router import decorators
from bitbucket_webhooks_router import router


def test_no_handler_available():
    assert router.route("random:event", {}) is None


def test_num_handlers():
    assert len(router._HANDLER_MAP) == 7


@decorators.handle_repo_push
def _repo_push_handler(event):
    assert event.repository.name == "webhook-test-project"
    return "repo_pushed"


def test_repo_push_router():
    with open("tests/sample_data/repo_push.json") as f:
        data = json.load(f)
    assert router.route("repo:push", data) == ["repo_pushed"]


@decorators.handle_pr_created
def _pr_created_handler(event):
    assert event.pullrequest.title == "PR title"
    assert event.pullrequest.description == "PR description"
    return "pr_created"


def test_pr_created_router():
    with open("tests/sample_data/pull_request_created.json") as f:
        data = json.load(f)
    assert router.route("pullrequest:created", data) == ["pr_created"]
