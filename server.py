import json
import jwt
import mysql.connector
from flask import Flask, request
from flask_cors import CORS

app = Flask(__name__)
# api = Api(app)
CORS(app)
app.secret_key = b'wellThisIsMySecreteKey'

#### MySQL #######3
# initializing database connection
mydb = mysql.connector.connect(
  host="localhost",
  user="root",
  password="password",
  database = "fintech",
  auth_plugin='mysql_native_password'
)
# defining cursor to navigate through database
mycursor = mydb.cursor()

def checkLogin(userEmail,userPassword):
  query = "SELECT user_id, password FROM users WHERE email = '" + userEmail + "';"
  mycursor.execute(query)
  result = mycursor.fetchall()
  json_data = {}
  if(result):
    print(result)
    if(result[0][1] == userPassword):
      json_data["authorized"] = "True"
      json_data["id"] = result[0][0]
      json_data["message"] = "login succsfull"
    else:
      json_data["authorized"] = "False"
      json_data["id"] = "id"
      json_data["message"] = "password incorrect"
  else:
    json_data["authorized"] = "False"
    json_data["id"] = "id"
    json_data["message"] = "Email address not found"
  return (json.dumps(json_data),json_data)

######### Login ###########
@app.route('/login/<email>/<password>', methods=['GET', 'POST'])
def login(email,password):
  ret, json_data = checkLogin(email,password)
  print(ret)
  if(json_data["authorized"] == "True"):
    encoded_jwt = jwt.encode({"email": email, "password": password, "usrId": json_data["id"]}, "secret", algorithm="HS256")
    print(encoded_jwt)
    json_data["jwt"] =  str(encoded_jwt)
    ret = json.dumps(json_data)
  return (ret)

######### signup ###########
@app.route('/signup', methods=['GET', 'POST'])
def signup():
  user = request.json
  print(user)
  pairs = user.items()
  key = []
  value = []
  for k, v in pairs:
    key.append(str(k))
    value.append(str(v))
  key = tuple(key)
  value = tuple(value)
  sql = "INSERT INTO users (" + ", ".join(key) + ") VALUES (%s, %s, %s)"
  mycursor.execute(sql, value)
  mydb.commit()
  return ("success")
app.run(host='0.0.0.0', port=5002, debug=True)
