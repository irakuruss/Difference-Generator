from gendiff.generate_diff import generate_diff
import pytest
import os


TEST_FILES = [
    ('file1.json', 'file2.json', 'result.txt', 'stylish'),
    ('file1.json', 'file2.json', 'result-plain.txt', 'plain'),
    ('file1.json', 'file2.json', 'result-json.txt', 'json'),
    ('file1.yml', 'file2.yml', 'result.txt', 'stylish'),
    ('file1.yml', 'file2.yml', 'result-plain.txt', 'plain'),
    ('file1.yml', 'file2.yml', 'result-json.txt', 'json'),
    ('file1.yaml', 'file2.yaml', 'result.txt', 'stylish'),
    ('file1.yaml', 'file2.yaml', 'result-plain.txt', 'plain'),
    ('file1.yaml', 'file2.yaml', 'result-json.txt', 'json'),
    ('file3.json', 'file4.json', 'result2.txt', 'stylish'),
    ('file3.json', 'file4.json', 'result2-plain.txt', 'plain'),
    ('file3.json', 'file4.json', 'result2-json.txt', 'json'),
    ('file3.yml', 'file4.yml', 'result2.txt', 'stylish'),
    ('file3.yml', 'file4.yml', 'result2-plain.txt', 'plain'),
    ('file3.yml', 'file4.yml', 'result2-json.txt', 'json'),
    ('file3.yaml', 'file4.yaml', 'result2.txt', 'stylish'),
    ('file3.yaml', 'file4.yaml', 'result2-plain.txt', 'plain'),
    ('file3.yaml', 'file4.yaml', 'result2-json.txt', 'json')
]

TEST_FILES_EXCEPTION = [
    ('file1.json', 'file2.json', 'txt'),
    ('file3.yml', 'file4.yml', 'doc')
]

TEST_FILES_EXCEPTION2 = [
    ('file1.pdf', 'file2.yaml'),
    ('file3.json', 'file4.pdf')
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


@pytest.mark.parametrize('file1, file2, formatter', TEST_FILES_EXCEPTION)
def test_exception(file1, file2, formatter):
    with pytest.raises(ValueError) as e:
        generate_diff(
            get_path(file1),
            get_path(file2),
            formatter)
        assert str(e.value) == 'Unsupported format'


@pytest.mark.parametrize('file1, file2', TEST_FILES_EXCEPTION2)
def test_exception2(file1, file2):
    with pytest.raises(ValueError) as e:
        generate_diff(
            get_path(file1),
            get_path(file2))
        assert str(e.value) == 'Unsupported data format: pdf'
