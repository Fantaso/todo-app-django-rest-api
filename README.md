<!-- logo -->
<a href="https://www.fantaso.de">
<img src="/readme/fantaso.png" align="right" />
</a>

<!-- header -->
<h1 style="text-align: left; margin-top:0px;">
  ToDo App API
</h1>

> ToDo app with Django and django rest framework.

<!-- build -->
<!-- [![Build Status][travis-image]][travis-link] -->




Project consists to allow a client applications to consume resources for a ToDo application. It is partly tested as only and was developed as showcase only.




How ToDo App Works:
- You can create a project
- one project can have many tasks also know as to-do's, shores.
- each task can have a title, description, deadline, priority, mark it as task done and can have many comments or reminders(dates)

<br><br>

## Index:
- #### Installation
    1. Installing Django API App

- #### Usage:
    1. Access and Interact with API Front-end app (django restframework)
    2. Available Endpoints
    3. Consuming resources example with Requests Python Library (Soon... probably never)
    4. Tests INFO
    5. Access Django Admin
    6. Access Database Client - Adminer

- #### Information:
- #### Maintainer


<br><br>


## Installation:
#### 1.Installing Django API App Using ![docker-compose][docker-compose]:


1. Clone repository and go inside the repository folder "todo-app-django-rest-api"
```sh
git clone https://github.com/Fantaso/todo-app-django-rest-api.git
```

2. Build the docker images with docker-compose package  
```sh
docker-compose build
```

3. Initialize database and create the database mapping used for persistance in the ToDo app. _Docker-Compose was configured so the data created inside the container from the database service will be store in your repository's root dir. If you want the database data to be store in a docker volume, please go to the `docker-compose.yml` file and in the "Volume" section of the `db` service  choose one or the other._
```sh
docker-compose run --rm api python manage.py makemigrations
```

4. Apply the database mapping from the app to the database; migrate the database.
```sh
docker-compose run --rm api python manage.py migrate
```

5. Create the containers from the docker images and run the services needed for the ToDo App.
```sh
docker-compose up
```


<br>

#### 2. Access and Interact with API Front-end app (django restframework)

<!-- <br><br> -->


## Usage:
Once docker-compose is done downloading all images and none of the services failed after you have run the containers with `docker-compose up`

<br>

#### 1. Access and Interact with API Front-end app (django restframework)

The api fron-end application should be running and you can access it in your web browser at _http://0.0.0.0:8000/todo/_ which will take you to the web app interface that will allow you interact and use the API via the web browser.

<br>

#### 2. Available Endpoints

Endpoints are categorized by the database's table or models architecture. Models used for this example are:
1. Project model
  - `name`: project's name
  - `task_ids`: Relationship back reference with Task model. a list of id's for each task that belongs to the project
2. Task model
  - `project`: Relationship with Project model. the id of the project it belongs to.
  - `title`: 'name your task'
  - `description`: Describe your task more in detail.
  - `deadline`: set a date for a deadline if you want.
  - `priority`: Set the priority level of the task. Choices available are: low, medium, high.
  - `is_done`: Used to mark the task as done. by default is `False`.
  - `comment_ids`: Relationship back reference with Comment model. a list of id's for each comment that belongs to the task.
  - `reminder_ids`: Relationship back reference with Comment model. a list of id's for each reminder that belongs to the task.
3. Comment model
  - `comment`: add a quick comment or note to your task
  - `task`: Relationship with Task model. the id of the task it belongs to.
4. Reminder model
  - `date`: schedule a quick reminder to your task
  - `task`: Relationship with Task model. the id of the task it belongs to.

So, the database relationship between the models stays like this.
  - a project can have many tasks (one-to-many)
  - a task can have many comments and reminders (one-to-many)


<br>


###### Endpoint List
URI Example: `http://0.0.0.0:8000/todo/projects/<id>/`


| | Available Methods | URI |
| -: | :- | :- |
| | | |
| | **Project Endpoints** | |
| 1. | `GET` `POST`                      | `projects/` |
| 2. | `GET` `PUT` `PATCH` `DELETE`      | `projects/<id>/` |
| 3. | `GET` `POST`                      | `projects/<id>/tasks/` |
| 4. | `GET` `PUT` `PATCH` `DELETE`      | `projects/<id>/tasks/<id>/` |
| 5. | `GET` `POST`                      | `projects/<id>/tasks/<id>/comments/` |
| 6. | `GET` `PUT` `PATCH` `DELETE`      | `projects/<id>/tasks/<id>/comments/<id>/` |
| 7. | `GET` `POST`                      | `projects/<id>/tasks/<id>/reminders/` |
| 8. | `GET` `PUT` `PATCH` `DELETE`      | `projects/<id>/tasks/<id>/reminders/<id>/` |
| | | |
| | **Task Endpoints** | |
| 1. | `GET` `POST`                      | `tasks/` |
| 2. | `GET` `PUT` `PATCH` `DELETE`      | `tasks/<id>/` |
| 3. | `GET` `POST`                      | `tasks/<id>/comments/` |
| 4. | `GET` `PUT` `PATCH` `DELETE`      | `tasks/<id>/comments/<id>/` |
| 5. | `GET` `POST`                      | `tasks/<id>/reminders/` |
| 6. | `GET` `PUT` `PATCH` `DELETE`      | `tasks/<id>/reminders/<id>/` |
| | | |
| | **Comment Endpoints** | |
| 1. | `GET` `POST`                      | `comments/` |
| 2. | `GET` `PUT` `PATCH` `DELETE`      | `comments/<id>/` |
| | | |
| | **Reminder Endpoints** | |
| 1. | `GET` `POST`                      | `reminders/` |
| 2. | `GET` `PUT` `PATCH` `DELETE`      | `reminders/<id>/` |


