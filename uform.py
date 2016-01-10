from uuid import uuid4
from peewee import Model, PrimaryKeyField, UUIDField
from playhouse.postgres_ext import PostgresqlExtDatabase, BinaryJSONField


class UForm(Model):
    """A lightweight U-Form implementation based on PostgreSQL's JSONB Binary
       JSON datatype. PostgreSQL's Binary JSON enables the storage of key-value
       pairs tied to a UUID. See https://en.wikipedia.org/wiki/U-form
       Serial IDs are kept to provide query performance where UUIDs are not
       required. UUIDs are provided to guarantee identity universally and
       eliminate data silos.
    """
    id = PrimaryKeyField()
    uuid = UUIDField(default=uuid4)
    attrs = BinaryJSONField()

    @classmethod
    def store(cls, **kv):
        """
        Takes a dictionary and sets the JSON attrs based on the dict.
        """
        cls.create(attrs=kv)
