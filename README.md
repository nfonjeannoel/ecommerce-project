# Ecommerce Project

This is an ecommerce project that provides a backend API for managing users, addresses, products, and orders. It is built using FastAPI, SQLAlchemy, and Alembic.

## Getting Started

### Prerequisites

- Python 3.9 or higher
- PostgreSQL database (or any other supported by SQLAlchemy)

### Installation

1. Clone the repository:

   ```shell
   git clone https://github.com/nfonjeannoel/ecommerce-project.git
   cd ecommerce-project
   ```

2. Create a virtual environment and activate it:

   ```shell
   python3 -m venv venv
   source venv/bin/activate
   ```

3. Install the dependencies:

   ```shell
   pip install -r requirements.txt
   ```

4. Set up the database:

   - Create a PostgreSQL database.
   - Configure the database connection URL in the `.env` file:

     ```dotenv
     DATABASE_URL=postgresql://user:password@localhost:5432/database_name
     ```

   - Apply the initial database migration:

     ```shell
     alembic upgrade head
     ```

5. Start the server:

   ```shell
   uvicorn main:app --reload
   ```

   The API will be available at http://localhost:8000.

## Project Structure

- `app/`: Contains the main FastAPI application code.
- `alembic/`: Contains the Alembic migration scripts.
- `models.py`: Defines the database models using SQLAlchemy ORM.
- `schemas.py`: Defines the Pydantic schemas for request/response validation.
- `database.py`: Provides the database connection and session management.
- `main.py`: Entrypoint for the FastAPI application.

## Database Migration

This project uses Alembic for database migration management. The migration scripts can be found in the `alembic/versions/` directory. To create a new migration script after making changes to the models, run:

```shell
alembic revision --autogenerate -m "description"
```

To apply the migrations:

```shell
alembic upgrade head
```

For more information on using Alembic, refer to the [Alembic documentation](https://alembic.sqlalchemy.org/en/latest/).

## Contributing

Contributions are welcome! If you find any issues or want to add new features, feel free to open an issue or submit a pull request.

## License

This project is licensed under the MIT License. See the `LICENSE` file for more information.
```

Feel free to modify and expand the `README.md` file based on your project's specific details and requirements.