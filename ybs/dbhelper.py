import os
import pymongo
import json
import functools
import config
root_data_dir = os.getcwd() + os.sep + config.JSON_FILE_DIR + os.sep
mongodb_connection = pymongo.MongoClient(config.MONGODB_HOST,config.MONGODB_PORT)

#def get_file_names(dir=root_data_dir,l=[]):
#    for i in os.listdir(dir):
#        if os.path.isdir(root_data_dir+i):
#            return get_file_names(root_data_dir+i,l)
#        else : l.append(dir+os.sep+i)
#    return l



def importdata(c):
    file_list = config.JSON_FILES
    for i in file_list:
        i = root_data_dir + os.sep + i
        file_name =  i [i.rindex('/')+1:i.rindex('.')]
        print(file_name)
        with  open(i) as file_:
            c.ybs[file_name].insert(json.load(file_))

def initialize_data(fn):
    @functools.wraps(fn)
    def wrapper(*a,**ka):
        if not mongodb_connection.ybs.bus_stops.find_one():
            print("recreating database")
            mongodb_connection.drop_database('ybs')
            importdata(mongodb_connection)
        return fn(*a,**ka)
    return wrapper


