from gendiff.formatter.stylish import generate_result_string
from gendiff.get_diff_tree import get_diff_tree


def generate_diff(path1, path2):
    tree = get_diff_tree(path1, path2)
    result = generate_result_string(tree)
    return result
