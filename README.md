# User Management Microservice

Microservice for adding, updating, and deleting users (firstname, lastname, email) using a PostgreSQL database.

## How to execute in Linux:

**1. Create and activate the virtual environment:**
```bash
python3 -m venv env
source env/bin/activate
```

**2. Install the dependencies:**
```bash
pip install -r requirements.txt
```

**3. Environment setup:**
Copy the `.env.dist` file to `.env` and fill in your PostgreSQL database credentials:
```bash
cp .env.dist .env
```

**4. Apply database migrations:**
Before running the app, create the necessary tables in your database:
```bash
flask db upgrade
```

**5. Execute the project:**
```bash
flask run
```
