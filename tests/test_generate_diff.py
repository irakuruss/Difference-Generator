from gendiff.generate_diff import generate_diff


def test_generate_diff():
    file1 = 'tests/fixtures/file1.json'
    file2 = 'tests/fixtures/file2.json'
    file3 = 'tests/fixtures/file1.yml'
    file4 = 'tests/fixtures/file2.yml'
    with open('tests/fixtures/result.txt', 'r') as result:
        result_string = "\n".join(result.read().splitlines())
        assert generate_diff(file1, file2) == result_string
        assert generate_diff(file3, file4) == result_string
