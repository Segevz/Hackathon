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
    all_users = read_json_file("C:\\Users\\Fanzone\\Desktop\\users.json")
    return all_users.get(id)

def update_user(query):
    all_users = read_json_file("C:\\Users\\Fanzone\\Desktop\\users.json")

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
    with open(str) as data:
        data = eval(data.read())
        data = json.dumps(data)
        data = json.loads(data)
        data = ast.literal_eval(json.dumps(data))
    return data


def save_to_json(data, file_path):
    with open(file_path,'w') as file:
        json.dump(data, file)