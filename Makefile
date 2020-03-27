test:
	black --check --diff bitbucket_webhooks_router
	isort --check-only -rc bitbucket_webhooks_router
	mypy bitbucket_webhooks_router tests
	flake8 bitbucket_webhooks_router
	pytest

fmt:
	isort -rc .
	black .

release: test
	rm -rf dist
	python setup.py sdist bdist_wheel
	twine check dist/*
	twine upload dist/*
