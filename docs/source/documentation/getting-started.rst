Getting Started
===============

This section will help you get started with updating our codebase.


Installation
------------
Clone our github repository and navigate to the root directory.

Install all requirements from `requirements.txt` file using

.. code-block::

   python -m pip install -r requirements.txt

This should be all you need to do to install all the requirements



Running the code
----------------

Before you can run our software, you will need to compile all .ui and .qrc files
for python to be able to load them. We wrote a quick script ``precompile.sh`` that will do just that.

.. code-block::

   bash precompile.sh

Once precompiled you can now run the software.

.. code-block::

   python run.py

If you want to reset the database, delete the data folder and run the ``precompile.sh`` script again.
This will copy contents of ``data_clean`` into the ``data`` directory, effectively initialising fresh
db.

Every time you make changes to the ``.ui`` files you have to run ``precompile.sh`` for your changes to take
effect. However, if you look at ``copyclare/config.py``, set the ``DEBUG`` variable as needed when
extensively editing the UI.

.. literalinclude:: /../../copyclare/config.py
   :language: python




Project Structure
-----------------
Here you can see our project file structure.

.. code-block::

   copyclare/
   ├── app.py
   ├── common.py
   ├── __init__.py
   ├── model
   ├── pages
   ├── widgets
   ├── video
   └── ui


- ``app.py`` - contains the main app logic for user interaction. Manages which pages can be shown where.
  currently it is implemented with a **Singleton** pattern such that app's interface is avalable all across
  the codebase.

- ``common.py`` - contains commonly used functionality.

- ``model`` - subpackage that acts as an interface to mediapipe for landmark detection and angle_calculations.
  Also currently contains database, and file handling related code.

- ``pages`` - subpackage that implements every single page. Each page is implemented in a separate file.

- ``widgets`` - subpackage that implements any repetitive ui elements in use.

- ``video`` - implements threads for displaying a video and a camera on the screen.
  Makes use of ``OpenCV`` and ``PySide6``'s threads.

- ``ui`` - Contains ``.ui`` files that define the looks of our user interface.


Data
----

All data that is used by our code **MUST** be stored in the data directory.

.. code-block::

   data/
   ├── accuracy-graphs
   ├── images
   ├── progress-charts
   └── videos
   └── Copyclare.db



- ``Copyclare.db``: sqlite database
- ``videos``: all the exercise videos are stored here
- ``images``: images that are displayed on exercise cards
- ``progress-charts``: all progress charts are saved to separate images for export.
- ``accuracy-graphs``: all accuracy graphs are also saved to separate images for export.


An example of a clean ``data`` directory can be found in a ``data_clean`` directory.
It should not be edited since this comes as a template for initiailing a new DB in case
something goes wrong with the existing one.

To reset the db from scratch run:

.. code-block::

   bash precompile.sh


In order to simplify the process of referencing the data directory we have
a global variable called ``DATA_DIR`` that contains a string representation
of the data path.

to reference it use:

.. code-block:: python

   from copyclare.data import DATA_DIR

   path = DATA_DIR + "/videos"
