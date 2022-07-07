.PHONY: install dev clean check format check-format lint

VIRTUAL_ENV = .venv
DEV_BUILD_FLAG = $(VIRTUAL_ENV)/DEV_BUILD_FLAG

install:
	$(VIRTUAL_ENV)/bin/python setup.py install

dev: $(DEV_BUILD_FLAG)

$(DEV_BUILD_FLAG):
	python3 -m venv $(VIRTUAL_ENV)
	$(VIRTUAL_ENV)/bin/python setup.py install
	$(VIRTUAL_ENV)/bin/pip install -r dev-requirements.txt
	$(VIRTUAL_ENV)/bin/ipython kernel install --name ".venv" --user
	touch $(DEV_BUILD_FLAG)

clean:
	rm -rf $(VIRTUAL_ENV)
	rm -rf build
	rm -rf dist
	rm -rf **/*.egg-info
	rm -rf **/__pycache__
	rm -rf .coverage
	rm -rf htmlcov

requirements:
	$(VIRTUAL_ENV)/bin/pip-compile --upgrade dev-requirements.in

check: check-format lint

format: $(DEV_BUILD_FLAG)
	$(VIRTUAL_ENV)/bin/black src

check-format: $(DEV_BUILD_FLAG)
	$(VIRTUAL_ENV)/bin/black --check src

lint: $(DEV_BUILD_FLAG)
	$(VIRTUAL_ENV)/bin/pylint src
