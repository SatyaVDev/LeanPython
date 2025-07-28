from utils import FileUtils, Helper

# from project_100days import higher_lower_game
# import guess_the_number
import os

current_dir = "/mnt/c/Users/Satish/Downloads/"

script_dir = os.path.dirname(current_dir)
files = FileUtils(file_path=script_dir)

files.move_files_by_extension()


"""

empty_files = files.get_empty_folders()
result = files.get_dir_with_size()
sorted_list = Helper.sort_by_column(result, "size", ascending=False)

print(Helper.format(sorted_list))
"""
