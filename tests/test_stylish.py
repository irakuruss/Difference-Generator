from gendiff.formatter.stylish import stringify


def test_style_formatter():
    assert stringify(True) == 'true'
    assert stringify(False) == 'false'
    assert stringify(24) == '24'
