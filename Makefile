make:
	echo "hello"
upload_test_pypi:
	rm -rf dist || True
	python setup.py sdist
	twine -r testpypi dist/* 
upload_pypi:
	rm -rf dist || True
	python setup.py sdist
	twine upload dist/*
py:
	python -m IPython
test_pprint:
	python bin/csv_dispatch.py pprint test/pprint_test.csv --module pprint --list_columns object
test_foo:
	python bin/csv_dispatch.py print_foo test/foo_test.csv --module csv_dispatcher.test_foo --list_columns x y --grouping_columns group

