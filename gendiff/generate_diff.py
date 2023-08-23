from gendiff.to_format import to_format
from gendiff.get_diff_tree import get_diff_tree
from gendiff.load_data import load_data


def generate_diff(path1, path2, formatter='stylish'):
    data1 = load_data(path1)
    data2 = load_data(path2)
    diff_tree = get_diff_tree(data1, data2)
    result = to_format(diff_tree, formatter)
    return result
