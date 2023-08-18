import json


def generate_diff(file1, file2):
    with open(file1, 'r') as file1, open(file2, 'r') as file2:
        data1 = json.load(file1)
        data2 = json.load(file2)
    all_keys = sorted(list(set(list(data1.keys()) + list(data2.keys()))))
    general_info = []
    for key in all_keys:
        if key in data1 and key in data2:
            if data1[key] == data2[key]:
                general_info.append({
                    'type': 'identical',
                    'key': key,
                    'value': data1[key]
                })
            else:  # values are different
                general_info.append({
                    'type': 'changed',
                    'key': key,
                    'value': [data1[key], data2[key]]
                })
        elif key in data1 and key not in data2:
            general_info.append({
                'type': 'removed',
                'key': key,
                'value': data1[key]
            })
        elif key not in data1 and key in data2:
            general_info.append({
                'type': 'added',
                'key': key,
                'value': data2[key]
            })
    diff = generate_result_string(general_info)
    return diff


def generate_result_string(data):
    result = []
    for i in data:
        if i['type'] == 'removed':
            result.append(
                '  ' + '-' + ' ' + str(i['key']) + ': ' + str(i['value']))
        elif i['type'] == 'added':
            result.append(
                '  ' + '+' + ' ' + str(i['key']) + ': ' + str(i['value']))
        elif i['type'] == 'identical':
            result.append(
                '    ' + str(i['key']) + ': ' + str(i['value']))
        elif i['type'] == 'changed':
            result.append(
                '  ' + '-' + ' ' + str(i['key']) + ': ' + str(i['value'][0]))
            result.append(
                '  ' + '+' + ' ' + str(i['key']) + ': ' + str(i['value'][1]))
    return '{' + '\n' + '\n'.join(
        sorted(result, key=lambda x: x[4])
    ) + '\n' + '}'
