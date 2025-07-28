from utils import FileUtils, Helper

import os

current_path = "/mnt/c/Users/Satish/"
script_dir = os.path.dirname(current_path)

files = FileUtils(file_path=script_dir)

for i in range(0, 5):

    empty_files = files.get_empty_folders(verbose=True, exclude=["php projects"])
    if len(empty_files) == 0:
        break

    # result = files.get_dir_with_size()
    # sorted_list = Helper.sort_by_column(result, "size", ascending=False)
    files.remove_dir(empty_files, ask_confirm=False)
