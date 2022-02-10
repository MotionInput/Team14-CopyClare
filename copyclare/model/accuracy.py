import os

import cv2
import numpy as np
import time


class AccuracyModel:
    """
    Computes the accuracy of the camera feed compared
    to a source video.
    """
    def __init__(self, video_path, joints):
        """
        Class constructor

        Parameters:
            video_path: relative path to the video file
            joints: a set of joint strings or id's
        """
        dirname = os.path.dirname(os.path.realpath(__file__))
        self.video_path = dirname + "/sample1.mp4"
        self.joints = {"left_elbow"}
        #self.src_joint_dict = self._init_exercise()
        #self.time_range = self._time_range(self.src_joint_dict)
        #self.user_joint_dict = self._init_user_buffer()
        #self.src_area = self._find_area(self.src_joint_dict)

    def accuracy_session(self):
        """
        This is a generator function that updates every frame.
        """
        accuracy = 0

        # user user's camera
        cap = cv2.VideoCapture(0)

        frame_count = 0

        # for each frame
        while cap.isOpened():

            success, frame = self.cap.read()
            if not success:
                print("Can't read from camera")
                break

            frame_angles = self._process_frame(frame, frame_count)

            # if buffer is about the same as the input video
            # this also controls buffer size
            if self._update_user_buffer(frame_angles):
                accuracy = self._calculate_accuracy()

            self._highlight_landmarks(frame)
            frame_count += 1

            yield frame, accuracy

    def _raw_video(self):
        print(self.video_path)

        cap = cv2.VideoCapture(self.video_path)
        frames = []

        while cap.isOpened():
            success, frame = cap.read()
            print(success)

            if not success:
                print("Can't read from camera")
                break

            frames.append(frame)

        frame_ind = 0
        while True:
            frame_ind += 1
            frame_ind %= len(frames)
            yield frames[frame_ind]

    def _time_range(self, joint_dict):
        """
        Since there can be slight variations between timestamps
        of each joint we take the average
        """
        dif = 0
        for key in joint_dict:
            start = joint_dict[key][0]
            end = joint_dict[key][-1]
            dif += end - start

        dif /= len(joint_dict)

        return dif

    def _highlight_landmarks(self, frame):
        """
        Takes in a frame and does the cutification of the image
        depending on what joints are in self.joints
        """

        return frame

    def _process_frame(self, frame):
        """
        Takes in an image of the frame.

        returns a dictionary where keys are joints and values are tuples of timestamps
        and angles
        {"left_elbow": (1,30.1321), (2,"left_shoulder"): (3,20.12312)}
        """
        time_stamp = time.time()

        pass

    def _calculate_accuracy(self):
        """
        processes src_joint_dict and user_joint_dict

        find area under each of those and returns the difference
        """

        # find area under the src_curve
        area = self._find_area(self.user_joint_dict)

        dif = abs(self.src_area - area)

        return dif

    def _find_area(self, joint_dict):

        area = 0
        ys = []
        times = []

        for key in self.src_joint_dict:

            for each in self.src_joint_dict[key]:
                ts, y = each
                ys.append(y)
                times.append(ts)

            dt = sum(times) / len(times)

            area += np.trapz(ys, dx=dt)

        return area

    def _init_exercise(self):
        """
        Convert source video into a joint_dict

        use self._process_frame(frame) for that
        """
        joint_dict = {}

        cap = cv2.VideoCapture(self.video_path)

        while cap.isOpened():

            success, frame = cap.read()

            if not success:
                print("Can't receive frame (stream end?). Exiting ...")
                break

            frame_angles = self._process_frame(frame)

            for key in self.joints:
                if key not in self.joints:
                    self.joints[key] = []

                joint_dict[key].append(frame_angles[key])

        return joint_dict

    def _init_user_buffer(self):
        """
        Initialises the joint dict just like the src_joint_dict
        """
        joint_dict = {}

        for key in self.joints:
            joint_dict[key] = []

        return joint_dict

    def _update_user_buffer(self, frame_angles, frame_count):
        """
        All user timestamp calculations happen here
        """
        for key in self.joints:
            self.user_joint_dict[key].append(frame_angles[key])

        # make sure we have at least 2 frames loaded in the buffer
        if frame_count > 2:
            # if buffer just became longer than the input video
            if self._time_range(self.user_joint_dict) > self.time_range:

                # pop the first element of all joints
                for key in self.joints:

                    # NOTE: replace with a linked list for efficient
                    # first element removal
                    self.user_joint_dict[key].pop(0)

                return True

        return False
