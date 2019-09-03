# https://docs.python-guide.org/writing/tests/
# enter py.test in terminal to start the test
# content of test_sample.py
def func(x):
    return x + 1 

def test_answer():
    assert func(3) == 4
