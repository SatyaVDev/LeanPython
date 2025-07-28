__all__ = ["FileUtils"]
import os
from rich.console import Console
from rich.table import Table
import pandas as pd
from .helpers import Helper

import shutil


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

    def get_empty_folders(self, verbose=False, exclude=None):
        """
        Get a list of empty folders within the directory tree.

        Args:
            verbose (bool): Whether to print scanning progress.

        Returns:
            list of str: Full paths of empty folders.
        """
        empty_folders = []
        exclude = set(exclude or [])  # Handle None as an empty list

        # Walk bottom-up to ensure all subfolders are checked before parents
        for root, dirs, files in os.walk(self.file_path, topdown=False):

            print(f"total empty folder count is : {len(empty_folders)}")
            if verbose:
                print(f"Scanning: {root}")

            if root in exclude or any(ex in root for ex in exclude):
                if verbose:
                    print(f"Excluded: {root}")
                continue

            # Check if the directory is empty
            if not dirs and not files:
                empty_folders.append(root)
                if len(empty_folders) == 500:
                    break

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
        paginated_df = df.iloc[offset : offset + limit]

        return paginated_df["path"].tolist()

    def __get_all_dirs(self, offset=0, limit=10):
        dirs = []
        for root, subdirs, files in os.walk(self.file_path):
            for subdir in subdirs:
                full_path = os.path.join(root, subdir)
                if os.path.isdir(full_path):  # optional, since subdirs are from os.walk
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

    def remove_dir(self, folder_list, ask_confirm=True):
        """
        Remove directories from the given list.

        Args:
            folder_list (list of str): List of directory paths to remove.
        """

        # Display the folders to be deleted
        self.format_and_print_folders(folder_list)

        # Ask for confirmation
        confirm = (
            input("Are you sure you want to delete the above folders? (Y/N): ")
            if ask_confirm
            else "y"
        )

        if confirm.lower() == "y":
            for folder in folder_list:
                if os.path.exists(folder):
                    try:
                        os.rmdir(folder)  # Try removing as empty
                        print(f"Removed empty dir: {folder}")
                    except OSError:
                        # Directory not empty, remove recursively
                        shutil.rmtree(folder)
                        print(f"Removed recursively: {folder}")
                else:
                    print(f"Folder not found: {folder}")

            print("✅ Done cleaning directories.")
        else:
            print("❌ Operation cancelled by user.")
