# Dockerfile
#Use an official Python runtime as a parent image
FROM python:3.11.5-slim-bullseye


# Set environment variables
ENV PIP_DISABLE_PIP_VERSION_CHECK 1
ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

# Set the working directory to /code
WORKDIR /code

# Install any needed packages specified in requirements.txt
COPY ./requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# Copy the current directory contents into the container at /code
COPY . .




