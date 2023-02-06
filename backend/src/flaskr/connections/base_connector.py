import abc
from contextlib import contextmanager
from typing import List, Dict

import pandas as pd
from src.flaskr.utils.log_config.logging_conf import logger
from sqlalchemy.engine.interfaces import Connectable
from sqlalchemy.orm import sessionmaker


class Database(abc.ABC):
    def __init__(self, engine: Connectable = None):
        if engine is None:
            self.engine = self.create_engine(self.retrieve_credentials())
        else:
            self.engine = engine

        self._Session = sessionmaker(bind=self.engine)
        logger.info(f"Database engine created: {self.engine}")

    @abc.abstractmethod
    def create_engine(self, secret_dict: Dict[str, str]):
        pass

    @abc.abstractmethod
    def retrieve_credentials(self) -> Dict[str, str]:
        pass

    @contextmanager
    def session_scope(self):
        """
        Provide a transactional scope around a series of operations
        """
        session = self._Session()
        try:
            yield session
            session.commit()
        except:
            session.rollback()
            raise
        finally:
            session.close()

    def execute(self, sql_cmds: List):
        """
        Executes a list of sql commands using the self managed session
        """
        assert type(sql_cmds) == list, "SQL commands must be in list format"
        with self.session_scope() as session:
            for cmd in sql_cmds:
                logger.debug(f"Executing SQL cmd: {cmd}")
                session.execute(cmd)

    def query(self, sql_cmd: str):
        """
        Executes and returns the results of a sql SELECT using the self-managed session
        Returns a pandas dataframe
        """
        with self.session_scope() as session:
            logger.debug(f"Querying: {sql_cmd}")
            query = session.execute(sql_cmd)
            rows = query.fetchall()

        return pd.DataFrame(rows, columns=query.keys())
