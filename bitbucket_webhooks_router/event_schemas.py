from marshmallow import Schema, fields
from marshmallow import EXCLUDE

from bitbucket_webhooks_router import base_schemas


class RepoPush(Schema):
    class Meta:
        unknown = EXCLUDE

    actor = fields.Nested(base_schemas.User)
    repository = fields.Nested(base_schemas.Repository)


class PullRequestApproved(Schema):
    class Meta:
        unknown = EXCLUDE

    actor = fields.Nested(base_schemas.User)
    repository = fields.Nested(base_schemas.Repository)
    pullrequest = fields.Nested(base_schemas.PullRequest)
    approval = fields.Nested(ApprovalInfo)


class ApprovalInfo(Schema):
    date = fields.DateTime()
    user = fields.Nested(base_schemas.User)
