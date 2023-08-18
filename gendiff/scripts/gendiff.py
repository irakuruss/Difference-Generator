#!/usr/bin/env python3
from gendiff.parse_args import parse_args
from gendiff.generate_diff import generate_diff


def main():
    file1, file2 = parse_args()
    diff = generate_diff(file1, file2)
    print(diff)


if __name__ == '__main__':
    main()
