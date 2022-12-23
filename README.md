# test_1
py3 -m doctest -o ELLIPSIS -o NORMALIZE_WHITESPACE -v test_1.py > .\result_1.txt
# test_2
py3 -m pytest -v test_2.py > .\result_2.txt
# test_3
py3 -m unittest -v test_3.py 2> .\result_3.txt
# test_4
py3 -m pytest -v test_4.py > .\result_4.txt
# test_5
py3 -m unittest -v test5.py 2> .\result_5.txt
# Получение отчета покрытия
py3 -m coverage run -m unittest test_5.py
coverage report
# Save in html
py3 -m coverage html
