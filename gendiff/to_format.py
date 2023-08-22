from gendiff.formatter.stylish import format_to_stylish


def to_format(data, format_name='stylish'):
    if format_name == 'stylish':
        return format_to_stylish(data)
    else:
        raise ValueError('Unsupported format')

