"""
Contributors: Adi Bozzhanov

"""

"""
copyclare.data.objects

contains class definitions of interfaces for data that can be accessed from
our db

You can import modules like so:

.. code-clock: python

   from copyclare.data.objects import Attempt
"""

from .attempt import Attempt
from .exercises import Exercise
from .tag import Tag

__all__ = [
    "Database",
    "Exercise",
    "Tag",
    "Attempt",
]
