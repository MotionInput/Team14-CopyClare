from copyclare.model import database
from copyclare import DATA_PATH
from copyclare.model.attempt import Attempt
from copyclare.model.exercises import Exercise
from copyclare.model.user import User



if __name__ == "__main__":
    data = database.main()
    
    #data.init_user("tianhao Chen")
    #data.add_exercise(Exercise("a","b","c","d","e","f"))
    #x = data.get_exercises("video_directory","b")
    #x = data.get_all_categories()
    data.add_attempt(1,2,3,4,"tianhao chen",1)
    
    
    #print(x)

    pass