<br>

Each model model endpoints follows a pattern of CRUDL (Create, Retrieve, Update, Delete and List) and a http method is allow on the API for each action.

Let's take **Comment endpoints** as an example:


| | Method | URI | Description |
| -: | :- | :- | :- |
| | URI Example:             |  `http://0.0.0.0:8000/todo/comments/<id>/` | |
| | | |
| 1. | `GET`                | `comments/`       | Get a **List** of all Comments available |   
| 2. | `POST`               | `comments/`       | **Create** a comment |    
| 3. | `GET`                | `comments/<id>/`  | **Retrieve** a comment's details with the id of the comment in the uri <id> section e.g. `comments/2/`|    
| 4. | `PUT` or `PATCH`     | `comments/<id>/`  | **Update** a comment's details |    
| 5. | `DELETE`             | `comments/<id>/`  | **Delete** a comment |    


<br>


This Pattern applied with to the **_Reminder_** endpoints shown in the previous table is also applied to all other Endpoints (Project, Task, Comment) and they are applied the same way in the nested relationships between the models. Example:



| | Method | URI | Description |
| -: | :- | :- | :- |
| | URI Example:             |  `http://0.0.0.0:8000/todo/projects/<id>/tasks/<id>` | |
| | | | |
| 1. | `GET`                | `projects/<id>/tasks/`       | Get a **List** of all Tasks available in a specific project. With project's id. e.g.: `projects/2/tasks/`  |   
| 2. | `POST`               | `projects/<id>/tasks/`       | **Create** a task for a specific project |    
| 3. | `GET`                | `projects/<id>/tasks/<id>/`  | **Retrieve** a task's details of a specific project |    
| 4. | `PUT` or `PATCH`     | `projects/<id>/tasks/<id>/`  | **Update** a task's details of a specific project |    
| 5. | `DELETE`             | `projects/<id>/tasks/<id>/`  | **Delete** a task of a specific project |    



#### 3. Consuming resources example with Requests Python Library (Soon... probably never)

<br>


#### 4. Tests INFO

To find a pattern for naming the testing methods of the application and having the data necessary to test the API djangoapp a txtfile was created. This file contains two main tables:
1. **ENDPOINTS SUMMARY** _(Which is what's describe previously in USAGE -> AVAILABLE ENDPOINTS -> ENDPOINT LIST section)_
2. **TESTS** _A table containing: Verbose name, Test method name, Http-methods, Reverse(name), Request(URI)_


| Legend | Table Column | Description |
| -: | :- | :- | :- |
|1| **Verbose name** | Action of the method humanly named (not used in the app, just for better understanding of the table of endpoints) |
|2| **Test method name** | the test case unique name (used in the app in the tests.py file in the application)' |
|3| **Http-methods** | HTTP method to test' |
|4| **Reverse(name)** | the Django "reverse" function to get the relative URI path to be used in the request to test the endpoint (not including the base_path['http://...'])' |
|5| **Request(url)** | the relative path used to test URI. <id> is the id of the object to be retrieved' |


Download the [test.txt][test-txt] or find it in the repository's root folder with name _test.txt_

<br>

#### 5. Access Django Admin

To access Django Admin you must create a user to login into the admin interface and manage and edit the database.

##### Using ![docker-compose][docker-compose]:


1. Create the a user.
```sh
docker-compose run --rm api python manage.py createsuperuser
```
You will be prompted to add a `username` and `password` for your user.



2. Visit in your web browser at _http://0.0.0.0:8000/admin_ and enter the `username` and `password` created in the previous step.  

<br>

#### 6. Access Database Client - Adminer
Access the database client at _http://0.0.0.0:8080_  
You will be prompt to enter **System**, **Server**, **Username**, **Password**, **Database** which has been pre-configured within the `docker-compose.yml`for the docker service named 'db'.

Login information:
- System = `PostgreSQL`
- Server = `db`
- Username = `todo-postgres`
- Password = `todo-password`
- Database = `todo-db`

<br><br>


## Information:
| Technology Stack |  |  |
| :- | :-: | :- |
| Python                    | ![back-end][python]                   | Back-End |
| Django                    | ![django][django]                     | Web Framework |
| Django Rest Extension     | ![api-extension][django-rest-extension]| API Django Extension |
| PostgreSQL                | ![database][postgresql]               | Database |
| Docker                    | ![container][docker]                  | Container |
| Docker-Compose            | ![container-manager][docker-compose]  | Container Manager |
| Adminer                   | ![database-client][adminer]           | Database Web Client |


<br><br>


## Maintainer
Get in touch -–> [fantaso.de][fantaso]



<!-- Links -->
<!-- Profiles -->
[github-profile]: https://github.com/fantaso/
[linkedin-profile]: https://www.linkedin.com/
[fantaso]: https://www.fantaso.de/
<!-- Extra -->
[test-txt]: test.txt

<!-- Repos -->
[github-repo]: https://github.com/Fantaso/todo-app-django-rest-api

<!-- Builds -->
[travis-link]: https://travis-ci.org/
[travis-image]: https://travis-ci.org/

<!-- images -->
[python]: readme/python.png
[django]: readme/django.png
[django-rest-extension]: readme/django-rest-extension.png
[postgresql]: readme/postgresql.png
[docker]: readme/docker.png
[docker-compose]: readme/docker-compose.png
[adminer]: readme/adminer.png
