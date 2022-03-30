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

.. blogfield:: Widgets Module

.. blogfield:: UiElement


.. blogfield:: App

.. blogfield:: Data Module





:octicon:`database` Database
----------------------------
