# PROJECT-BETA
## REST APIs with Flask and Python
A Flask based RESTful API using SQLAlchemy to communicate with SQLite
### How To Run
1. Install `virtualenv`:
```
$ pip install virtualenv
```

2. Open a terminal in the project root directory and run:
```
$ virtualenv env
```

3. Then run the command:
```
$ .\env\Scripts\activate
```

4. Then install the dependencies:
```
$ (env) pip install -r requirements.txt
```

5. Finally start the web server:
```
$ (env) python app.py
```

#### Tech Stack:

 - **Web framework:** Flask
 - **ORM:** SQLAlchemy
 - **Database:** SQLite
 - **Containerization:** Docker
 - **WSGI Server:** Gunicorn
 - **Reverse Proxy Server:** NGINX
 
 
 ## API
 
 | Endpoint | HTTP Method | Result |
|:---|:---:|---|
| `/register`  | `POST`  | Registers a new user  |
| `/auth`  | `POST`  | Login the user  |
| `/store/<name>`  | `POST`  | add a new store to inventory |
| `/store/<name>`  | `GET`  | display a individual store   |
| `/item/<name>`  | `POST`  | add a item to inventory  |
| `/item/<name>`  | `GET`  | display a individual item from inventory |
| `/item/<name>`  | `DELETE`  | remove a particular item from inventory  |
| `/item/<name>`  | `PUT`  | update the item entry  |
| `/store/<name>`  | `DELETE`  | remove a particular store from inventory  |
| `/multi`  | `POST`  | add multiple items to inventory at a time  |
| `/upload`  | `POST`  | add multiple items to inventory at a time through .csv file  |
| `/stores`  | `GET`  | display all stores from inventory  |
| `/items`  | `GET`  | display all the items from inventory  |
