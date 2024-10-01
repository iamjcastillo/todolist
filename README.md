# Project Setup
This guide will walk you through configuring and running the project.


## Prerequisites
- Docker Desktop: Install Docker Desktop from Docker's official website.
- Poetry: Install Poetry, a dependency management tool for Python. Make sure to add Poetry to your system's PATH and verify the installation.


## Configuration
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
Generate migration files:
```
poetry run alembic revision -m "your_migration_message"
```

Apply migrations:
```
poetry run alembic upgrade head
```
or
```
docker-compose exec web alembic upgrade head
```

### Running the Project
Start Docker, Build and start your services:
```
docker-compose up --build
```


# Access FastAPI Documentation:
Once the services are up and running, you can access the FastAPI documentation by navigating to:
```
http://localhost:8000/docs#/
```


### Additional Information
Poetry: Manage dependencies and virtual environments with Poetry. To install any additional packages, use:
```
poetry add package-name
```
Docker: Ensure Docker is running before starting the project.
