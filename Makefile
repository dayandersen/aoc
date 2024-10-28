.PHONY: run check format

run_no_lint:
	python3 src/main.py --day $(DAY) --year $(YEAR)

run: check print_args
	python3 src/main.py --day $(DAY) --year $(YEAR)

print_args:
	echo "day argument passed in as: ${DAY}"
	echo "year argument passed in as: ${YEAR}"

check: format
	mypy src

format:
	black src