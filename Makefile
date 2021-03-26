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
	python bin/csv_dispatch.py pprint test/pprint_test.csv --module pprint --grouping_columns group
test_foo:
	python bin/csv_dispatch.py print_foo test/foo_test.csv --module csv_dispatcher.test_foo --grouping_columns group
test_foo_nogroups:
	python bin/csv_dispatch.py print_foo test/foo_test_nogroups.csv --module csv_dispatcher.test_foo 
test_foo2_nogroups:
	python bin/csv_dispatch.py foo2 test/foo2_test.csv --module csv_dispatcher.test_foo --cores 2

