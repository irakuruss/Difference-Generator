from gendiff.to_format import to_format
from gendiff.get_diff_tree import get_diff_tree
from gendiff.load_data import load_data
from gendiff.parser import parse, get_ext


def generate_diff(file1, file2, formatter='stylish'):
    file_data1, file_data2 = load_data(file1), load_data(file2)
    dict1 = parse(file_data1, get_ext(file1))
    dict2 = parse(file_data2, get_ext(file2))
    diff_tree = get_diff_tree(dict1, dict2)
    result = to_format(diff_tree, formatter)
    return result
