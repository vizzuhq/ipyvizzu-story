.PHONY: clean \
	clean-dev update-dev-req install-dev-req install install-kernel touch-dev \
	check format check-format lint check-typing test-wo-install test \
	clean-doc doc \
	clean-build build-release check-release release

VIRTUAL_ENV = .venv

DEV_BUILD_FLAG = $(VIRTUAL_ENV)/DEV_BUILD_FLAG



clean: clean-dev clean-doc clean-build



# init

clean-dev:
	rm -rf $(VIRTUAL_ENV)

update-dev-req: $(DEV_BUILD_FLAG)
	$(VIRTUAL_ENV)/bin/pip-compile --upgrade dev-requirements.in

install-dev-req:
	$(VIRTUAL_ENV)/bin/pip install -r dev-requirements.txt

install:
	$(VIRTUAL_ENV)/bin/python setup.py install

install-kernel:
	$(VIRTUAL_ENV)/bin/ipython kernel install --name ".venv" --user

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
	$(VIRTUAL_ENV)/bin/black src tests docs setup.py

check-format: $(DEV_BUILD_FLAG)
	$(VIRTUAL_ENV)/bin/black --check src tests docs setup.py

lint: $(DEV_BUILD_FLAG)
	$(VIRTUAL_ENV)/bin/pylint src tests setup.py

check-typing: $(DEV_BUILD_FLAG)
	$(VIRTUAL_ENV)/bin/mypy src tests setup.py

test-wo-install: $(DEV_BUILD_FLAG)
	mkdir -p docs/coverage
	$(VIRTUAL_ENV)/bin/coverage run --data-file docs/coverage/.coverage --branch --source ipyvizzustory -m unittest discover tests
	$(VIRTUAL_ENV)/bin/coverage html --data-file docs/coverage/.coverage -d docs/coverage
	$(VIRTUAL_ENV)/bin/coverage report --data-file docs/coverage/.coverage -m --fail-under=100

test: $(DEV_BUILD_FLAG) install test-wo-install



# doc

clean-doc:
	rm -rf docs/coverage
	rm -rf docs/ipyvizzustory
	rm -rf `find docs -name '*.html'`
	rm -rf `find docs -name '*.js'`
	rm -rf `find docs -name '.ipynb_checkpoints'`

doc: $(DEV_BUILD_FLAG)
	$(VIRTUAL_ENV)/bin/pdoc --docformat google src/ipyvizzustory -o docs
	$(VIRTUAL_ENV)/bin/jupyter nbconvert --to html --template classic --execute ./docs/examples/**/*.ipynb



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
