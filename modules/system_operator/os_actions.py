import os

def list_dir():
    return os.listdir()

def mkdir(dir_name: str):
    return os.mkdir(dir_name)

def rename_file(old: str, new: str):
    return os.rename(old, new)

def move_file(old_path: str, new_path: str):
    return os.rename(old_path, new_path)

def delete_dirs(dir_path_name: str):
    return os.removedirs(dir_path_name)

def cd(dir: str):
    return os.chdir(dir)
