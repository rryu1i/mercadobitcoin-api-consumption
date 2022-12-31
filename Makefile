.PHONY: install virtualenv ipython clean pflake8


install:
	@echo "Installing for dev environment"
	@.venv/bin/python -m pip install -e '.[test,dev]'


vritualenv:
	@.venv/bin/python -m pip -m venv .venv


ipython:
	@.venv/bin/ipython


test:
	@.venv/bin/pytest -s --forked


testci:
	@pytest -v --junitxml=test-result.xml


watch:
	# @.venv/bin/ptw
	@ls **/*.py | entr pytest --forked


clean:            ## Clean unused files.
	@find ./ -name '*.pyc' -exec rm -f {} \;
	@find ./ -name '__pycache__' -exec rm -rf {} \;
	@find ./ -name 'Thumbs.db' -exec rm -f {} \;
	@find ./ -name '*~' -exec rm -f {} \;
	@rm -rf .cache
	@rm -rf .pytest_cache
	@rm -rf .mypy_cache
	@rm -rf build
	@rm -rf dist
	@rm -rf *.egg-info
	@rm -rf htmlcov
	@rm -rf .tox/
	@rm -rf docs/_build


lint:  # analise estatica
	@.venv/bin/pflake8


fmt:
	@.venv/bin/isort --profile=black -m 3 mercado_bitcoin tests
	@.venv/bin/black mercado_bitcoin tests


build:
	@python setup.py sdist bdist_wheel


publish-test:
	@twine upload --repository testpypi dist/*
