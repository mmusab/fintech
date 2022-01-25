# Intro
In the project angular is used at frontend, Flask server is deployed for backend and MySQL is used for database management.
YOu need to reset username and password for MySQL in both server.py and dbInit.py.

#### Server
Run server through python3 using following command.
```sh
python3 server.py
```
Above command will run flask server on port 5002 and endpoint is accessible at.

#### MySQL
MySQL is used as a database with four tables:
###### products
###### users
###### categories
###### category_product_link
following ERD is showing tables and there relationship.
![alt text](https://github.com/[mmusab]/[fintech]/blob/[main]/ERD.png?raw=true)

dbInit.py is used to setup database and tables run this using following command to setup database.
