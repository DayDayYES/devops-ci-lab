.PHONY: install test lint docker-build all

install:
	python -m pip install -r requirements.txt

test:
	python -m pytest

lint:
	python -m ruff check .

docker-build:
	docker build -t devops-ci-lab:local .

all: lint test docker-build
