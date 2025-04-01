from sqlalchemy import create_engine, event
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
from .controller.app_config import app_config

# MySQL Database Connection
mysql_engine = create_engine(app_config.MYSQL_CONNECTION_STRING, pool_pre_ping=True, echo=False)
SessionLocalMySQL = sessionmaker(autocommit=False, autoflush=False, bind=mysql_engine)
BaseMySQL = declarative_base()

# Function to replace placeholders with actual values in executed SQL MySQL queries
def set_params(stmt, params):
    """
    Replace placeholders with actual values in the SQL statement.
    """
    try:
        if isinstance(params, dict):
            for key, value in params.items():
                placeholder = f":{key}" if f":{key}" in stmt else f"%({key})s"
                stmt = stmt.replace(placeholder, f"'{value}'" if isinstance(value, str) else str(value))
        return stmt
    except Exception as e:
        print("Error in set_params:", e)
        return stmt

@event.listens_for(mysql_engine, "before_cursor_execute")
def replace_placeholders_with_values(conn, cursor, statement, parameters, context, executemany):
    """
    Print the executed SQL MySQL query with actual parameter values.
    """
    try:
        if executemany and isinstance(parameters, list):
            for param_set in parameters:
                stmt = set_params(statement, param_set)
                print("\n[EXECUTED SQL MySQL]:\n", stmt, "\n")
        elif isinstance(parameters, dict):
            stmt = set_params(statement, parameters)
            print("\n[EXECUTED SQL MySQL]:\n", stmt, "\n")
    except Exception as e:
        print("Failed to replace placeholders in SQL statement:", e)

# Dependency for MySQL
def get_mysql_db_con():
    """
    Function to establish connection to MySQL database.
    """
    print(f"MySQL Connection String: {app_config.MYSQL_CONNECTION_STRING}")
    db = SessionLocalMySQL()
    try:
        yield db
    finally:
        db.close()
