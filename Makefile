.PHONY: clean \
	clean-dev update-dev-req install-dev-req install-kernel install touch-dev \
	check format check-format lint check-typing clean-test test-wo-install test \
	clean-doc doc \
	clean-build build-release check-release release

VIRTUAL_ENV = .venv

DEV_BUILD_FLAG = $(VIRTUAL_ENV)/DEV_BUILD_FLAG



clean: clean-dev clean-test clean-doc clean-build



# init

clean-dev:
	rm -rf $(VIRTUAL_ENV)

update-dev-req: $(DEV_BUILD_FLAG)
	$(VIRTUAL_ENV)/bin/pip-compile --upgrade dev-requirements.in

install-dev-req:
	$(VIRTUAL_ENV)/bin/pip install -r dev-requirements.txt

install-kernel:
	$(VIRTUAL_ENV)/bin/ipython kernel install --name ".venv" --user

install:
	$(VIRTUAL_ENV)/bin/python setup.py install

touch-dev:
	touch $(DEV_BUILD_FLAG)

dev: $(DEV_BUILD_FLAG)

$(DEV_BUILD_FLAG):
	python3 -m venv $(VIRTUAL_ENV)
	$(VIRTUAL_ENV)/bin/python -m pip install --upgrade pip
	$(MAKE) -f Makefile install
	$(MAKE) -f Makefile install-dev-req
	$(MAKE) -f Makefile install-kernel
	$(VIRTUAL_ENV)/bin/pre-commit install --hook-type pre-commit --hook-type pre-push
	$(MAKE) -f Makefile touch-dev



# ci

check: check-format lint check-typing test

format: $(DEV_BUILD_FLAG)
	$(VIRTUAL_ENV)/bin/black src tests tools setup.py
	$(VIRTUAL_ENV)/bin/black -l 78 docs

check-format: $(DEV_BUILD_FLAG)
	$(VIRTUAL_ENV)/bin/black --check src tests tools setup.py
	$(VIRTUAL_ENV)/bin/black -l 78 --check docs

lint: $(DEV_BUILD_FLAG)
	$(VIRTUAL_ENV)/bin/pylint src tests tools setup.py

check-typing: $(DEV_BUILD_FLAG)
	$(VIRTUAL_ENV)/bin/mypy src tests tools setup.py

clean-test:
	rm -rf tests/coverage
	rm -rf `find docs -name '.test.*'`

test-wo-install: $(DEV_BUILD_FLAG)
	$(VIRTUAL_ENV)/bin/coverage run --data-file tests/coverage/.coverage --branch --source ipyvizzustory -m unittest discover tests
	$(VIRTUAL_ENV)/bin/coverage html --data-file tests/coverage/.coverage -d tests/coverage
	$(VIRTUAL_ENV)/bin/coverage report --data-file tests/coverage/.coverage -m --fail-under=100

test: $(DEV_BUILD_FLAG) install test-wo-install



# doc

clean-doc:
	rm -rf site
	rm -rf `find docs -name '.ipynb_checkpoints'`

doc: $(DEV_BUILD_FLAG)
	$(VIRTUAL_ENV)/bin/python tools/mkdocs/run_mkdocs.py $(VIRTUAL_ENV)/bin/mkdocs



# release

clean-build:
	rm -rf build
	rm -rf dist
	rm -rf `find . -name '*.egg-info'`
	rm -rf `find . -name '__pycache__'`

build-release: $(DEV_BUILD_FLAG)
	$(VIRTUAL_ENV)/bin/python -m build

check-release: $(DEV_BUILD_FLAG)
	$(VIRTUAL_ENV)/bin/python -m twine check dist/*.tar.gz dist/*.whl

release: clean-build build-release check-release
