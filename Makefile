.PHONY: test

deps:
		pip install -r requirements.txt
test:
		PHONYPATH=. py.test
