import os

filename = 'budget.txt'
data_dir = 'data'


def get_file_path(filename):
    curren_dir_path = os.getcwd()
    filepath = os.path.join(curren_dir_path, data_dir, filename)
    return filepath


def read_budget(file_path):
    with open(file_path, 'r') as f:
        c_budget = f.read()
        return c_budget


path = get_file_path(filename)
current_budget = float(read_budget(path))

if __name__ == '__main__':
    read_budget(path)
