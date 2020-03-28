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


handle_repo_push = BaseHandler()
handle_pr_approved = BaseHandler()
handle_pr_unapproved = BaseHandler()
handle_pr_created = BaseHandler()
handle_pr_updated = BaseHandler()
handle_pr_merged = BaseHandler()
handle_pr_declined = BaseHandler()
