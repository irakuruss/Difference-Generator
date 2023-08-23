from gendiff.generate_diff import generate_diff
import pytest
import os


TEST_FILES = [
    ('file1.json', 'file2.json', 'result.txt', 'stylish'),
    ('file1.json', 'file2.json', 'result-plain.txt', 'plain'),
    ('file1.yml', 'file2.yml', 'result.txt', 'stylish'),
    ('file1.yml', 'file2.yml', 'result-plain.txt', 'plain'),
    ('file1.yaml', 'file2.yaml', 'result.txt', 'stylish'),
    ('file1.yaml', 'file2.yaml', 'result-plain.txt', 'plain'),
    ('file3.json', 'file4.json', 'result2.txt', 'stylish'),
    ('file3.json', 'file4.json', 'result2-plain.txt', 'plain'),
    ('file3.yml', 'file4.yml', 'result2.txt', 'stylish'),
    ('file3.yml', 'file4.yml', 'result2-plain.txt', 'plain'),
    ('file3.yaml', 'file4.yaml', 'result2.txt', 'stylish'),
    ('file3.yaml', 'file4.yaml', 'result2-plain.txt', 'plain')
]


def get_path(filename):
    return os.path.join('tests/fixtures', filename)


@pytest.mark.parametrize('file1, file2, result, formatter', TEST_FILES)
def test_generate_diff(file1, file2, result, formatter):
    with open(get_path(result), 'r') as res:
        result_string = '\n'.join(res.read().splitlines())
    assert generate_diff(
        get_path(file1),
        get_path(file2),
        formatter) == result_string

