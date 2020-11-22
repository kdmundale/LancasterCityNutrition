# TSCT Portal

[![Build Status]()]()

An interactive web app for Lancaster City Nutrition Python, Flask, and PostgreSQL.


## Installation

Fork this repo and use `git clone` to get a copy of your fork on your local machine, then create and activate a virtual environment to install the dependencies.

```sh
$ cd LCN
$ python3 -m venv venv
$ source venv/bin/activate
$ pip install -r requirements.txt
```

Then you can run the shell script provided to create the database for the application:

```sh
$ sh bin/create-db.sh
```

You need to set environment variables in your terminal session to use any of the following `flask` commands:

```sh
$ export FLASK_APP=portal
$ export FLASK_ENV=development
```

To create the tables, you can run the following command. You'll need to run this again for any changes to `schema.sql`.

```sh
$ flask init-db
```

Mock data is stored in `tests/data.sql` and will be inserted into the test database for every test. If you would like to use the same data when developing, you can run this command to insert it into the development database.

```sh
$ flask mock-db
```


## Running the Application Locally

```sh
$ flask run
```

You should be able to view the app at [http://localhost:5000]().


## Run the Tests

```sh
$ coverage run -m pytest
$ coverage report
```

The first command runs your tests, while the second will show you a report of your total test coverage across all your modules. To generate a more detailed interactive report, run this command and view the result in your browser, which allows you to click on each module and see which lines need to be tested.

```sh
$ coverage html
$ open htmlcov/index.html
```


## Deploy to Heroku

[![Deploy](https://www.herokucdn.com/deploy/button.svg)](https://heroku.com/deploy)

If you've forked this repo, you can deploy your code by clicking the button above. On the following screen, leave the name blank and it will be generated for you.
