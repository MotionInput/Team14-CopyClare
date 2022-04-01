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
The time is important to pass, in order to be able to select a correct angle for comparison.



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


Discussions
-----------

We have identified a number limitations of our comparison approach.

#. Long preprocessing time

   The primary source of long preprocessing time come from Lowess Smothing.
   The values must be smoothed to reduce the noise in the data, yet it does
   add a significant amount to the computation time.

#. In accurate readings for videos where a body part of interest gets covered frequently.

   This bit is primarily a limitation of the mediapipe library and nothing much we can do about it.

#. Limited range of exercise camera angles.

   We do not recommend adding exercises where the joint of interest is not visible in the video.
   For instance, if we are talking about a push up from a side view, our model will not give accurate
   results for both hands (one of the hands is simply not visible). The recommended exercise camera angle
   is either top down or from the front side infront of the face.

#. Not all exercises are even applicable

   Some physiotherapy exercises simply cannot be done while watching at the camera, which
   makes the whole point of real time feedback meaningless. An example of such an exercise
   can be found here: https://www.youtube.com/watch?v=G_c3QztMZNQ .In this specific example
   you are supposed to be  facing a wall, making it impossible for you to look at our screen
   in parallel.





Conclusion
----------

Our solution still remains to be a proof of concept with its own drawbacks and inefficiencies. However
we have proven that real time video comparison without the need of extensive machine learning is possible
and within sight.
