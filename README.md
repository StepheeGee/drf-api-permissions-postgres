# Wigs Project - DRF, Permissions, and Postgres Integration

## Author: Stephanie G. Johnson

**Date**: 02-20-2024

## Lab 32 - Description

The Wigs project is a Django REST Framework application designed to manage information about wigs. This includes details such as wig name, color, length, curl pattern, density, hair origin, description, and price. The project utilizes Docker for containerization, making it easy to deploy and manage the application in various environments. We've enhanced the project with Permissions and integrated PostgreSQL for robust data storage.

This project serves as a wig website where any user can view the wigs available in stock. However, to perform actions such as purchasing a wig or customizing it (adding to the cart, deleting, or editing quantities), users must be authenticated.

## Requirements

- **Docker:** The project uses Docker for containerization, allowing for consistent and reproducible deployments.
- **Django:** A high-level Python web framework used to build the backend of the Wigs project.
- **Django REST Framework:** A powerful and flexible toolkit for building Web APIs in Django.

## Features

- **CRUD Operations:** Create, Read, Update, and Delete wigs.
- **Customization:** Users can customize wigs based on their preferences.
- **Authentication:** Only authenticated users can perform purchase and customization actions.
- **Switch User:** Users can switch directly from the browsable API.

## Links and Resources

- [Django Documentation](https://docs.djangoproject.com/): Official documentation for the Django web framework.
- [Django REST Framework Documentation](https://www.django-rest-framework.org/): Documentation for the Django REST Framework.
- [Docker Documentation](https://docs.docker.com/): Official documentation for Docker, the containerization platform.

## Setup

1. **Clone the Repository:**

    ```bash
    # Clone the Repository
    git clone https://github.com/stephegee/drf-api-permissions-postgres.git
    cd wigs_project
    ```

2. **Build and Run Docker Container:**

    ```bash
    # Build and Run Docker Container
    docker-compose up --build
    ```

3. **Run Migrations:**

    ```bash
    # Run Migrations
    docker-compose exec web python manage.py makemigrations
    docker-compose exec web python manage.py migrate
    ```

4. **Access the API:**

    The API should be accessible at [http://localhost:8000/api/](http://localhost:8000/api/).

## Virtual Environment

This project includes a virtual environment to isolate Python dependencies. Activate the virtual environment using the following commands:

```bash
# On Windows
.\venv\Scripts\activate

# On Unix or MacOS
source venv/bin/activate
```

Install dependencies while the virtual environment is active:

```bash
pip install -r requirements.txt
```

Deactivate the virtual environment when done:

```bash
deactivate
```

## Tests

To run tests for the Wigs project, use the following command:

```bash
docker-compose run web python manage.py test
```

Ensure that the application is running, and the necessary dependencies are installed before running the tests.

## Additional Resources

- [Django for Beginners](https://djangoforbeginners.com/): A comprehensive beginner-friendly guide to Django.
- [Django REST Framework Tutorial](https://www.django-rest-framework.org/tutorial/quickstart/): Quickstart guide for Django REST Framework.
- [Dockerizing Django with Postgres, Gunicorn, and Nginx](https://testdriven.io/blog/dockerizing-django-with-postgres-gunicorn-and-nginx/): A tutorial on Dockerizing a Django application with Postgres, Gunicorn, and Nginx.
- [Permissions & Postgresql](https://testdriven.io/blog/permissions-and-postgresql/): A tutorial on Permissions and Postgresql.

## Thank You
