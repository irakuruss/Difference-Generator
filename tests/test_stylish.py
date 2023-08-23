from gendiff.formatter.stylish import stringify


def test_style_formatter():
    assert style_formatter(True) == 'true'
    assert style_formatter(False) == 'false'
    assert style_formatter(24) == '24'

