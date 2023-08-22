from gendiff.load_data import load_data


TEST_FILES = [
    'tests/fixtures/file1.json',
    'tests/fixtures/file1.yml',
    'tests/fixtures/file1.yaml'
]


def test_load_data():
    for file in TEST_FILES:
        assert load_data(file) == {
            'host': 'hexlet.io',
            'timeout': 50,
            'proxy': '123.234.53.22',
            'follow': False
        }

