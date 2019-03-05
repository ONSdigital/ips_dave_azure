# azure_pipelines
Creates docker image containing flask app

## Running the website as dokcer container

1. Run the following command to build the docker image  
`$ docker build -t myapp:1.0 .`

2. Run the following command to run the image  
`$ docker run -d -p 5000:5000 myapp:1.0`

3. Access the website by navigating to  
`http://127.0.0.1:5000`

---

## Running MySQL in a docker container

1. Use docker compose to run the database in a container  
`$ cd db`  
`db $ docker-compose up`

MySQL is now running in the container with a `sqldb` database and you can login to the adminer interface on `http://localhost:8080`

You can connect to the database on localhost port:3310, using root and password defined in docker-compse file.

--
## Initialising DB with data

[Alembic](https://alembic.sqlalchemy.org/en/latest/) is used to update database schema and insert data. Once you have the MySQL docker conatiner running, you can use Alembic to create the database schema.
The connection string for the database is given in `alembic.ini` file

If you are running Alembic for the first time, run the following command:  
`$ pip install -r requirements.txt`

Run the initialise script:  
`$ alembic upgrade head`

If you want to rollback a script:  
`$ alembic downgrade base`

If you want to add a new script to modify schema/modify data:  
`$ alembic revision -m "sensible comment here"`  
This will create a new file in `versions` folder you can add your code under `upgrade()` & `downgrade()` functions. For more information on Alembic commands check [this page](https://eticlab.co.uk/alembic-database-migrations-using-python/).