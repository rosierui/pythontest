# how to test
py.test
py.test test* my*
py.test test* my* py*

$ cat run-2.sh
python -m pytest

$ cat run-3.sh
python -m pytest test_1.py

$ cat run.sh
python -m unittest mytest.py

$ python -m unittest mytest.py
$ py.test mytest.py

