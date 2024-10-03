# Project Setup
This guide will walk you through configuring and running the project.


## Prerequisites
- Docker Desktop:  
  Install Docker Desktop from Docker's official website. https://www.docker.com/products/docker-desktop/
- Poetry:  
  Install Poetry. https://python-poetry.org/docs/  
  Make sure to add Poetry to your system's PATH and verify the installation.
  ```
  poetry --version
  ```


## Configuration
Navigate to the root of the folder where you cloned the repository.  

### Configure Docker:
Pull the Postgres image from Docker:
```
docker pull postgres
```

### Install requirements:
```
poetry install
```

### Initialize Alembic:
First, you'll need to apply the migrations:
```
poetry run alembic upgrade head
```
or
```
docker-compose exec web alembic upgrade head
```

In case you need to generate additional migration files, run:
```
poetry run alembic revision -m "your_migration_message"
```

### Running the Project
Start Docker, Build and start your services:
```
docker-compose up --build
```

### Seed
In order to speed up the testing process, you can run the following command to generate some demo To Do lists:
```
python seed.py
```


# Access FastAPI Documentation:
Once the services are up and running, you can access the FastAPI documentation by navigating to:
```
http://localhost:8000/docs#/
```


### Additional Information
- Poetry:  
Manage dependencies and virtual environments with Poetry. To install any additional packages, use:
```
poetry add package-name
```
- Docker:  
Ensure Docker is running before starting the project.
- Python:
The minimum version to run this project is 3.8.

