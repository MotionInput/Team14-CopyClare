from copyclare.model import database
from copyclare import DATA_PATH
from copyclare.model.attempt import Attempt
from copyclare.model.exercises import Exercise
from copyclare.model.user import User
from copyclare.model.exporter import Exporter

if __name__ == "__main__":
    data = database.main()

    # data.init_user("tianhao Chen")
    # data.add_exercise(Exercise("a", "b", "c", "d", "e", "f"))
    # x = data.get_exercises("video_directory", "b")
    # x = data.get_all_exercises()
    # x = data.get_all_categories()
    # data.add_attempt(Attempt(1, 2, 3, 4, "tianhaochen", 1, 2))
    # attempts = data.get_all_attempts()
    # for attempt in attempts:
    #     exe_id = attempt.exercise_id
    #     exe = data.get_one_exercise_by_ID(exe_id)
    #     exe_name = exe.name
    #     exe_des = exe.description
    #     print(exe_id, exe_name, exe_des)

    # print(x)

    # pass

    exporter = Exporter(data)
    exporter.export("test.docx")
