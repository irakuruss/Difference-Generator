from gendiff.formatter.stylish import format_to_stylish
from gendiff.formatter.plain import format_to_plain
from gendiff.formatter.json import format_to_json


def to_format(tree, format_name='stylish'):
    if format_name == 'stylish':
        return format_to_stylish(tree)
    elif format_name == 'plain':
        return format_to_plain(tree)
    elif format_name == 'json':
        return format_to_json(tree)
    else:
        raise ValueError('Unsupported format')
