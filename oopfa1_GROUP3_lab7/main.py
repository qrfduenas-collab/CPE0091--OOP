# -*- coding: utf-8 -*-
"""
Created on Sat Apr 18 10:48:40 2026

@author: user
"""
from FileReaderWriter import FileReaderWriter
from CSVFileReaderWriter import CSVFileReaderWriter
from JSONFileReaderWriter import JSONFileReaderWriter
from TextFileReaderWriter import TextFileReaderWriter # New Import

# 1. Test the default base class
print("Testing Default Class:")
df = FileReaderWriter()
df.read()
df.write()
print()

# 2. Test the CSV class
print("Testing CSVFileReaderWriter:")
c = CSVFileReaderWriter()
# Note: Ensure sample.csv exists in your folder or change to a file you have
# c.read("sample.csv") 
c.write(filepath="sample2.csv", data=["Hello", "World"])
print()

# 3. Test the JSON class
print("Testing JSONFileReaderWriter:")
j = JSONFileReaderWriter()
# j.read("sample.json")
j.write(data=['foo', {'bar': ('baz', None, 1.0, 2)}], filepath="sample2.json")
print()

# 4. Test your new Text File class
print("Testing TextFileReaderWriter:")
t = TextFileReaderWriter()
t.write(filepath="lab_note.txt", data="This is a test for the OOP Lab Activity.")
t.read("lab_note.txt")