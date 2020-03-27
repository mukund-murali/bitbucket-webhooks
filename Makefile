test:
	black --check --diff bitbucket_webhooks_router
	isort --check-only -rc bitbucket_webhooks_router
	mypy bitbucket_webhooks_router
	flake8 bitbucket_webhooks_router
	pytest

fmt:
	isort -rc bitbucket_webhooks_router
	black bitbucket_webhooks_router

release:
	python setup.py sdist bdist_wheel
	twine check dist/*
	twine upload dist/*
