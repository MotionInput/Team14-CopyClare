Algorithms
==========

Models
------

Copyclare implements ``Accuracy Model``, that allows to compare user's hand and shoulder motion
with any exercise video.


When developing the algorithm we were working with the following goal in mind:

- Each frame we should get an "Accuracy" score that would represent how close
  the user currently is to the desired motion

With that we came up with a following function signature.


.. code-block::

   func get_accuracy(frame, time): -> accuracy

The function takes in an OpenCV frame object, and a time stamp in seconds of the source video.
The time is important to pass, in order to be able to distinguish between the beginning and the
end of exercise motion.



Data
----

Our model does not require any training to be done for the algorithm to work.
We do require to preprocess the exercise video in advance.






Experiments
-----------


Discussions
-----------




Conclusion
----------




References
----------
