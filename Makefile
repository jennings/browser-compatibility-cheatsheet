.PHONY: all setup execute clean FORCE

all: execute

FORCE:

setup: v/.Python
venv/.Python:
	virtualenv v

execute: FORCE
	python -m scraper

clean: FORCE
	rm -f data.sqlite3 global_objects.html
