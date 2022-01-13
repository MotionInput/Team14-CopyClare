# Documentation

This section contains all you need to know about
our documentation.


We are using **sphinx** to generate our documentation.

To get started install all documentation requirements in docs directory.

	pip install -r requirements.txt
	
Now make changes to ``.rst`` and ``.md`` files to update our docs.

Commit your changes to the `dev` branch and the docs website should get automatically
updated.

If you are working on your own branch and want to see how the docs would look like,
navigate to ``docs`` directory and run

	make clean; make html
	
This will create a build folder where you can find and open html files that will be generated.



