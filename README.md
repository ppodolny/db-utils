Installation
============

pip install -r requirements.txt


Usage:
=======

Say we have the following table (t2) structure in MySQL:

+----------------+-------------+------+-----+---------+-------+
| Field          | Type        | Null | Key | Default | Extra |
+----------------+-------------+------+-----+---------+-------+
| project_name   | varchar(40) | NO   | PRI |         |       |
| project_status | varchar(20) | YES  |     | NULL    |       |
+----------------+-------------+------+-----+---------+-------+

Current status is:

mysql> select * from t2;
+--------------+----------------+
| project_name | project_status |
+--------------+----------------+
| myproj         | stopped      |
| myproj2        | stopped      |
+--------------+----------------+
2 rows in set (0.00 sec)


And we want to update 'project_status' of specific 'project_name' (myproj2 in this case):

curl -H "Content-Type: application/json" -X POST -d '{"project_name": "myproj2", "project_status": "running"}' localhost:5000

mysql> select * from t2;
+--------------+----------------+
| project_name | project_status |
+--------------+----------------+
| babu         | stopped        |
| bla          | running        |
+--------------+----------------+
2 rows in set (0.00 sec)

