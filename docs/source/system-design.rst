System Design
=============

Our system includes a single standalone application that encapsulates the entire
physiotherapy flow within itself.



:octicon:`workflow` Architecture
--------------------------------

.. image:: imgs/architecture-diagram.png


The following figure represent our application archiecture. Here you will find a brief description
of each module shown.

.. blogfield:: Model

   Our ``Model`` module provides functionality to process video files, calculating angles between joints
   and conducting comparison calculations between 2 video streams that results in an accuracy score.

   Submodules:

   #. ``Pose Module`` - our preprocessing enging that wraps up mediapipe to
      find landmarks and identify angles between joints of interest.
   #. ``Accuracy Model`` - Contains main video processing and comparison logic.

.. blogfield:: Video Module

   Our ``Video Module`` is responsible for displaying video streams
   in our application.

   Submodules:

   #. ``Camera Thread`` - Runs OpenCV session to update user interface with
      camera feed, Queries the ``Model`` to display landmarks and update the accuracy
      graph.

   #. ``Video Thread`` - Updates user interface with the exercise video stream.

   #. ``Thread Manager`` - Makes sure that all threads are started and finished safely.

.. blogfield:: UI

   Our ``UI`` module contains code defining styling and positioning of UI elements.
   This code is automatically generated using QtDesigner app that allows creating user
   interface through drag and grop and then compiling it into python's source code.

   This module **DOES NOT** contain any application logic.

.. blogfield:: Pages Module

   The ``Pages`` modules contains application logic of Pages.

.. blogfield:: Widgets Module

   The ``Widgets`` modules contains application logic of arbitrary UI elements,
   that we create dynamically



.. blogfield:: UiElement

   The ``UiElement`` is an interface for all of our UI elements.
   The biggest advantage we gain from it is, when debugging
   we can avoid running precompilation script, and rather load
   ui directly from qml files. Very useful for when we need to quickly
   test the UI changes.


.. blogfield:: App

   The ``App`` modules cotntains main application logic. It is responsible changing pages,
   and accessing the Database.

.. blogfield:: Data Module

   The ``Data`` module contains a SQLITE database interface and tools,
   for managing the data from the DB.





:octicon:`database` Database
----------------------------

.. image:: imgs/er-diagram.png

there are 3 main tables(exercises,attempts,tags).
   * Exercises table is used to take down all sorts of exercises.
   * An attempts informatation would be recorded into database when patients finish their exercise.
   * Tags are used to classify the exercise. And the tag_to_exercise table is generated because of the many to many relation between tags and exercises table.
