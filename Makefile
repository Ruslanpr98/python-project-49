#Makefile

install:
	poetry install

build:
	poetry build

publish:
	poetry publish --dry-run

package-install:
	python3 -m pip install dist/*.whl --force-reinstall

brain-games:
	poetry run brain_games

all-steps:
	poetry install
	poetry build
	poetry publish --dry-run
	python3 -m pip install dist/*.whl --force-reinstall
