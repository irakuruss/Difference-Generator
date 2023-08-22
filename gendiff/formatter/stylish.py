START_INDENT = 4
INDENT = ' '


def style_formatter(value, depth=0):
    if isinstance(value, dict):
        result = ['{']
        for key, nest_val in value.items():
            if isinstance(nest_val, dict):
                new_value = style_formatter(nest_val, depth + START_INDENT)
                result.append(f'{INDENT * depth}    {key}: {new_value}')
            else:
                result.append(f'{INDENT * depth}    {key}: {nest_val}')
        result.append(f'{INDENT * depth}}}')
        return '\n'.join(result)
    if isinstance(value, bool):
        return str(value).lower()
    if value is None:
        return 'null'
    return str(value)


def get_marker(sign):
    markers = {
        'added': '+',
        'removed': '-',
        'nothing': ' '
    }
    return f'{INDENT * 2}{markers[sign]}{INDENT}'


def string_constructor(depth, marker, key, value):
    return f'{INDENT * depth}{get_marker(marker)}{key}: ' \
           f'{style_formatter(value, depth + START_INDENT)}'


def format_to_stylish(tree, depth=0): # noqa: format_to_stylish
    result = ['{']
    for node in tree:
        if node['type'] == 'identical':
            result.append(string_constructor(
                depth, 'nothing', node['key'], node['value']
            ))

        if node['type'] == 'added':
            result.append(string_constructor(
                depth, 'added', node['key'], node['value']
            ))

        if node['type'] == 'removed':
            result.append(string_constructor(
                depth, 'removed', node['key'], node['value']
            ))

        if node['type'] == 'changed':
            result.append(string_constructor(
                depth, 'removed', node['key'], node['old_value']
            ))
            result.append(string_constructor(
                depth, 'added', node['key'], node['new_value']
            ))

        if node['type'] == 'nested':
            result.append(
                f"{INDENT * depth}    {node['key']}:"
                f" {format_to_stylish(node['children'], depth + START_INDENT)}")

    result.append(f'{INDENT * depth}}}')
    return '\n'.join(result)
