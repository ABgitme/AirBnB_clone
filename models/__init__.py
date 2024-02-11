#!/usr/bin/python3
"""
Module responsible for initializing
and loading data using the FileStorage class.
"""
from models.engine.file_storage import FileStorage

storage = FileStorage()
storage.reload()

