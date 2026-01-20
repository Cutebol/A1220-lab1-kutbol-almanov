VENV := .venv
PY   := $(VENV)/bin/python

.PHONY: run

run:
	$(PY) main.py --print