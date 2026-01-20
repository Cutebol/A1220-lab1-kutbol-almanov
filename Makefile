PY := python

.PHONY: run

run:
	PYTHONPATH=.. $(PY) -m lab_1.main receipts --print