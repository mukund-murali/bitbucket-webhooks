import datetime
import json

import pytest

from bitbucket_webhooks_router import event_schemas
from bitbucket_webhooks_router import hooks
from bitbucket_webhooks_router import router


def test_no_handler_available() -> None:
    assert router.route("random:event", {}) is None


def test_num_handlers() -> None:
    assert len(router._HANDLER_MAP) == 10


@hooks.repo_push
def _repo_push_handler_1(event: event_schemas.RepoPush) -> str:
    assert event.repository.name == "webhook-test-project"
    return "repo_pushed_1"


@hooks.repo_push
def _repo_push_handler_2(event: event_schemas.RepoPush) -> str:
    assert event.repository.name == "webhook-test-project"
    return "repo_pushed_2"


def test_repo_push_router() -> None:
    with open("tests/sample_data/repo_push.json") as f:
        data = json.load(f)
    assert router.route("repo:push", data) == ["repo_pushed_1", "repo_pushed_2"]


@hooks.pr_created
def _pr_created_handler(event: event_schemas.PullRequestCreated) -> str:
    assert event.pullrequest.title == "PR title"
    assert event.pullrequest.description == "PR description"
    assert event.pullrequest.source.branch.name == "feature-branch"
    assert event.pullrequest.destination.branch.name == "master"
    return "pr_created"


def test_pr_created_router() -> None:
    with open("tests/sample_data/pull_request_created.json") as f:
        data = json.load(f)
    assert router.route("pullrequest:created", data) == ["pr_created"]


@hooks.pr_approved
def _pr_approved_handler(event: event_schemas.PullRequestApproved) -> str:
    assert event.approval.user.display_name == "user2"
    assert event.approval.date == datetime.datetime(
        2020,
        3,
        28,
        12,
        27,
        1,
        368921,
        tzinfo=datetime.timezone(datetime.timedelta(0), "+0000"),
    )
    assert event.pullrequest.closed_by is None
    assert event.pullrequest.state == "OPEN"
    assert event.pullrequest.author.nickname == "mukundvis"
    assert event.repository.owner.nickname == "mukundvis"
    assert len(event.pullrequest.reviewers) == 1
    assert event.pullrequest.reviewers[0].nickname == "user2"
    assert len(event.pullrequest.participants) == 2
    participant_1 = event.pullrequest.participants[0]
    assert participant_1.role == "REVIEWER"
    assert participant_1.approved is True
    assert participant_1.user.nickname == "user2"
    participant_1 = event.pullrequest.participants[1]
    assert participant_1.role == "PARTICIPANT"
    assert participant_1.approved is False
    assert participant_1.user.nickname == "mukundvis"
    return "pr_approved"


def test_pr_approved_router() -> None:
    with open("tests/sample_data/pull_request_approved.json") as f:
        data = json.load(f)
    assert router.route("pullrequest:approved", data) == ["pr_approved"]


@hooks.pr_merged
def _pr_merged_handler(event: event_schemas.PullRequestMerged) -> str:
    assert event.pullrequest.state == "MERGED"
    assert event.pullrequest.merge_commit.hash == "19bdde53bbf1"
    assert event.pullrequest.closed_by.nickname == "mukundvis"
    return "pr_merged"


def test_pr_merged_router() -> None:
    with open("tests/sample_data/pull_request_merged.json") as f:
        data = json.load(f)
    assert router.route("pullrequest:fulfilled", data) == ["pr_merged"]


@hooks.pr_comment_created
def _pr_comment_created_handler(event: event_schemas.PullRequestCommentCreated) -> str:
    assert event.comment.content.raw == "New inline comment"
    assert event.comment.inline.path == "test.txt"
    assert event.comment.inline.to_line == 23
    assert event.comment.inline.from_line == 21
    return "pr_comment_created"


def test_pr_comment_created_router() -> None:
    with open("tests/sample_data/pr_comment_created.json") as f:
        data = json.load(f)
    assert router.route("pullrequest:comment_created", data) == ["pr_comment_created"]


@hooks.pr_comment_updated
def _pr_comment_updated_handler(event: event_schemas.PullRequestCommentUpdated) -> str:
    assert event.comment.content.raw == "New comment edited"
    assert event.comment.inline is None
    assert event.comment.created_on == datetime.datetime(2020, 3, 28, 8, 13, 4, 293869, tzinfo=datetime.timezone(datetime.timedelta(0), '+0000'))
    assert event.comment.updated_on == datetime.datetime(2020, 3, 28, 12, 1, 38, 182013, tzinfo=datetime.timezone(datetime.timedelta(0), '+0000'))
    assert event.comment.parent.id == 142468018
    assert event.pullrequest.comment_count == 4
    return "pr_comment_updated"


def test_pr_comment_updated_router() -> None:
    with open("tests/sample_data/pr_comment_updated.json") as f:
        data = json.load(f)


@hooks.pr_comment_deleted
def _pr_comment_deleted_handler(event: event_schemas.PullRequestCommentDeleted) -> str:
    assert event.comment.content.raw == ""
    return "pr_comment_deleted"


def test_pr_comment_deleted_router() -> None:
    with open("tests/sample_data/pr_comment_deleted.json") as f:
        data = json.load(f)
    assert router.route("pullrequest:comment_deleted", data) == ["pr_comment_deleted"]
