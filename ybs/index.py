#!/usr/bin/python3
from flask import Flask , request , redirect , url_for , render_template,escape

import sys
import os
import json
import pymongo
import config
import dbhelper

app = Flask(__name__)
app.config['DEBUG'] = config.DEBUG
mongodb_connection = pymongo.MongoClient(config.MONGODB_HOST,config.MONGODB_PORT)

@app.route("/")
@dbhelper.initialize_data(mongodb_connection)
def index():
    bus_lines = [ x['bus_id'] for x in mongodb_connection.ybs.buslines.find({},{'bus_id':1}) ]
    bus_stops = [ "%s"%x['name']   for x in mongodb_connection.ybs.bus_stops.find({},{'name':1})  ]
    return render_template('index.html',bus_lines=bus_lines , bus_stops = bus_stops)

@app.route('/bus_stop/<path:x>')
@dbhelper.initialize_data(mongodb_connection)
def bus_stop_id(x):
    return json.dumps(mongodb_connection.ybs.bus_stops.find_one({'name':x},{'_id':0}))

@app.route('/bus/<int:x>')
@dbhelper.initialize_data(mongodb_connection)
def bus_id(x):
    return json.dumps(mongodb_connection.ybs.buslines.find_one({'bus_id':x},{ '_id':0}))


@app.route('/getpath/<x>')
def getpath(x):
    with open(root_data_dir+'geojson'+'/route'+x+'.geojson') as f:
        return json.dumps(json.load(f))

def main(arg):
    print(bus_id(sys.argv[-1]))


if __name__ == "__main__":
    app.run()
#    main(sys.argv)
