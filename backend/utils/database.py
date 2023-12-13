"""Database module."""

from contextlib import contextmanager, AbstractContextManager
from typing import Callable

from sqlalchemy import create_engine, orm
from sqlalchemy.orm import Session

class Database:
    def __init__(self, db_url: str) -> None:
        self._engine = create_engine(db_url)
        self._session_factory = orm.scoped_session(
            orm.sessionmaker(
                autocommit=False,
                autoflush=False,
                bind=self._engine,
            ),
        )

    @contextmanager
    def session(self) -> Callable[..., AbstractContextManager[Session]]:
        session: Session = self._session_factory()
        try:
            yield session
        except Exception:
            session.rollback()
            raise
        finally:
            session.close()

# class Database:
#     def __init__(self, db_url: str) -> None:
#         self._engine = create_engine(db_url, echo=True)
#
#     def session(self) -> Session:
#         session: Session = Session(bind=self._engine)
#         try:
#             return session
#         except Exception:
#             session.rollback()
#             raise Exception("DB Exception")
#         finally:
#             session.close()

def get_connection_url(database_setting) -> str:
    return f"postgresql+psycopg2://{database_setting.user()}:{database_setting.password()}" \
           f"@{database_setting.host()}:{database_setting.port()}/{database_setting.database_name()}"