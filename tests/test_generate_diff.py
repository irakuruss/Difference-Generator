def test_generate_diff():
    file1 = 'fixtures/file1.json'
    file2 = 'fixtures/file2.json'
    with open('fixtures/result.txt', 'r') as result:
        result_string = n.join(result.read().splitlines())
        assert generate_diff(file1, file2) == result_string

