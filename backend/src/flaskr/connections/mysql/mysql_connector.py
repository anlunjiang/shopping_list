from typing import Dict
import sys
import sqlalchemy as sa

from src.flaskr.connections.base_connector import Database


class MySQLDatabase(Database):
    def __init__(self):
        super().__init__()

    def create_engine(self, secret_dict: Dict[str, str]):
        conn_str = str(
            "mysql+pymysql://{user}:{pwd}@{host}:{port}/{dbname}".format(
                user=secret_dict["db_user"],
                pwd=secret_dict["db_pwd"],
                host=secret_dict["db_host"],
                port=secret_dict["db_port"],
                dbname=secret_dict["db_name"],
            ),
        )
        self.engine = sa.create_engine(conn_str, pool_recycle=1)
        return self.engine

    def retrieve_credentials(self) -> Dict[str, str]:
        if sys.platform == "darwin":
            host = "127.0.0.1"
        else:
            host = "shop_db"
        return {
            "db_user": "aj2814",
            "db_pwd": "1234",
            "db_host": host,
            "db_port": "3306",
            "db_name": "SHOP",
        }
