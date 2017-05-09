.PHONY: all setup FORCE

all: scrape

FORCE:

setup: venv/.Python
venv/.Python:
	virtualenv venv

scrape: FORCE
	python3 -m scraper
