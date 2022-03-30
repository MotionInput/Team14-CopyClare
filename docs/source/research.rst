:octicon:`mortar-board` Research
================================


:octicon:`book` Understanding Physiotheraphy
--------------------------------------------

Our team has begun research very early in the process. From our conversations with the
with our client and the NeuroPhysiotherapy team, we learned that there are various
types of `physiotherapy <https://mjphysio.ca/types-of-physiotherapy/>`_. For our project we will be working on a tool to aid:

#. Musculoskeletal physiotherapy (client requirement)

#. Neurological physiotheraphy (NeuroPhysiotherapy team requirement)

Although both types of therapy have different exercises, the characteristics of their exercises are
the same. The exercise tend to be slow, repetitive, and rely mostly on body weight.

We have also learned that the feedback physiotherapists give patients is based on:
    #. Trajectory
    #. Accuracy
    #. Coordination
    #. Precision
    #. Time
    #. Speed
    #. Effciency
    #. Effort
    #. Repetition
    #. Jerk
    #. Distance

In addition, physiotherapists also use `Gait analysis <https://www.mgs.physio/what-is-gait-analysis/>`_ to identify weaknesses and demonstrate
progress over time. Althought this is out of the scope of our project, we thought that the
`Wee Gait Glasgow Index <https://www.quest.scot.nhs.uk/hc/en-gb/articles/360000547917-The-Wee-Glasgow-Gait-Index/>`_ and `Edinburgh Visual Gait Score <https://pubmed.ncbi.nlm.nih.gov/12724590/>`_ are
very interesting ways of calcualting Gait scores.

:octicon:`tools` Similar Tools
------------------------------

Upon further research, we've learned that there are two tools similar to CopyClare:
`Kinovea <https://www.kinovea.org/>`_ and `Dartfish <https://www.dartfish.com/healthcare>`_.

Based on the features of Kinovea and Dartfish, we were able to realise how important CopyClare is

Here is how CopyClare compares with them:

.. image:: imgs/competitor-comparison.png
  :alt: Comparision of similar tools


:octicon:`plug` Technology Review
---------------------------------

From our research of the existing tooks, we realised that they were focused on sports analysis.
Additionally, we were able to identify the key features, such as video manipulation, annotation, measurements,
and video capture with camera) are crucial for exercise analysis tool.

After discussing with our clients about our MoSCow, we decided to put our focus on measurement. Therefore,
CopyClare is the first patient-facing tool with automated exercise analysis (like accuracy calcuations) without the active
need for a physiotherapist.

Additionally, one of the requirements was that CopyClare has to run on Windows as an
executable without installation. With resources like PySide6, we would be able to build
a windows executable.We also need dependencies like OpenCV and MediaPipe
to speed up the development of CopyClare. Therefore, we decided to use Python as our
main language.

One of the novel features of CopyClare is our automated analysis (like exercise accuracy calcuations). When we
searched for algorithms that would help us compare angles/time (the metric to measure accuracy), we were not able
to find anything. After multiple experiments we settled on an algorithm. It is more extensively described
in the Algorithms page.

Additional Resources/References:

   * https://www.youtube.com/watch?v=MV_sZNAiVts&t=145s (angle calculations)
   * https://bess.ac.uk/exercises-for-shoulder-pain/
   * `R. Tucker, “The effect of a five-week hippotherapy programme on gait in a child with Angelman's syndrome. A case study using the Wee Glasgow Gait Index (Weeggi),” International Journal of Therapy and Rehabilitation, vol. 26, no. 6, pp. 4–4, 2019. [Accessed: Feb. 7, 2022]`
   * `N. Tennant, L. Wiggins, H. Read, B. Meadows, "The Wee Glasgow Gait Index - A Screening Tool.", APCP Journal, 3(2): 39-48, 2012. [Accessed: Feb. 6, 2022]`
   * `H. Read, M. Hazlewood, S. Hillman, R. Prescott, J. Robb , "Edinburgh visual gait score for use in cerebral palsy.", Journal of pediatric orthopedics, 23(3), 296–301. [Accessed: Feb. 7, 2022]`
