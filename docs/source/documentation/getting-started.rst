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

To run our software from command line run:

.. code-block::

   python run.py




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

   data
   ├── assets
   ├── Copyclare.db
   ├── test
   └── videos

- ``assets``: icons and images used by our app
- ``Copyclare.db``: sqlite database
- ``test``: files needed explicitely for testing
- ``videos``: all the exercise videos are stored here

In order to simplify the provess of referencing the data directory we have
a global variable called ``DATA_PATH`` that contains a string representation
of the data path.

to reference it use:

.. code-block:: python

   from copyclare import DATA_PATH

   path = DATA_PATH + "/videos"
