from bitbucket_webhooks_router import decorators


@decorators.handle_repo_push
def sample_repo_push_handler_1(event):
    pass


@decorators.handle_repo_push
def sample_repo_push_handler_2(event):
    pass


@decorators.handle_pr_approval
def sample_pr_approval_handler(event):
    pass


def test_handlers():
    assert len(decorators.handle_repo_push.methods) == 2
    assert len(decorators.handle_pr_approval.methods) == 1