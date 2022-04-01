
Evaluation
==========



Summary of achievements
-----------------------

.. csv-table:: Achievement table
   :header: "ID", "Requirements", "Priority", "State", "Contributors"
   :widths: 30, 600, 100, 30, 100

   "1", "Enable users to view and replicate physiotherapy rehabilitation exercises (Design + Implementation)", "Must", "Y", "All"
   "2", "Give user feedback on how accurately users are doing the exercise to the video during the exercise regime set by the physiotherapist", "Must", "Y", "Adi"
   "3", "Accuracy metric of 2D translation", "Must", "Y", "Adi, Tianhao"
   "4", "Reports for progress over time (based on physiotherapy students)", "Should", "Y", "Yan, Sree"
   "5", "Desktop Application (Compilation)", "Should", "Y", "Adi"
   "6", "Video addition feature equipped with video trimmer", "Should", "Y", "Tianhao"
   "7", "Accuracy metric of 3D translation", "Could", "Y", "Adi, Tianhao"
   "8", "Login / Register", "Could", "X", "N/A"
   "9", "Users to be able to receive and understand feedback from clinicians about which videos to use for therapy through the app", "Could", "X", "N/A"

.. csv-table:: Overall Achievement table
   :header: "Key Functionalities (must have & should have)", "Optional Functionalities (could have)"
   :widths: 500, 500

   "**100%** completed", "**33%** completed"



.. csv-table:: Known bugs list
   :header: "ID", "Bug description", "Priority"
   :widths: 30, 600, 100

   "1", "App crashes if camera is already on when opening an Exercise page", "Must"
   "2", "If video addition page has been used, and is opened again during the same session, the page does not return to initial state. However, the functions still work.", "Could"



.. csv-table:: Individual contribution distribution
   :header: "Work packages", "Adi", "Yan", "Tianhao", "Sree"
   :widths: 600, 50, 50, 50, 50

   "Client liaison", "40%", "10%", "10%", "40%"
   "Requirement analysis", "25%", "25%", "25%", "25%"
   "Research", "32%", "5%", "31%", "32%"
   "UI Design", "20%", "30%", "20%", "30%"
   "Programming", "40%", "30%", "15%", "15%"
   "Testing", "20%", "20%", "40%", "20%"
   "Development blog", "10%", "60%", "10%", "20%"
   "Website editing", "28%", "20%", "25%", "27%"
   "Video editing", "45%", "45%", "5%", "5%"
   "**Overall contribution**", "**28%**", "**27%**", "**21%**", "**24%**"
   "**Roles** (All are Report Editors)", "**Software architect, Client liaison, Full-stack, Researcher, Programmer**", "**UX/UI, Front-end, Blog editor, Programmer**", "**Full-stack, Researcher, Tester**", "**Back-end, UX/UI, Client liaison, Researcher**"



Evaluation of project
---------------------

In order to evaluate our project, we have decided to rate the following aspects on a scale of 0-5, where 0 represents 'not achieved' and 5 represents 'perfectly accomplished'.

.. csv-table:: Evaluation table
   :header: "Aspect", "Rating", "Evaluation"
   :widths: 200, 30, 600

   "UX / UI", "5", "Our UI requires very few clicks for users to perform actions such as starting an exercise session or viewing progress. Furthermore, we have a tutorial which pops up upon starting the app, so users can quickly learn all the features. Besides that, we also added several features that were not specifically requested by our clients to enhance UX; one example is the option to pin/unpin exercises of choice to the top of the home page. Therefore, we rate 5 for the UX/UI aspect, and this is further backed by our second round of User Acceptance Testing, where we received good feedback from potential users."
   "Functionality", "4", "We rate 4 for the functionality aspect as we achieved all key requirements as requested by our clients. The implemented features are fully functional and performs their tasks as expected. However, not many optional functionalities are achieved."
   "Stability", "2", "Our accuracy model can be a little unstable. There are limitations in the duration of a repetition and the speed of execution - certain values (e.g. movements being too short or too fast) can cause issues, affecting its ability to perform well."
   "Efficiency", "3", "Our main functionality - allowing users to follow sample exercise videos and receive live feedback - requires video preprocessing. Currently with our algorithm, the video preprocessing does not work for videos longer than 15 seconds. In order to mitigate this issue, our video trimmer allows users to first trim their videos before uploading them to be processed."
   "Compatibility", "5", "Our app compiles to an exe (native desktop Windows application), and therefore runs on all Windows devices. The code itself does run on all operating systems, hence compatibility is 5."
   "Maintainability", "5", "Our code is fully documented using doc strings, therefore it is easy to read and understand. We have also used meaningful encapsulation, and patterns such as singleton and threat worker separation to ensure that our code is maintainable not only to our current team, but for future developers as well."
   "Project management", "4", "Our team had regular progress meetings, where we would allocate tasks. We also managed our project using Trello and a Gantt chart, in order to keep track of tasks to complete as well as deadlines."



Future work
-----------

We have laid a solid foundation for future work on CopyClare. Our research and code documentation will and should set future teams on the right path to begin.

We believe that future work on this project should be on:

- Calculating accuracy - a more robust way of comparing two videos is needed for advanced exercises
- Create a way for the data to be shared online, so physiotherapists can monitor their patient's progress
- Perform more usability testing with the app to get feedback to improve the UX/UI
- Experimentation with various types of cameras to see its effect on accuracy









