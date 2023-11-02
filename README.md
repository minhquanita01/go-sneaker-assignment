# GO-Sneaker-Assignment

## Introduction
Firstly, I would like to express my sincere gratitude to Golden Owl Consulting Company for taking an interest in my CV, and for providing me with the opportunity to test and practice my programming skills. During the process of completing the tasks, there might have been some shortcomings, for which I hope to receive understanding from your esteemed company.

## Usage
Here's how to set up this project on your local machine:

- Install MySQL Server and MySQL Workbench, then execute the script at [`script_db.sql`](./myproject/script_db.sql).
- Go to [`setting.py`](./myproject/go_sneaker/go_sneaker/settings.py) to update the username and password.
- Activate the virtual environment (already present in the `myproject` folder) using the file [`myproject/Scripts/activate`](./myproject/Scripts/activate).
- In the `myproject` directory, run the command `pip install -r requirements.txt` for Python to install the necessary libraries onto the virtual environment.
- Migrate table in database by using command `python manage.py makemigrations go_shoes` then `python manage.py migrate`
- Then, navigate to the [`/myproject/go_sneaker`](./myproject/go_sneaker) directory and execute the command `python manage.py collectstatic` to create a container for asset files.
- Launch the server using the command `python manage.py runserver`.
