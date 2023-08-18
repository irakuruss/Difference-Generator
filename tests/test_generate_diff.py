def test_generate_diff():
    file1 = 'tests/fixtures/file1.json'
    file2 = 'tests/fixtures/file2.json'
    with open('tests/fixtures/result.txt', 'r') as result:
        result_string = n.join(result.read().splitlines())
        assert generate_diff(file1, file2) == result_string

