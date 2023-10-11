#!/usr/bin/python3
"""Update models/__init__.py: to create a unique FileStorage instance for your application"""
from engine.file_storage import FileStorage

storage = FileStorage()
storage.reload()
