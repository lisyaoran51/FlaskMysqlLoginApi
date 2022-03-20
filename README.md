# Flask Mysql Login Api

This is built with flask, flask-restful, flask-jwt-extended.
Connecting to mysql or sqlite database.

## How to install?
```shell
$ pip install -r requirements.txt
```

## How to run?
-- Run Server (http://localhst:5000)
```

$ python app.py

```

## Endpoints
* `POST`    **/register**    = route for register new user
* `GET`     **/user/:id**    = get data of user with id. login required for this route.
* `DELETE`  **/user/:id**    = delete user with id. login required for this route.
* `POST`    **/login**       = route to retrieve access token
* `GET`     **/user**        = get data of current logged in user.
* `PUT`     **/user**        = update data of current logged in user.
* `DELETE`  **/user**        = delete current logged in user.

## DB Schema DDL
```sql
CREATE DATABASE user_db;
CREATE TABLE users (
user_id INTEGER AUTO_INCREMENT PRIMARY KEY, 
username VARCHAR(255), 
password VARCHAR(255), 
birthdate DATE);
```