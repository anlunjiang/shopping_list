from src.flaskr.connections.mysql.mysql_connector import MySQLDatabase
from src.flaskr.dao.internal import Base


def initialise_database():
    db = MySQLDatabase()

    with db.session_scope() as session:
        tables = Base.metadata.tables.keys()
        table_names_str = ", ".join(tables)

        print(f"Deleting tables if exists: {table_names_str}")

        Base.metadata.drop_all(session.get_bind())

        print(f"Creating tables: {table_names_str}")

        Base.metadata.create_all(session.get_bind())


if __name__ == "__main__":
    initialise_database()
