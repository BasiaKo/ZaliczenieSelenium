.PHONY: test

deps:
		pip install -r requirements.txt
test:
		PHONYPATH=. python3 tests/test_suite.py
