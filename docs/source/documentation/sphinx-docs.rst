Sphinx Documentation
====================

We are using sphinx to produce our project website. Sphinx converts ``.rst`` files into static html and css files with an applied theme. This section will explain how to build our website.


Docs Overview
-------------

The contents of our docs directory are as following.

.. code-block::

   docs
   ├── build
   ├── make.bat
   ├── Makefile
   ├── requirements.txt
   └── source

The most important bits here are ``build`` and ``source`` directories.

- ``source``: contains ``.rst`` files which are used to create static html for our website.
- ``build``: contains the generated ``.html`` files.


Installing requirements
-----------------------

First of all you will need to install documentation specific requirements. From ``/docs`` directory run:


.. code-block::

   pip install -r requirements.txt





Building documentation
----------------------

In order generate docs in the ``build`` directory, run the following command from the ``/docs`` directory.

.. code-block::

   make clean ; make html

This will go over every ``.rst`` file in the source folder and translate it into html, according
to the configuration defined int ``source/conf.py``. Resultant files can be found in ``build/html``.
