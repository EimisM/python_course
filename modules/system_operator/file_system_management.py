from os_actions import *

# List all files directories of the current path
print(list_dir())

# Create a new directorys
mkdir("first_dir")
mkdir("second_dir")
print(list_dir())

# Rename a file
rename_file("first_dir", "last_dir")
print(list_dir())

# Move a file
rename_file("last_dir", "second_dir/last_dir")
cd("second_dir")
print(list_dir())
cd("..")

# Delete a dir
delete_dirs("second_dir/last_dir")
print(list_dir())