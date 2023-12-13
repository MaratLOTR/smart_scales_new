from sqlalchemy import inspect

from models import Base


def asdict(model: Base) -> dict:
    return {c.key: getattr(model, c.key) for c in inspect(model).mapper.column_attrs}