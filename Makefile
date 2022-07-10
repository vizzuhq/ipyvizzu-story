.PHONY: clean install clean-dev touch-dev dev check format check-format lint clean-test test test-wo-install clean-build build-release check-release release

VIRTUAL_ENV = .venv
DEV_BUILD_FLAG = $(VIRTUAL_ENV)/DEV_BUILD_FLAG

clean: clean-dev clean-build clean-test

dev: $(DEV_BUILD_FLAG)

$(DEV_BUILD_FLAG):
	python3 -m venv $(VIRTUAL_ENV)
	$(VIRTUAL_ENV)/bin/python -m pip install --upgrade pip
	$(VIRTUAL_ENV)/bin/pip install -r dev-requirements.txt
	$(VIRTUAL_ENV)/bin/python setup.py install
	$(VIRTUAL_ENV)/bin/ipython kernel install --name ".venv" --user
	touch $(DEV_BUILD_FLAG)

clean-dev:
	rm -rf $(VIRTUAL_ENV)

touch-dev:
	touch $(DEV_BUILD_FLAG)

update-dev-req:
	$(VIRTUAL_ENV)/bin/pip-compile --upgrade dev-requirements.in

check: check-format lint test

format: $(DEV_BUILD_FLAG)
	$(VIRTUAL_ENV)/bin/black src tests docs

check-format: $(DEV_BUILD_FLAG)
	$(VIRTUAL_ENV)/bin/black --check src tests docs

lint: $(DEV_BUILD_FLAG)
	$(VIRTUAL_ENV)/bin/pylint src tests

clean-test:
	rm -rf .coverage
	rm -rf htmlcov

test: install test-wo-install

test-wo-install: $(DEV_BUILD_FLAG)
	$(VIRTUAL_ENV)/bin/coverage run --branch --source ipyvizzustory -m unittest discover tests
	$(VIRTUAL_ENV)/bin/coverage html
	$(VIRTUAL_ENV)/bin/coverage report -m --fail-under=100

install:
	$(VIRTUAL_ENV)/bin/python setup.py install

clean-build:
	rm -rf build
	rm -rf dist
	rm -rf **/*.egg-info
	rm -rf **/__pycache__

build-release: $(DEV_BUILD_FLAG)
	$(VIRTUAL_ENV)/bin/python -m build

check-release: $(DEV_BUILD_FLAG)
	$(VIRTUAL_ENV)/bin/python -m twine check dist/*.tar.gz dist/*.whl

release: clean-build build-release check-release

doc: $(DEV_BUILD_FLAG)
	$(VIRTUAL_ENV)/bin/ipython kernel install --name ".venv" --user
	$(VIRTUAL_ENV)/bin/jupyter nbconvert --to html --template classic --execute ./docs/examples/index.ipynb