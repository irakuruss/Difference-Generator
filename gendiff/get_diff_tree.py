from gendiff.load_data import load_data


def get_diff_tree(path1, path2):
    data1 = load_data(path1)
    data2 = load_data(path2)
    all_keys = list(set(list(data1.keys()) + list(data2.keys())))
    diff_tree = []
    for key in all_keys:
        if key in data1 and key in data2:
            if data1[key] == data2[key]:
                diff_tree.append({
                    'type': 'identical',
                    'key': key,
                    'value': data1[key]
                })
            else:
                diff_tree.append({
                    'type': 'changed',
                    'key': key,
                    'value': [data1[key], data2[key]]
                })
        elif key in data1 and key not in data2:
            diff_tree.append({
                'type': 'removed',
                'key': key,
                'value': data1[key]
            })
        elif key not in data1 and key in data2:
            diff_tree.append({
                'type': 'added',
                'key': key,
                'value': data2[key]
            })
    return diff_tree
