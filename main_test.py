import pytest
import re

def regex_test(expected, lines):
    i = 0 ; match = 0
    for token in expected:
        for j in range(i, len(lines)):
            res = re.search(token, lines[j])
            if res is not None:
                i = j + 1
                match += 1
                break
        else:
            print(f'\033[91m Not Found: {token} \033[0m')
            assert False, f'Expect: {expected}'
    else:
        print(f'\033[91m match count: {match} \033[0m')
        assert match == len(expected), f'Expect: {expected}'


@pytest.mark.T1
def test_main_1():
    # Range [2..20]: primes are 2 3 5 7 11 13 17 19
    with open('result1.txt', 'r') as f:
        lines = f.readlines()
    print(lines)
    lines = [line.strip() for line in lines]
    # All primes on one line: match a line containing 2, 7, 13, 19
    regex_test([r'2.*7.*13.*19'], lines)


@pytest.mark.T2
def test_main_2():
    # Range [2..50]: primes include 2 ... 47
    with open('result2.txt', 'r') as f:
        lines = f.readlines()
    print(lines)
    lines = [line.strip() for line in lines]
    # Match a line containing 2, 23, 47
    regex_test([r'2.*23.*47'], lines)


@pytest.mark.T3
def test_main_3():
    # Range [10..30]: primes are 11 13 17 19 23 29
    with open('result3.txt', 'r') as f:
        lines = f.readlines()
    print(lines)
    lines = [line.strip() for line in lines]
    # Match a line containing 11, 17, 29
    regex_test([r'11.*17.*29'], lines)


@pytest.mark.T4
def test_main_4():
    # Range [2..100]: primes include 2 ... 97
    with open('result4.txt', 'r') as f:
        lines = f.readlines()
    print(lines)
    lines = [line.strip() for line in lines]
    # Match a line containing 2, 53, 97
    regex_test([r'2.*53.*97'], lines)
