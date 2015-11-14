#!/usr/bin/env python
import MySQLdb
import json, ast

class Database:
    host="localhost"
    user="root"
    passwd="test"
    db="paul_test"

    def __init__(self):
        self.conn = MySQLdb.connect(self.host,self.user,self.passwd,self.db)
        self.cursor = self.conn.cursor()

    def __del__(self):
        self.conn.close()

    def insert_to_table(self,table,project_object):
        query="INSERT INTO "+table+" VALUES ('" + project_object.project_name + "','"+project_object.project_status+"') ON DUPLICATE KEY UPDATE project_status='"+project_object.project_status+"';"
        print query
        try:
           self.cursor.execute(query)
           self.conn.commit()
           return True
        except:
           self.conn.rollback()
           return False

class ProjectStatus:
    def __init__(self,j):
        self.__dict__ = ast.literal_eval(json.dumps(j))

    def toJson(self):
        return json.dumps(self, default=lambda o: o.__dict__, sort_keys=True, indent=4)

