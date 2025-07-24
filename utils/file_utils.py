__all__ = ["list_files"]
import os


class FileUtils:

    def __init__(self, file_path):
        self.file_path = file_path

    def get_all_files(self):
        """
        Retrieve all files in the specified folder.
        Returns:
        list of str: A list containing the names of all files (not directories)
                     present in the folder specified by folder_path.
        """
        files = []

        for item in os.listdir(self.file_path):
            full_path = os.path.join(self.file_path, item)
            if os.path.isfile(full_path):
                files.append(item)
        return files

    def get_file_count(self):
        return len(self.get_all_files())

    def get_empty_folder(self):

        for root, folder, file in os.walk(self.file_path):
            print(file)


'''


def __get_all_files(folder_path):
  """
    Retrieve all files in the specified folder.

    Args:
        folder_path (str): The path to the directory to search for files.

    Returns:
        list of str: A list containing the names of all files (not directories)
                     present in the folder specified by folder_path.
    """
  files = []
  for item in os.listdir(folder_path):
    full_path = os.path.join(folder_path, item)
    if os.path.isfile(full_path):
      files.append(item)
  return files


def list_files(folder_path):
  # Public function that wraps the private one
  return __get_all_files(folder_path)


def count_files(folder_path):
  return len(__get_all_files(folder_path))


  '''
