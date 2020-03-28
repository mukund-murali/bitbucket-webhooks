from typing import Callable
from typing import List


class BaseHandler:
    def __init__(self) -> None:
        self.handlers: List[Callable] = []

    def __call__(self, method: Callable) -> Callable:
        self.handlers.append(method)
        return method

    def get_methods(self) -> List[Callable]:
        return self.handlers


repo_push = BaseHandler()
pr_approved = BaseHandler()
pr_unapproved = BaseHandler()
pr_created = BaseHandler()
pr_updated = BaseHandler()
pr_merged = BaseHandler()
pr_declined = BaseHandler()
pr_comment_created = BaseHandler()
pr_comment_updated = BaseHandler()
pr_comment_deleted = BaseHandler()
