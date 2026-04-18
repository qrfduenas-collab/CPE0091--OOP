# -*- coding: utf-8 -*-
"""
Created on Sat Apr 18 10:39:25 2026

@author: user
"""

from FileReaderWriter import FileReaderWriter

class TextFileReaderWriter(FileReaderWriter):
    def read(self, filepath):
        """Reads the entire content of a text file and prints it."""
        try:
            with open(filepath, "r") as read_file:
                data = read_file.read()
                print(data)
                return data
        except FileNotFoundError:
            print(f"Error: The file at {filepath} was not found.")
            return None

    def write(self, filepath, data):
        """Overrides the text file with the provided string data."""
        with open(filepath, "w") as write_file:
            # We ensure the data is cast to a string to avoid errors
            write_file.write(str(data))
            print(f"Write Complete to {filepath}")