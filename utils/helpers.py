from pandas.io.parquet import json
import pandas as pd


class Helper:
    """General helper utilities for file and system operations."""
    """Utility class to convert byte sizes into human-readable formats."""
    UNITS = ['B', 'KB', 'MB', 'GB', 'TB', 'PB']

    @staticmethod
    def bytes_to_readable(size_in_bytes: int, precision: int = 2) -> str:
        """Convert bytes to a formatted string (e.g., 1.23 MB)."""
        size = float(size_in_bytes)
        index = 0

        while size >= 1024 and index < len(Helper.UNITS) - 1:
            size /= 1024
            index += 1

        return f"{size:.{precision}f} {Helper.UNITS[index]}"

    @staticmethod
    def format(data):
        return json.dumps(data, default=str, indent=4)

    @staticmethod
    def size_to_bytes(size_str):
        if pd.isna(size_str):
            return 0
        number, unit = size_str.split()
        number = float(number)
        unit = unit.upper()
        multiplier = {"B": 1, "KB": 1024, "MB": 1024**2, "GB": 1024**3}
        return int(number * multiplier[unit])

    @staticmethod
    def sort_by_column(data, column_name: str, ascending=True):
        df = pd.DataFrame(data)
        if column_name == "size":
            df["size_bytes"] = df["size"].apply(Helper.size_to_bytes)
            df = df.sort_values(by="size_bytes", ascending=ascending)
            df.drop("size_bytes", axis=1, inplace=True)
        else:
            df = df.sort_values(by=column_name, ascending=ascending)

        return df.to_dict(orient="records")
