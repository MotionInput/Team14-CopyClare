import os

from .app import App
from .video import VideoThread
from .widgets import *
from .common import *
from .pages import *
from .model import *

__all__ = [
    "App",
    "VideoThread",
    "widgets",
    "common",
    "model",
]


DATA_PATH = os.path.abspath(
    os.path.join(
        os.path.dirname(
            os.path.realpath(__file__)
        ),
        "../data"
    )
)
