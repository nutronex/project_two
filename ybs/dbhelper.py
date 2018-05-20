import os
import json
import config
root_data_dir = os.getcwd() + os.sep + config.JSON_FILE_DIR + os.sep

def get_file_names(dir=root_data_dir,l=[]):
    for i in os.listdir(dir):
        if os.path.isdir(root_data_dir+i):
            return get_file_names(root_data_dir+i,l)
        else : l.append(dir+os.sep+i)
    return l

def importdata(c):
    file_list = get_file_names()
    for i in file_list:
        file_name =  i [i.rindex('/')+1:i.rindex('.')]
        with  open(i) as file_:
            c.ybs[file_name].insert(json.load(file_))

def initialize_data(c):
    def wrapper(fn):
        if not c.ybs.bus_stops.find_one():
            print("recreating database")
            c.drop_database('ybs')
            importdata(c)
        return fn

    return wrapper


