# Makefile

PYTHON := python
PIP := pip
BLACK := black
PIPREQS := pipreqs

all: format dependencies

format:
	$(BLACK) .

dependencies:
	$(PIPREQS) . --force
