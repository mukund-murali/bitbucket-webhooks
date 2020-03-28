import marshmallow_objects as mo

from bitbucket_webhooks import base_schemas


class RepoPush(mo.Model):
    class Meta:
        unknown = mo.EXCLUDE

    actor = mo.NestedModel(base_schemas.User)
    repository = mo.NestedModel(base_schemas.Repository)


# Pull request events
# https://confluence.atlassian.com/bitbucket/event-payloads-740262817.html#EventPayloads-Pullrequestevents


class PullRequestCreated(mo.Model):
    class Meta:
        unknown = mo.EXCLUDE

    actor = mo.NestedModel(base_schemas.User)
    repository = mo.NestedModel(base_schemas.Repository)
    pullrequest = mo.NestedModel(base_schemas.PullRequest)


class PullRequestUpdated(PullRequestCreated):
    pass


class PullRequestMerged(PullRequestCreated):
    pass


class PullRequestDeclined(PullRequestCreated):
    pass


class ApprovalInfo(mo.Model):
    date = mo.fields.DateTime()
    user = mo.NestedModel(base_schemas.User)


class PullRequestApproved(mo.Model):
    class Meta:
        unknown = mo.EXCLUDE

    actor = mo.NestedModel(base_schemas.User)
    repository = mo.NestedModel(base_schemas.Repository)
    pullrequest = mo.NestedModel(base_schemas.PullRequest)
    approval = mo.NestedModel(ApprovalInfo)


class PullRequestUnapproved(PullRequestApproved):
    pass


class PullRequestCommentCreated(mo.Model):
    actor = mo.NestedModel(base_schemas.User)
    repository = mo.NestedModel(base_schemas.Repository)
    pullrequest = mo.NestedModel(base_schemas.PullRequest)
    comment = mo.NestedModel(base_schemas.Comment)


class PullRequestCommentUpdated(PullRequestCommentCreated):
    pass


class PullRequestCommentDeleted(PullRequestCommentCreated):
    pass
