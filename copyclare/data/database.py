import json
import os
import pathlib
from distutils.dir_util import copy_tree
from copyclare.data import DATA_DIR
from copyclare.model.accuracy_v2 import AccuracyModel

from sqlalchemy import (
    create_engine,
    Column,
    ForeignKey,
    Integer,
    String,
    Float,
    DateTime,
    Table,
)
from sqlalchemy.orm import declarative_base, relationship, sessionmaker, scoped_session

JOINTS_MAP = {
    "left_elbow": (13, 15, 11),
    "right_elbow": (14, 12, 16),
    "left_shoulder": (11, 13, 12),
    "right_shoulder": (12, 11, 14),
    "right_hip": (24, 12, 26),
    "right_knee": (26, 24, 28),
    "left_hip": (23, 11, 25),
    "left_knee": (25, 23, 27),
}

Base = declarative_base()


class Database:
    class Decorators:
        @classmethod
        def session(cls, func):
            def create_and_remove_session(obj, *args, session=None, **kwargs):
                if session is None:
                    session = obj.session
                return func(obj, *args, session=session, **kwargs)
            return create_and_remove_session

    def __init__(self, db_file):
        """create a database connection to the SQLite database
            specified by db_file
        :param db_file: database file
        :return: Connection object or None
        """

        if not os.path.exists(os.path.join(DATA_DIR, "videos")) or not os.path.exists(
            os.path.join(DATA_DIR, "images")
        ):
            print("Initialising usesr data directory")
            os.makedirs(DATA_DIR, exist_ok=True)
            local_data = pathlib.Path(__file__).parent.parent.parent.joinpath("data")
            copy_tree(local_data, DATA_DIR)

        if not os.path.exists(os.path.join(DATA_DIR, "progress-charts")):
            os.makedirs(os.path.join(DATA_DIR, "progress-charts"))

        if not os.path.exists(os.path.join(DATA_DIR, "accuracy-graphs")):
            os.makedirs(os.path.join(DATA_DIR, "accuracy-graphs"))

        exists = os.path.exists(db_file)
        self.engine = create_engine(
            f"sqlite+pysqlite:///{db_file}", echo=True, future=True
        )
        self.Session = scoped_session(sessionmaker(bind=self.engine))
        self.session = self.Session()
        if not exists:
            Base.metadata.create_all(self.engine)
            self._init_joints()
            self._init_debug_data()
    
    @Decorators.session
    def _init_joints(self, session=None):
        for joint_name, (center, adj1, adj2) in JOINTS_MAP.items():
            joint = Joint(name=joint_name, center=center, adj1=adj1, adj2=adj2)
            session.add(joint)
        session.commit()

    @Decorators.session
    def _init_debug_data(self, session=None):
        tag = Tag(name="My Exercises")
        with open(DATA_DIR + "/videos/clare2.txt", "r", encoding="UTF-8") as f:
            clare2_desc = f.read()

        exercise = Exercise(
            name="Shoulder Rotation",
            video_directory="/videos/clare2.mp4",
            image_directory="/images/1.png",
            description=clare2_desc,
        )

        exercise.tags.append(tag)
        joints = session.query(Joint).all()
        accuracymodel = AccuracyModel(exercise, joints)
        angles = accuracymodel.get_angles(DATA_DIR + exercise.video_directory)
        for joint in joints:
            for t, angle in angles[joint.name].items():
                exercise.data.append(ExerciseData(exercise=exercise, joint=joint, time=t, angle=angle))
        session.add(tag)
        session.add(exercise)
        session.commit()

    @Decorators.session
    def add_tag(self, tag, session=None):
        session.add(tag)
        session.commit()

    @Decorators.session
    def remove_tag_from_exercise(self, tag, exercise, session=None):
        exercise.tags.remove(tag)
        session.commit()

    @Decorators.session
    def add_tag_to_exercise(self, tag, exercise, session=None):
        exercise.tags.append(tag)
        session.commit()

    def get_exercise_tags(self, exercise):
        return exercise.tags

    @Decorators.session
    def get_all_tags(self, session=None):
        return session.query(Tag).all()

    @Decorators.session
    def get_all_exercises(self, session=None):
        return session.query(Exercise).all()
    
    def get_exercises_by_tag(self, tag):
        return tag.exercises

    @Decorators.session
    def get_one_exercise_by_ID(self, id, session=None):
        return session.query(Exercise).filter(Exercise.id == id).first()

    @Decorators.session
    def add_attempt(self, attempt, session=None):
        session.add(attempt)
        session.commit()

    @Decorators.session
    def get_one_attempt_by_ID(self, id, session=None):
        return session.query(Attempt).filter(Attempt.id == id).first()

    def get_attempt_in_exercise(self):
        raise NotImplementedError

    @Decorators.session
    def get_exercise_ame_ang_dec_by_ID(self, id, session=None):
        exercise = self.get_one_exercise_by_ID(id, session)
        return exercise.name, exercise.description

    def delete(self, table_name, key_name, key):
        raise NotImplementedError

    @Decorators.session
    def get_all_attempts(self, session=None):
        return session.query(Attempt).all()

    @Decorators.session
    def add_exercise(self, exercise, session=None):
        session.add(exercise)
        session.commit()

    @Decorators.session
    def get_all_joints(self, session=None):
        return session.query(Joint).all()

    @Decorators.session
    def get_exercise_name_and_desc_by_ID(self, exercise_id, session=None):
        exercise = session.query(Exercise).filter(Exercise.id == exercise_id).first()
        return exercise.name, exercise.description

    @Decorators.session
    def get_tag_by_name(self, tag_name, session=None):
        return session.query(Tag).filter(Tag.name == tag_name).first()

    @Decorators.session
    def get_joint_by_name(self, joint_name, session=None):
        return session.query(Joint).filter(Joint.name == joint_name).first()

    @Decorators.session
    def get_flipped_joint(self, joint, session=None):
        if "right" in joint.name:
            flipped_name = joint.name.replace("right", "left")
        else:
            flipped_name = joint.name.replace("left", "right")
        return session.query(Joint).filter(Joint.name == flipped_name).first()

    @Decorators.session
    def get_joints_map(self, session=None):
        joints = session.query(Joint).all()
        return {joint.name:(joint.adj1, joint.center, joint.adj2) for joint in joints}

