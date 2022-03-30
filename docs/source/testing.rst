Testing
=======



User acceptance testing (UAT)
-----------------------------


- **Why we did this test**

This test is mainly used to test our UI. This is because 'usability' is our main priority. Therefore, we need feedback from users (and potential users) themselves to know how the app works for them. The most straightforward way to achieve this is through UAT.



- **Test tools used**

The only tool needed to run the tests was our app. We also prepared some tasks (test scenarios) for users to work through during the test.

.. csv-table:: Test scenarios
   :header: "ID", "Task description"
   :widths: 30, 600

   "1", "Start an exercise"
   "2", "Maintain a good accuracy score (white line) for 3 seconds"
   "3", "End an exercise"
   "4", "View list of attempts"
   "5", "Export a single attempt"
   "6", "Export all attempts"



- **How we conducted the test**

We started running the app for our users and gave them the test scenarios to go through. We encouraged them to 'think out loud', so that we are able to know their thought process as they navigate through the app. 

A member of our team would ask the user questions as they go through the tasks to prompt them to think further, or give guidance while needed. Another member of the team would observe the test run, recording the interactions and noting any interesting findings.



- **Results we got**

.. csv-table:: Complaints / Issues
   :header: "ID", "Description"
   :widths: 30, 600

   "1", "No quick overview of all attempts"
   "2", "UI not intuitive enough"
   "3", "No landing page to properly launch app"
   "4", "Colour scheme is not 'professional'"
   "5", "User's camera is too small during exercise sessions"

.. csv-table:: Good features
   :header: "ID", "Description"
   :widths: 30, 600

   "1", "Sample video present during exercise"
   "2", "Accuracy live graph & colour coding feature helps with motivation"
   "3", "'My Exercises' tag feature to allowing pinning"
   "4", "Analysis page is detailed & easy to understand"



- **Analysis and conclusion to the results**

We made the following changes to address the complaints:

.. csv-table:: Solutions to address complaints
   :header: "ID", "Complaint Description", "Solution"
   :widths: 30, 600, 600

   "1", "No quick overview of all attempts", "Progress chart"
   "2", "UI not intuitive enough", "Pop-up tutorial"
   "3", "No landing page to properly launch app", "Created landing page"
   "4", "Colour scheme is not 'professional'", "Changed colour theme to muted blue"
   "5", "User's camera is too small during exercise sessions", "Changed layout of Exercise page to maximise user's camera"

We did a second round of UAT after making these changes to our UI, and there were much fewer issues detected. Users were generally able to work through the test scenarios with ease. Therefore, we are confident that the 'usability' aspect has been achieved.















