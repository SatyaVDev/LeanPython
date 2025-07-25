__all__ = ["FileUtils"]
import os
from rich.console import Console
from rich.table import Table
import pandas as pd
from .helpers import Helper


class FileUtils:

    def __init__(self, file_path):
        self.file_path = file_path

    def get_all_files(self):
        """
        Retrieve all files in the specified folder.
        Returns:
            list of str: Names of all files (excluding directories).
        """
        files = []
        for item in os.listdir(self.file_path):
            full_path = os.path.join(self.file_path, item)
            if os.path.isfile(full_path):
                files.append(item)
        return files

    def get_file_count(self):
        """
        Count the number of files in the specified folder.
        """
        return len(self.get_all_files())

    def get_empty_folders(self):
        """
        Get a list of empty folders within the directory tree.

        Returns:
            list of str: Full paths of empty folders.
        """
        empty_folders = []
        for root, dirs, files in os.walk(self.file_path):
            if not dirs and not files:
                empty_folders.append(root)
        return empty_folders

    def format_and_print_folders(self, folders, title="Empty Folders"):
        """
        Display a list of folder paths in a well-formatted table using the 'rich' library.

        Args:
            folders (list): List of folder paths to display.
            title (str): Optional title for the table.
        """
        console = Console()

        if not folders:
            console.print("[bold red]No folders found.[/bold red]")
            return

        table = Table(title=title)
        table.add_column("#", style="cyan", justify="right")
        table.add_column("Folder Path", style="green")

        for i, path in enumerate(folders, 1):
            table.add_row(str(i), path)

        console.print(table)

    def __get_paginated_data(self, data, offset: int = 0, limit: int = 10000):
        df = pd.DataFrame([{"path": d} for d in data])
        paginated_df = df.iloc[offset:offset + limit]

        return paginated_df["path"].tolist()

    def __get_all_dirs(self, offset=0, limit=10):
        dirs = []
        for root, subdirs, files in os.walk(self.file_path):
            for subdir in subdirs:
                full_path = os.path.join(root, subdir)
                if os.path.isdir(
                        full_path):  # optional, since subdirs are from os.walk
                    dirs.append(full_path)

        # df = pd.DataFrame([{"path": d} for d in dirs])
        # # df.reset_index(drop=True, inplace=True)

        # # Apply offset and limit
        # paginated_df = df.iloc[offset:offset + limit]

        return dirs  # paginated_df['path'].tolist()

    def get_dir_with_size(self, offset=0, limit=10):
        all_dirs = self.__get_all_dirs()
        dir_list = self.__get_paginated_data(all_dirs, offset, limit)

        dict = []
        for dir in dir_list:
            size = os.path.getsize(dir)
            dict.append({"path": dir, "size": Helper.bytes_to_readable(size)})

        return dict
