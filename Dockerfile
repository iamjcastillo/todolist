# Use an official Python image from the slim-buster family
FROM python:3.11-slim

# Set environment variables
ENV POETRY_VERSION=1.8.0
ENV POETRY_VIRTUALENVS_CREATE=false

# Set working directory
WORKDIR /myapp

# Install dependencies required to install Poetry and build the app
RUN apt-get update && apt-get install -y curl build-essential libpq-dev && \
    apt-get clean && rm -rf /var/lib/apt/lists/*

# Install Poetry
RUN curl -sSL https://install.python-poetry.org | python3 - && \
    ln -s /root/.local/bin/poetry /usr/local/bin/poetry

# Copy pyproject.toml and poetry.lock to the container
COPY pyproject.toml poetry.lock* /myapp/

# Install Python dependencies via Poetry
RUN poetry install --no-root --no-interaction --no-ansi

# Copy the app code into the container
COPY ./myapp /myapp/app

# Set the PYTHONPATH to the app directory
ENV PYTHONPATH=/myapp/app

# Expose the port FastAPI runs on
EXPOSE 8000

# Command to run the app with uvicorn
CMD ["uvicorn", "myapp.main:app", "--host", "0.0.0.0", "--port", "8000"]
