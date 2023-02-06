import pandas as pd
from sqlalchemy import text
from src.flaskr.connections.base_connector import Database
from src.flaskr.utils.log_config.logging_conf import logger


def connect(db: Database = None) -> pd.DataFrame:
    logger.info("Reading from mysql")
    with db.session_scope() as session:
        df = pd.read_sql_query(text("select * from SHOP.test"), session.connection())

    return df
