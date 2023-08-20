from gendiff.formatter.stylish import style_formatter


def test_style_formatter():
    assert style_formatter(True) == 'true'
    assert style_formatter(False) == 'false'
    assert style_formatter(24) == '24'

