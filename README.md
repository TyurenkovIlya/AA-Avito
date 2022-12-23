# test_doctest
py -3 -m doctest -o ELLIPSIS -o NORMALIZE_WHITESPACE -v test_doctest.py > .\result_doctest.txt
# test_pytest_param
py -3 -m pytest -v test_pytest_param.py > .\result_pytest_param.txt
# test_unittest
py -3 -m unittest -v test_unittest.py 2> .\result_unittest.txt
# test_pytest
py -3 -m pytest -v test_pytest.py > .\result_pytest.txt
# test_unittest_mock
py -3 -m unittest -v test_unittest_mock.py 2> .\result_unittest_mock.txt
# Получение отчета покрытия
py -3 -m coverage run -m unittest test_unittest_mock.py
coverage report
# Save in html
py -3 -m coverage html
