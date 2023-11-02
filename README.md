# GO-Sneaker-Assignment

## Introduction
Firstly, I would like to express my sincere gratitude to Golden Owl Consulting Company for taking an interest in my CV, and for providing me with the opportunity to test and practice my programming skills. During the process of completing the tasks, there might have been some shortcomings, for which I hope to receive understanding from your esteemed company.

## Usage
Here's how to set up this project on your local machine:

- Create new virtual environment then clone my repository in the virtual environment dicrectory.
- After that, go to `Scripts` directory to activate the virtual environment that you created (run file [`activate`]).
- Install MySQL Server and MySQL Workbench, then execute the script at [`script_db.sql`](./script_db.sql).
- Go to [`setting.py`](./go_sneaker/go_sneaker/settings.py) to update the username and password.
- Run the command `pip install -r requirements.txt` for Python to install the necessary libraries onto the virtual environment.
- Navigate to the [`/go_sneaker`](./go_sneaker) directory and migrate table in database by using command `python manage.py makemigrations go_shoes` then `python manage.py migrate`
- Then execute the command `python manage.py collectstatic` to create a container for asset files.
- Launch the server using the command `python manage.py runserver`.
