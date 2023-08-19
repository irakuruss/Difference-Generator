def style_formatter(value):
    if isinstance(value, bool):
        return 'true' if value else 'false'
    else:
        return str(value)


def generate_result_string(tree, indent='  '):
    mark = {'removed': '-', 'added': '+', 'identical': ' '}
    result = []
    for i in tree:
        if i['type'] in ['removed', 'added', 'identical']:
            result.append(
                indent + mark[i['type']] +
                ' ' + style_formatter(i['key']) +
                ': ' + style_formatter(i['value'])
            )

        elif i['type'] == 'changed':
            result.append(
                '  ' + '-' + ' ' +
                style_formatter(i['key']) + ': ' +
                style_formatter(i['value'][0]))
            result.append(
                '  ' + '+' + ' ' + style_formatter(i['key']) + ': ' +
                style_formatter(i['value'][1]))
    return '{' + '\n' + '\n'.join(
        sorted(result, key=lambda x: x[4])
    ) + '\n' + '}'
