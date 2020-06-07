.PHONY: test

deps:
		pip install -r requirements.txt
test:
		PYTHONPATH=${PYTHONPATH}:.:tests:pages python3 tests/test_suite.py
