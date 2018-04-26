import json
import ast
import Config
from Config import USERS_LOC, COURSES_LOC, SCHOOLS_LOC

# USER
def add_user(query):
    data = read_json_file(SCHOOLS_LOC)
    Config.id+=1
    data[id] = query
    save_json_file(data, SCHOOLS_LOC)

def get_all_users():
    pass

def get_users_query(query):
    pass

def get_user(id):
    all_users = read_json_file("users.json")
    return all_users.get(id)

def update_user(query):
    all_users = read_json_file("users.json")

    return

def get_users_per_course ():
    all_users = read_json_file("users.json")

# COURSE
def get_courses_for_school(school):
    all_courses = read_json_file("courses.json")
    return all_courses.get(school)

# SCHOOL
def get_all_schools():
    return Config.schools


# JSON
def read_json_file(str):
    # data = open("C:\\Users\\Fanzone\\Desktop\\test.json")
    with open(str) as data:
        data = eval(data.read())
        data = json.dumps(data)
        data = json.loads(data)
        data = ast.literal_eval(json.dumps(data))
    return data


def save_json_file(data, file_path):
    with open(file_path, 'w') as file:
        json.dump(data, file)