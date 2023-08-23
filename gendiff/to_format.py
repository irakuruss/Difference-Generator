from gendiff.formatter.stylish import format_to_stylish
from gendiff.formatter.plain import format_to_plain


def to_format(data, format_name='stylish'):
    if format_name == 'stylish':
        return format_to_stylish(data)
    elif format_name == 'plain':
        return format_to_plain(data)
    else:
        raise ValueError('Unsupported format')
