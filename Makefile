SOURCE := tupper.py
PYTHON := python3

run:
	$(PYTHON) $(SOURCE)

clean:
	rm -rf images/

.PHONY: clean run
