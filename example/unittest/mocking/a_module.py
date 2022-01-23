"""
How to mock function in a module.
In a unit test we dont want to actually read a file so we will mock
the read_file_content() function. But still test get_number_of_line_in_file().
"""
def get_number_of_line_in_file():
    """
    Return how many lines exist in a file
    """
    content = read_file_content()
    nr_lines = 0
    for _ in content:
        nr_lines += 1
    return nr_lines

def read_file_content():
    """
    This function will be mocked
    """
    with open("a file.txt", encoding="utf-8") as fd:
        return fd.readlines()


def get_number_of_line_in_file_with_arg(filename):
    """
    Return how many lines exist in a file.
    The filename is sent as argument
    """
    content = read_file_content_with_arg(filename)
    nr_lines = 0
    for _ in content:
        nr_lines += 1
    return nr_lines


def read_file_content_with_arg(filename):
    """
    This function will be mocked and has an argument with can be asserted
    """
    with open(filename, encoding="utf-8") as fd:
        return fd.readlines()
