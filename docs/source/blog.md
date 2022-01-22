# November 2021

## Sun 21 Nov 2021

- Accomplished
    1. Discussed the requirements with Joseph
        - CopyClare is an online platform that allows people to follow rehabilitation videos for shoulders and elbows.
        - The users can track their accuracy of the movements over time
        - Users’ videos are uploaded to a secure server where the analysis will take place.
    2. Submitted HCI materials by deadline (Nov 10th)
        - Generated personas based on project requirements
        - Draft Sketches for HCI, and got them reviewed by Joseph (to see if those were what he envisioned)
        - Create a prototype
        - Testing complete: Usability testing (with other students) and Heuristic evaluation
        - Based on initial requirements, we our end product was a very brief prototype, which demonstrates the basic functionalities that the final CopyClare app should have
    3. Independent Projects
        - Based on the work required for MotionInput, our team had to lend a hand to improve MotionInput
            - Sree - Testing to see if it is feasible to create React Native apps using MotionInput. Since there are different teams working on different builds of MotionInput (Android, MacOS,..), it makes sense to collaborate on a ReactNative version instead.
            - Adi - Part of the architect team, working on general design of an updated MotionInput.
            - Yan - Part of Exercises Module GUI Redesign team
- Goals for Next Week
    1. Independent Projects
        - Sree - Identify the feasibility of a React Native implementation of MotionInput
        - Adi - Plan out the architecture of the app.
- Blockers
    1. None


# December 2021

## Sun 5 Dec 2021

- Accomplished
    1. Reviewed the requirements with Joseph and Dean
        - Dean had mentioned that we are not allowed to send users’ exercise videos to a service. We need to analyze the videos locally on the users’ machines
    2. Independent Projects
        - Sree - It is not feasible to implement MotionInput on React Native. This is because of 2 main reasons:
            1. MotionInput is very messy. Refactoring the whole code base is needed before further experimentation.
            2. MotionInput may be too heavy for React Native (Not tested). Because MotionInput relies on OpenCV and the frame rate may drop, the accuracy may not be good enough for any real application.
- Goals for Next Week
    1. Get started with implementation of the project
    2. Finalise requirements with Joseph
- Blockers
    1. MotionInput is not compiling properly. There are many errors for several members of the team.

## Sun 12 Dec 2021

- Accomplished
    1. Finalised requirements with Joseph
        - Must Have:
            - CopyClare needs to enable users to view and replicate physiotherapy rehabilitation exercises
            - We must give user feedback on compliance to the video during the exercise regime
            - Compliance = how accurately users are doing the exercise
            - Accuracy = Angles/Time
        - Should Have:
            - Reports for progress over time
            - Desktop Application
        - Could Have:
            - Login/Register
            - Users to be able to understand and receive feedback from clinicians about which videos use for therapy
            - Web application
        - Nice to Have:
            - Accessibility through eye-tracking and Ask-KITA
    2. Compilation was more difficult than expected. Since those are being fixed, no actual progress was made on building CopyClare
- Goals for Next Week
    1. Research about using OpenCV and MediaPipe for video analysis
    2. Utilise OpenCV to create a POC of the CopyClare project
- Blockers
    1. MotionInput is still not ready to use for development

## Sun 19 Dec 2021

- Accomplished
    1. Due to end of term deadlines, no progress was made
- Goals for Next Week
- Blockers


# January 2022

## Sun 2 Jan 2022

- Accomplished
- Goals for Next Week
- Blockers

## Sun 16 Jan 2022

- Accomplished
- Goals for Next Week
- Blockers

## Nov-Jan Progress Video (Sat 22 Jan 2022)

Video link: link to youtube video here

## Sun 30 Jan 2022

- Accomplished
- Goals for Next Week
- Blockers
