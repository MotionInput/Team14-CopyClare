Algorithms
==========

Models
------

Copyclare implements ``Accuracy Model``, that allows to compare user's hand and shoulder motion
with any exercise video.


When developing the algorithm we were working with the following goal in mind:

.. admonition:: Goal

   Each frame we should get an "Accuracy" score that would represent how close the user currently is to the desired motion

With that we came up with a following function signature.


.. code-block::

   func get_accuracy(frame, time): -> accuracy

The function takes in an OpenCV frame object, and a time stamp in seconds of the source video.
The time is important to pass, in order to be able to distinguish between the beginning and the
end of exercise motion.



Data
----

Our model does not require any training to be done for the algorithm to work.
We do require to preprocess the exercise videos in advance. We iterate over every
single frame in the source video, and we use mediapipe to find 3D coordinates of joints.
We then calculate angles between joints of interest and store everything in a JSON format.
The JSON stores information about every joint and maps joint angles to timestamps in seconds.

Sample JSON:

.. code-block:: json

   {
	"left_elbow": {
		"0.0": 74.07107630335211,
		"0.04": 77.29212142432641,
		"0.08": 74.27721704527343,
		"0.12": 74.56098643827173,
		"0.16": 71.83270077427127
	},
	"left_shoulder": {
		"0.0": 50.0279337914335,
		"0.04": 46.463919668135865,
		"0.08": 47.896393906082416,
		"0.12": 49.82595639998958,
		"0.16": 49.06242257021765
	},
	"right_elbow": {
		"0.0": 114.61462231825777,
		"0.04": 113.73658720932791,
		"0.08": 113.41941301622808,
		"0.12": 111.46260391447437,
		"0.16": 109.5732235702205
	},
	"right_shoulder": {
		"0.0": 148.26033791855784,
		"0.04": 151.96533062061914,
		"0.08": 150.96903644421906,
		"0.12": 149.37786162510116,
		"0.16": 148.55592024363725
	}
    }



Experiments
-----------


Discussions
-----------


Conclusion
----------



References
----------
