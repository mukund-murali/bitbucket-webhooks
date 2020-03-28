test:
	black --check --diff bitbucket_webhooks
	isort --check-only -rc bitbucket_webhooks
	mypy bitbucket_webhooks tests
	flake8 bitbucket_webhooks
	pytest

fmt:
	isort -rc .
	black .

release: test
	rm -rf dist
	python setup.py sdist bdist_wheel
	twine check dist/*
	twine upload dist/*
