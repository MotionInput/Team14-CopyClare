Blog
====



.. blogfield:: 21-11-2021

   A weekly client meeting schedule with Professor Joseph Connor was established (Thursdays). During this week’s client meeting, we discussed the main requirements for CopyClare with Joseph. We understand that CopyClare is a web application that allows people to follow rehabilitation videos (mainly for shoulders and elbows), and users can track the accuracy of their movements over time.

   During previous weeks, we prioritised working on the Human Computer Interaction (HCI) section of the module, and submitted the final report before the deadline (10 Nov 2021). The end product of this HCI section was a brief prototype, which demonstrates the basic functionalities that the final CopyClare app should have.

   Apart from this, our team also worked on MotionInput:
   Sree was testing to see if it is feasible to create React Native apps using MotionInput. Since there are different teams working on different builds of MotionInput (Android, MacOS, etc.), it makes sense to collaborate on a ReactNative version instead.
   Adi was part of the architecture team, working on general design of an updated MotionInput.
   Yan was part of Exercises Module GUI Redesign team.

.. blogfield:: 05-12-2021

   We reviewed the requirements with Joseph and Professor Dean Mohamedally. Due to privacy issues, we are not allowed to send patients’ exercise videos to a server. This means that we need to analyse their videos locally on the patients’ machines. Hence, CopyClare will be a native Windows desktop application.

   For work on MotionInput:
   Sree concluded that it is not feasible to implement MotionInput on React Native. This is because of 2 main reasons: MotionInput is very messy and refactoring the whole code base is needed before further experimentation; MotionInput may be too heavy for React Native (not tested), because MotionInput relies on OpenCV and the frame rate may drop, the accuracy may not be good enough for any real application.
   Adi continued working on the new MotionInput architecture.
   Yan came up with a design idea for the new MotionInput Exercises Module GUI, which was shown during the brainstorming meetings with the rest of the GUI Redesign team. The team then came up with a whole new design, by incorporating ideas from each member of the team.

   Due to MotionInput not compiling properly for several members of the team, this has greatly disrupted our progress with CopyClare. However, we have started to look into the different ways we can implement the core functionalities of CopyClare.


.. blogfield:: 19-12-2021

   We finalised our requirements with Joseph, and documented them using the MosCoW method.

   Joseph also gave us further, more concrete guidelines on how we can analyse whether a patient is doing their exercises correctly. This could be done by noting the coordinates of the ‘starting’ and ‘ending’ positions of a patient’s body part (e.g. wrist).

   We will be researching on how we can use OpenCV and MediaPipe for video analysis. More specifically, to calculate the required angles.

   For work on MotionInput:
   Adi started working on the compilation for MotionInput.
   Due to issues with working on the new MotionInput Exercises Module GUI using a Macbook, Yan was unable to work on the actual implementation of the GUI.



.. blogfield:: 02-01-2021

   This was during our winter break. During this time, we did our own research to devise an algorithm for calculating accuracy. We also did some research on the frameworks or applications we can use to implement our user interface.

   Our biggest achievement was the completion of the code to calculate angles on the video from a patient’s camera. The angle is clearly displayed on the patient’s live camera video, and analysis lines are drawn to give the patient a clear idea of which angles we are measuring, as well as which landmarks (e.g. wrist and shoulder) we are tracking. A short demo of this is now available. The next step will be to calculate angles in 3-dimension, so that angles can still be accurately calculated regardless of where the patient is standing and how they are facing the camera.


.. blogfield:: 16-01-2022

   A lot of our work is centred around the preparation for the elevator pitch (which will be taking place on 21 Jan 2022). As a team, we collaboratively wrote the presentation script, and elected Sree to be the one presenting it.

   We also came up with a system architecture diagram, which clearly shows the modules CopyClare needs. We also identified which modules require the use of external libraries, and decided upon which ones to use.

   For the UI, we have decided to use the Pyside library, which allows us to easily create widgets and frames for CopyClare using the QtDesigner application. Hence, we will be experimenting on how we can fully utilise this drag-and-drop application to create our UI.

   Our next steps also include continuing the work on the implementation of angle calculations in 3D, and devising an algorithm for accuracy calculation.


.. blogfield:: 30-01-2022

   We started working with some Masters students, who wanted an application that could help with their patients’ recovery process. We had 2 meetings with them by this time, and we have established a weekly meeting schedule (Mondays). We were given more advice and suggestions for measuring how well a patient is doing in terms of movement accuracy. More specifically, we were told that accuracy is mostly measured by the quantity and quality of movements, where quality can be defined by different criteria such as smoothness or effortlessness. They have also mentioned that a heatmap would be desirable for analysis. The Masters’ students also gave insights on how the app should make the rehabilitation process more entertaining, as it can be quite repetitive and tough. By the 2nd meeting, we made a simple UI to show them the design we came up with, and received some feedback, which we will be using to improve on our design.

   The implementation of angle calculations in 3D has also been completed at this time. Therefore, the next steps for back-end will be to define a database structure, which is required to store both the patients’ progress and sample exercise videos from physiotherapists.

   For work on MotionInput:

   Adi is still working on the compilation.

.. blogfield:: 13-02-2022

   We came up with a 2nd UI design (which had quite significant changes from our initial prototypes), and Adi created a working demo to show how it works. We presented this to the Masters’ students, and received more feedback on how we can further improve it. We were also given a few examples of existing applications with similar functionalities to CopyClare.

   We also came up with a new algorithm that compares graphs to calculate the accuracy. Therefore, our next steps are to implement and test whether this algorithm works.

   The database structure is also mostly confirmed, and so we will begin to write the Python code required in order to access the database.

   For work on MotionInput:

   Adi’s compilation work is complete.
   Tianhao and Yan were assigned to work on the Joystick Module in the new architecture.


.. blogfield:: 27-02-2022

   We came up with a final UI, and Yan created a simple mock-up, which we have yet to show Joseph and the Masters’ students. With this finalised UI, we are now able to focus on building the UI.

   The graph algorithm that we were testing is almost working, although there are certain limitations to using this algorithm, with one of the biggest limitations being the sample exercise videos uploaded by physiotherapists need to be exactly 1 repetition long. After speaking to Joseph on this, we agreed that CopyClare will need to include a simple video editor that allows physiotherapists to trim the video directly within the app before uploading them for analysis.

   We have also discovered more features of Sphinx, a Python documentation generator, and so we decided to use Sphinx to build our project website (i.e. this website).

   For work on MotionInput:

   Tianhao and Yan’s work on the (wrist) Joystick Module is almost complete. However, it has yet to be tested.
