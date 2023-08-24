def get_diff_tree(data1, data2):
    all_keys = sorted(set(data1.keys()) | set(data2.keys()))
    diff_tree = []
    for key in all_keys:
        if key not in data1:
            child = {
                'type': 'added',
                'key': key,
                'value': data2[key]
            }
        elif key not in data2:
            child = {
                'type': 'removed',
                'key': key,
                'value': data1[key]
            }
        elif isinstance(data1[key], dict) and isinstance(data2[key], dict):
            child = {
                'type': 'nested',
                'key': key,
                'children': get_diff_tree(data1[key], data2[key])
            }
        elif data1[key] == data2[key]:
            child = {
                'type': 'identical',
                'key': key,
                'value': data1[key]
            }
        else:
            child = {
                'type': 'changed',
                'key': key,
                'old_value': data1[key],
                'new_value': data2[key]
            }
        diff_tree.append(child)
    return diff_tree
