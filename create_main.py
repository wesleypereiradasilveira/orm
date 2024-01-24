
from conf.db_session import create_tables

if __name__ == "__main__":
    # create_tables(sqlite=True) # SQLite
    create_tables() # Postgres

