import marshmallow_objects as mm


class User(mm.Model):
    class Meta:
        unknown = mm.EXCLUDE

    type = mm.fields.String()
    username = mm.fields.String()
    nickname = mm.fields.String()
    display_name = mm.fields.String()
    uuid = mm.fields.String()


class Project(mm.Model):
    class Meta:
        unknown = mm.EXCLUDE

    name = mm.fields.String()
    uuid = mm.fields.String()
    key = mm.fields.String()


class Repository(mm.Model):
    class Meta:
        unknown = mm.EXCLUDE

    name = mm.fields.String()
    full_name = mm.fields.String()
    website = mm.fields.String(allow_none=True)
    uuid = mm.fields.String()
    owner = mm.NestedModel(User)
    project = mm.NestedModel(Project)
    is_private = mm.fields.Boolean()


class Branch(mm.Model):
    class Meta:
        unknown = mm.EXCLUDE

    name = mm.fields.String()


class Commit(mm.Model):
    class Meta:
        unknown = mm.EXCLUDE

    hash = mm.fields.String()


class ChangeLocation(mm.Model):
    class Meta:
        unknown = mm.EXCLUDE

    repository = mm.NestedModel(Repository)
    branch = mm.NestedModel(Branch)
    commit = mm.NestedModel(Commit)


class PullRequest(mm.Model):
    class Meta:
        unknown = mm.EXCLUDE

    id = mm.fields.Int()
    title = mm.fields.String()
    description = mm.fields.String()
    # TODO: Change this to enum.
    state = mm.fields.String()
    author = mm.NestedModel(User)
    source = mm.NestedModel(ChangeLocation)
    destination = mm.NestedModel(ChangeLocation)
    merge_commit = mm.NestedModel(Commit, allow_none=True)
    participants = mm.fields.List(mm.NestedModel(User))
    reviewers = mm.fields.List(mm.NestedModel(User))
    closed_by = mm.NestedModel(User, allow_none=True)
    reason = mm.fields.String()
    created_on = mm.fields.DateTime()
    updated_on = mm.fields.DateTime()


class CommentContent(mm.Model):
    class Meta:
        unknown = mm.EXCLUDE

    raw = mm.fields.String()
    markup = mm.fields.String()
    html = mm.fields.String()


class InlineComment(mm.Model):
    to = mm.fields.Int()
    from_id = mm.fields.Int(allow_none=True, attribute="from")
    path = mm.fields.String()


class Comment(mm.Model):
    class Meta:
        unknown = mm.EXCLUDE

    id = mm.fields.Int()
    parent = mm.fields.Int(allow_none=True)
    content = mm.NestedModel(CommentContent)
    created_on = mm.fields.DateTime()
    updated_on = mm.fields.DateTime()
