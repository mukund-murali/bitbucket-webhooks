import marshmallow_objects as mm

from bitbucket_webhooks_router import base_schemas


class ApprovalInfo(mm.Model):
    date = mm.fields.DateTime()
    user = mm.NestedModel(base_schemas.User)


class RepoPush(mm.Model):
    class Meta:
        unknown = mm.EXCLUDE

    actor = mm.NestedModel(base_schemas.User)
    repository = mm.NestedModel(base_schemas.Repository)


class PullRequestApproved(mm.Model):
    class Meta:
        unknown = mm.EXCLUDE

    actor = mm.NestedModel(base_schemas.User)
    repository = mm.NestedModel(base_schemas.Repository)
    pullrequest = mm.NestedModel(base_schemas.PullRequest)
    approval = mm.NestedModel(ApprovalInfo)


class PullRequestMerged(mm.Model):
    class Meta:
        unknown = mm.EXCLUDE

    actor = mm.NestedModel(base_schemas.User)
    repository = mm.NestedModel(base_schemas.Repository)
    pullrequest = mm.NestedModel(base_schemas.PullRequest)
