START_INDENT = 4
INDENT = ' '


def stringify(value, depth=0):
    if isinstance(value, dict):
        result = ['{']
        for key, nest_value in value.items():
            if isinstance(nest_value, dict):
                new_value = stringify(nest_value, depth + START_INDENT)
                result.append(f'{INDENT * depth}    {key}: {new_value}')
            else:
                result.append(f'{INDENT * depth}    {key}: {nest_value}')
        result.append(f'{INDENT * depth}}}')
        return '\n'.join(result)
    elif isinstance(value, bool):
        return str(value).lower()
    elif value is None:
        return 'null'
    else:
        return str(value)


def get_marker(marker):
    markers = {
        'added': '+',
        'removed': '-',
        'nothing': ' '
    }
    return f'{INDENT * 2}{markers[marker]}{INDENT}'


def string_constructor(depth, marker, key, value):
    return f'{INDENT * depth}{get_marker(marker)}{key}: ' \
           f'{stringify(value, depth + START_INDENT)}'


def format_to_stylish(tree, depth=0): # noqa: format_to_stylish
    result = ['{']
    for node in tree:
        if node['type'] == 'identical':
            result.append(string_constructor(
                depth, 'nothing', node['key'], node['value']
            ))

        elif node['type'] == 'added':
            result.append(string_constructor(
                depth, 'added', node['key'], node['value']
            ))

        elif node['type'] == 'removed':
            result.append(string_constructor(
                depth, 'removed', node['key'], node['value']
            ))

        elif node['type'] == 'changed':
            result.append(string_constructor(
                depth, 'removed', node['key'], node['old_value']
            ))
            result.append(string_constructor(
                depth, 'added', node['key'], node['new_value']
            ))

        elif node['type'] == 'nested':
            result.append(
                f"{INDENT * depth}    {node['key']}:"
                f" {format_to_stylish(node['children'], depth + START_INDENT)}")

    result.append(f'{INDENT * depth}}}')
    return '\n'.join(result)
