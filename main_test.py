import pytest
import re

def regex_test(expected, content):
    pos = 0
    for token in expected:
        res = re.search(token, content[pos:])
        if res is None:
            assert False, f'Expect: {token}'
        pos += res.start() + 1

@pytest.mark.T1
def test_main_1():
    # Range [2..20]: primes are 2 3 5 7 11 13 17 19
    content = open('result1.txt').read()
    print(content)
    regex_test([r'\b2\b', r'\b7\b', r'\b13\b', r'\b19\b'], content)

@pytest.mark.T2
def test_main_2():
    # Range [2..50]: primes include 2 ... 47
    content = open('result2.txt').read()
    print(content)
    regex_test([r'\b2\b', r'\b23\b', r'\b47\b'], content)

@pytest.mark.T3
def test_main_3():
    # Range [10..30]: primes are 11 13 17 19 23 29
    content = open('result3.txt').read()
    print(content)
    regex_test([r'\b11\b', r'\b17\b', r'\b29\b'], content)

@pytest.mark.T4
def test_main_4():
    # Range [2..100]: primes include 2 ... 97
    content = open('result4.txt').read()
    print(content)
    regex_test([r'\b2\b', r'\b53\b', r'\b97\b'], content)
