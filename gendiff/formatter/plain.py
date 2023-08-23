def stringify(value):
    if isinstance(value, (dict, list)):
        return "[complex value]"
    elif value is None:
        return 'null'
    elif isinstance(value, bool):
        return str(value).lower()
    elif isinstance(value, str):
        return f"'{value}'"
    else:
        return str(value)


def format_to_plain(tree, path=''):
    result = []
    for node in tree:
        current_path = f'{path}{node["key"]}'
        if node['type'] == 'added':
            result.append(
                f"Property '{current_path}' "
                f"was added with value: "
                f"{stringify(node['value'])}")

        if node['type'] == 'removed':
            result.append(f"Property '{current_path}' was removed")

        if node['type'] == 'changed':
            result.append(
                f"Property '{current_path}'"
                f" was updated. From {stringify(node['old_value'])} "
                f"to {stringify(node['new_value'])}")

        if node['type'] == 'nested':
            new_value = format_to_plain(node['children'], f"{current_path}.")
            result.append(f"{new_value}")

    return '\n'.join(result)
