Microservice for adding, updating, and deleting users (firstname, lastname, email) using a PostgreSQL database.

## How to execute in Linux:

1. Create and activate the virtual environment:

python3 -m venv env
source env/bin/activate

2. Install the dependencies:

pip install -r requirements.txt

3. Environment setup:
Copy the .env.dist file to .env and fill in your PostgreSQL database credentials:

cp .env.dist .env

4. Apply database migrations:
Before running the app, create the necessary tables in your database:

flask db upgrade

5. Execute the project:

flask run