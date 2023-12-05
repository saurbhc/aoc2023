from __future__ import annotations

import argparse
import os.path

import pytest

import support

INPUT_TXT = os.path.join(os.path.dirname(__file__), 'input.txt')

numbers = {
    "one": "1",
    "two": "2",
    "three": "3",
    "four": "4",
    "five": "5",
    "six": "6",
    "seven": "7",
    "eight": "8",
    "nine": "9",
}

def check_number(s: str, start=True) -> tuple[bool, str]:
    for number, num in numbers.items():
        if start and s.startswith(number):
            return True, num
        elif not start and s.endswith(number):
            return True, num
    return False, None


def compute(s: str) -> int:
    _sum = 0
    for line in s.splitlines():
        n = ""

        for idx, c in enumerate(line):
            if c.isdigit():
                n += c
                break
            else:
                _line = line[idx:] if idx else line
                is_number, num = check_number(_line, start=True)
                if is_number:
                    n += num
                    break

        reversed_line = line[::-1]
        for idx, c in enumerate(reversed_line):
            if c.isdigit():
                n += c
                break
            else:
                _line = line[:-idx] if idx else line
                is_number, num = check_number(_line, start=False)
                if is_number:
                    n += num
                    break

        _sum += int(n)

    return _sum

INPUT_S = '''\
two1nine
eightwothree
abcone2threexyz
xtwone3four
4nineeightseven2
zoneight234
7pqrstsixteen
'''
EXPECTED = 281


@pytest.mark.parametrize(
    ('input_s', 'expected'),
    (
        (INPUT_S, EXPECTED),
    ),
)
def test(input_s: str, expected: int) -> None:
    assert compute(input_s) == expected


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument('data_file', nargs='?', default=INPUT_TXT)
    args = parser.parse_args()

    with open(args.data_file) as f, support.timing():
        print(compute(f.read()))

    return 0


if __name__ == '__main__':
    raise SystemExit(main())
