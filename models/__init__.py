#!/usr/bin/python3

""" Module to make an instance of filestorage. """

from models.engine.file_storage import FileStorage


storage = FileStorage()
storage.reload()
