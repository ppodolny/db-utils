#!/usr/bin/env python

from libs import *
from flask import Flask , request

app = Flask(__name__)

table="t2"


@app.route("/", methods=['POST'])
def update_status():
    #print request.get_json()
    project = ProjectStatus(request.get_json())
    try:
        db=Database()
        db.insert_to_table(table, project)
        return "status updated"
    except:
        return "could not create db object"


if __name__ == "__main__":
    app.run(debug=True)