exercise_tag_link = Table(
    "exercise_tag_link",
    Base.metadata,
    Column("exercise_id", ForeignKey("exercise.id"), primary_key=True),
    Column("tag_id", ForeignKey("tag.id"), primary_key=True),
)


class Exercise(Base):
    __tablename__ = "exercise"
    id = Column(Integer, primary_key=True)
    name = Column(String(50))
    video_directory = Column(String(200))
    image_directory = Column(String(200))
    description = Column(String(5000))
    prom_joint_id = Column(Integer, ForeignKey("joint.id"))
    prom_joint = relationship("Joint")
    data = relationship("ExerciseData", back_populates="exercise")
    tags = relationship("Tag", secondary="exercise_tag_link", back_populates="exercises")
    attempts = relationship("Attempt", back_populates="exercise")
    plan = relationship("Plan", back_populates="exercise", uselist=False)

    def get_angles(self):
        angles = {}
        for row in self.data:
            if row.joint.name not in angles:
                angles[row.joint.name] = {}
            angles[row.joint.name][row.time] = row.angle
        return angles


class Joint(Base):
    __tablename__ = "joint"
    id = Column(Integer, primary_key=True)
    name = Column(String(30), unique=True)
    center = Column(Integer)
    adj1 = Column(Integer)
    adj2 = Column(Integer)


class ExerciseData(Base):
    __tablename__ = "exercise_data"
    exercise_id = Column(Integer, ForeignKey("exercise.id"), primary_key=True)
    exercise = relationship("Exercise", back_populates="data")
    joint_id = Column(Integer, ForeignKey("joint.id"), primary_key=True)
    joint = relationship("Joint")
    time = Column(Float, primary_key=True)
    angle = Column(Float)


class Tag(Base):
    __tablename__ = "tag"
    id = Column(Integer, primary_key=True)
    name = Column(String(50))
    exercises = relationship("Exercise", secondary="exercise_tag_link", back_populates="tags")


class Attempt(Base):
    __tablename__ = "attempt"
    id = Column(Integer, primary_key=True)
    exercise_id = Column(Integer, ForeignKey("exercise.id", ondelete="CASCADE"))
    exercise = relationship("Exercise")
    data = relationship("AttemptData", back_populates="attempt")
    datetime = Column(DateTime)
    reps = Column(Integer)
    average_accuracy = Column(Float)
    duration = Column(Float)

    @property
    def accuracy(self):
        return [(data.time, data.accuracy) for data in self.data]

    @property
    def date(self):
        return self.datetime.strftime("%m/%d/%Y, %H:%M:%S")

class AttemptData(Base):
    __tablename__ = "attempt_data"
    id = Column(Integer, primary_key=True)
    attempt_id = Column(Integer, ForeignKey("attempt.id", ondelete="CASCADE"))
    attempt = relationship("Attempt")
    time = Column(Float)
    accuracy = Column(Float)


class Plan(Base):
    __tablename__ = "plan"
    id = Column(Integer, primary_key=True)
    exercise_id = Column(
        Integer, ForeignKey("exercise.id", ondelete="CASCADE")
    )
    exercise = relationship("Exercise", back_populates="plan", single_parent=True, cascade="delete, delete-orphan")
    days_per_week = Column(Integer)
    sessions_per_day = Column(Integer)
    reps_per_session = Column(Integer)
