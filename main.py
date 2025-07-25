import utils
import os
import utils

script_dir = os.path.dirname(os.path.realpath(__file__))

files = utils.FileUtils(file_path=script_dir)
empty_files = files.get_empty_folders()
result = files.get_dir_with_size()
sorted_list = utils.helpers.Helper.sort_by_column(result,
                                                  "size",
                                                  ascending=False)

print(utils.helpers.Helper.format(sorted_list))
