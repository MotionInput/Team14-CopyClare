"""
Contributors: Adi Bozzhanov

"""

"""
Data module

Provides functionality to manage copyclare data. Defines global variables
to access commonly used paths, provides the database, and data objects interfaces.
Has functions to export the data from the database as well.

"""

import os
from appdirs import AppDirs

BASE_DIR = AppDirs("Copy Clare", "UCL MI").user_data_dir

DATA_DIR = os.path.abspath(
    os.path.join(BASE_DIR, "data"))

SQL_DIR = os.path.dirname(os.path.realpath(__file__)) + "/sql/"

DB_DIR = os.path.join(DATA_DIR, "Copyclare.db")

from .database import Database
from .exporter import Exporter
