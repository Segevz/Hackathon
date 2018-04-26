import json
import ast
import Config
from Config import USERS_LOC, COURSES_LOC
# USER
def add_user(query):
    data = read_json_file(USERS_LOC)
    Config.id+=1
    data[id] = query
    save_json_file(data)


def get_users_query(query):
    return false


def get_user(id):
    all_users = ""
    return user


def update_user(query):
    return

# COURSE
def get_course_query(school):
    return queryset

# SCHOOL
def get_all_schools():
    return Config.schools


# JSON
def read_json_file(str):
    # data = open("C:\\Users\\Fanzone\\Desktop\\test.json")
    data = open(str)
    data = eval(data.read())
    data = json.dumps(data)
    data = json.loads(data)
    data = ast.literal_eval(json.dumps(data))
    return data
