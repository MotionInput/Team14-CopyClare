:octicon:`code` Implementation
==============================



:octicon:`project` Project Structure
------------------------------------
Here you can see our project file structure.

.. code-block::

   copyclare/
   ├── app.py
   ├── common.py
   ├── __init__.py
   ├── model
   ├── data
   ├── pages
   ├── widgets
   ├── video
   └── ui


- ``app.py`` - contains the main app logic for user interaction. Manages which pages can be shown where.
  currently it is implemented with a **Singleton** pattern such that app's interface is avalable all across
  the codebase.

- ``common.py`` - contains commonly used functionality.

- ``model`` - subpackage that acts as an interface to mediapipe for landmark detection and angle_calculations.


- ``data`` - contains database, and file handling related code.

- ``pages`` - subpackage that implements every single page. Each page is implemented in a separate file.

- ``widgets`` - subpackage that implements any repetitive ui elements in use.

- ``video`` - implements threads for displaying a video and a camera on the screen.
  Makes use of ``OpenCV`` and ``PySide6``'s threads.

- ``ui`` - Contains ``.ui`` files that define the looks of our user interface.

:octicon:`file` Data
--------------------
All data that is used by our code **MUST** be stored in the data directory.

.. code-block::

   data
   ├─accuracy-graphs
   ├─images
   ├─progress-charts
   ├─results
   ├─test
   └─videos

- ``Copyclare.db``: sqlite database
- ``accuracy-graph``: collect all accuracy graphs of attempts
- ``progress-charts``: all outputted long term progress chart of some exercises
- ``results``: all outputted reports
- ``test``: files needed explicitely for testing
- ``videos``: all the exercise videos and the images of the video are stored here

In order to simplify the provess of referencing the data directory we have
a global variable called ``DATA_DIR`` that contains a string representation
of the data path.

:octicon:`device-camera-video` Embed OpenCV stream into UI
----------------------------------------------------------

One of the challenges we needed to tackle for our implementation is to integrate the OpenCV camera stream
within the native application. We have solved this problem by applying a sequence of format conversion to
achieve full compatibility and efficiency. You can see the minimal code snippet that fully shows the
process of conversion.
-The conversion can be summarised into 3 steps:

    * First of all we need to convert a standard open cv frame from the BGR format into RGB.
    * The next step is to use the resultant RGB frame to create a QImage instance. Which is already enough to display it on the screen.
    * however if we want to also allow frequent and smooth updates to the ui, it is best to convert QImage into QPixmap, which will also make it incredibly simple to display the frame by using QLabels’s set pixmap method. It is important to note that the whole process must be running in a separate thread to prevent other ui elements from freezing.



:octicon:`file-binary` Compilation
----------------------------------

Using python as the main language for the application development poses a set of difficulties
when trying to create a distributable version of it. Even though Python is an interpreted
language, we have managed to create a set of executable versions of our application for different platforms.
This section will describe our compilation procedure, its advantages and limitations.

When it comes to compiling python to an executable, the standard approach is to package the python
interpreter along side with the source code and compress all of it to an executable. The mentioned
process is called "freezing", which results in a pretty reliable package yet comes with some drawbacks:

#. No code optimisation during compilation stage.

#. Long startup times due to code decompression (especially significant for large codebases).

#. Poor app efficiency over all.

There exists an alternative approach to "freezing" python code, which is to translate python to a compiled language
like C, and then compile the resultant C code. One of the tools that allows to do that is `Nuitka <https://nuitka.net/index.html>`_. There are a couple of advantages that we get from using it.

#. The resultant executable is faster than running the code with a python interpreter.

#. The code is optimised during compilation time.

#. Solves the issue of long start up times, since there is nothing to decompress.


The only issue here is the compilation time. It takes around 20 minutes to compile our codebase to an executable.
This is an unfavourable constraint, however it is more than a reasonable tradoff for the advantages we gain from it.

In order to compile our code base you first need to install nuitka.

.. code-block::

   python -m pip install nuitka


Once installed nuitka and all project dependencies just simply run.

.. code-block::

   deploy.sh
