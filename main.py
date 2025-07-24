import utils
import os

script_dir = os.path.dirname(os.path.realpath(__file__))

files = utils.FileUtils(file_path=script_dir)
print(files.get_empty_folder())
