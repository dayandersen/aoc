.PHONY: run check format

TEST ?= false

# Convert TEST to lowercase for case-insensitive comparison
TEST_LOWER = $(shell echo $(TEST) | tr A-Z a-z)

run_no_lint:
	python3 src/main.py --day $(DAY) --year $(YEAR)

run: check print_args
	python3 src/main.py --day $(DAY) --year $(YEAR) $(if $(filter true,$(TEST)),--test,--no-test)

print_args:
	echo "day argument passed in as: ${DAY}"
	echo "year argument passed in as: ${YEAR}"

check: format
	mypy src

format:
	black src