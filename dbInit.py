import mysql.connector
from os import listdir

mydb = mysql.connector.connect(
  host="localhost",
  user="root",
  password="password",
  database = "fintech",
  auth_plugin='mysql_native_password'
)

mycursor = mydb.cursor()

mycursor.execute("CREATE TABLE IF NOT EXISTS users (user_id INT AUTO_INCREMENT PRIMARY KEY, "
                                                        "email VARCHAR(255) , "
                                                        "password VARCHAR(255), "
                                                        "type VARCHAR(255))")
mycursor.execute("CREATE TABLE IF NOT EXISTS products (product_id INT AUTO_INCREMENT PRIMARY KEY, "
                                                        "title VARCHAR(255) , "
                                                        "date_added VARCHAR(255), "
                                                        "dated_updated VARCHAR(255), "
                                                        "image VARCHAR(255), "
                                                        "description VARCHAR(255), "
                                                        "price VARCHAR(255))")
mycursor.execute("CREATE TABLE IF NOT EXISTS categories (category_id INT AUTO_INCREMENT PRIMARY KEY, "
                                                        "category_name VARCHAR(255))")
mycursor.execute("CREATE TABLE IF NOT EXISTS category_product_link (link_id INT AUTO_INCREMENT PRIMARY KEY, "
                                                        "category_id INT, "
                                                        "product_id INT, "
                                                        "FOREIGN KEY (category_id) REFERENCES categories(category_id), "
                                                        "FOREIGN KEY (product_id) REFERENCES products(product_id))")
