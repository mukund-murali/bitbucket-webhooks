class handle_repo_push(object):
    methods: list = []

    def __init__(self, method: list) -> None:
        handle_repo_push.methods.append(method)


class handle_pr_approval(object):
    methods: list = []

    def __init__(self, method: list) -> None:
        handle_pr_approval.methods.append(method)
