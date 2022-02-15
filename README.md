# Changelog
All notable changes to this project will be documented in this file.

## [1.0.0] - 2022-02-13
### Added
* Initial commit.
## [1.0.1] - 2022-02-14
### Added
* README file added.
### Changed
* ER diagram updated.
* Models.py updated.
## [1.0.2] - 2022-02-15
### Added
* Index, login and registration page added.
* Human-readable changelog added.

# LTC++

## a Moodle-like website

### Database demo

![ER Diagram](https://github.com/XinyuGitHub/MoodlePlus/blob/master/ERD_Feb15.png)

Here is how to populate some dummy data into the database for testing.

* First, set up your virtual environment with Django==2.2.
* Run the following commands to create a database because \*.sqlite3 files will not be tracked by Git.

```
python manage.py makemigrations Demo
python manage.py migrate
```

* Then, we need to populate dummy data and start the server:

```
python populate_demo.py
python manage.py runserver
```

Then, go to

```
http://127.0.0.1:8000/admin/
```

To gain administrative access, please log in with the following information.

```
Username: 	admin
Password: 	123456
```

### Backend demo
* You will be able to visit the index page now.
```
http://127.0.0.1:8000/demo/
```
* Follow the links on that page to register and log in, or click the links below.
```
http://127.0.0.1:8000/demo/register/
http://127.0.0.1:8000/demo/login/
```
