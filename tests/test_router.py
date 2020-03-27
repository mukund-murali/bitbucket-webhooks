import datetime
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
    assert event.pullrequest.source.branch.name == "feature-branch"
    assert event.pullrequest.destination.branch.name == "master"
    return "pr_created"


def test_pr_created_router():
    with open("tests/sample_data/pull_request_created.json") as f:
        data = json.load(f)
    assert router.route("pullrequest:created", data) == ["pr_created"]


@decorators.handle_pr_approved
def _pr_approved_handler(event):
    assert event.approval.user.display_name == "Mukund Muralikrishnan"
    assert event.approval.date == datetime.datetime(
        2020, 3, 27, 21, 5, 8, 156574, tzinfo=datetime.timezone(datetime.timedelta(0), '+0000')
    )
    assert event.pullrequest.closed_by is None
    assert event.pullrequest.state == "OPEN"
    return "pr_approved"


def test_pr_approved_router():
    with open("tests/sample_data/pull_request_approved.json") as f:
        data = json.load(f)
    assert router.route("pullrequest:approved", data) == ["pr_approved"]


@decorators.handle_pr_merged
def _pr_merged_handler(event):
    assert event.pullrequest.state == "MERGED"
    assert event.pullrequest.merge_commit.hash == "19bdde53bbf1"
    assert event.pullrequest.closed_by.nickname == "mukundvis"
    return "pr_merged"


def test_pr_merged_router():
    with open("tests/sample_data/pull_request_merged.json") as f:
        data = json.load(f)
    assert router.route("pullrequest:fulfilled", data) == ["pr_merged"]