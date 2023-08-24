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


def format_to_plain(tree, start_path_key=''):
    result = []
    for node in tree:
        current_path_key = f'{start_path_key}{node["key"]}'
        if node['type'] == 'added':
            result.append(
                f"Property '{current_path_key}' "
                f"was added with value: "
                f"{stringify(node['value'])}")

        elif node['type'] == 'removed':
            result.append(f"Property '{current_path_key}' was removed")

        elif node['type'] == 'changed':
            result.append(
                f"Property '{current_path_key}'"
                f" was updated. From {stringify(node['old_value'])} "
                f"to {stringify(node['new_value'])}")

        elif node['type'] == 'nested':
            new_value = format_to_plain(
                node['children'], 
                f"{current_path_key}."
            )
            result.append(f"{new_value}")

    return '\n'.join(result)
