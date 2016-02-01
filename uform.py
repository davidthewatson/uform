import os

from uuid import uuid4
from peewee import Model, PrimaryKeyField, UUIDField
from playhouse.postgres_ext import PostgresqlExtDatabase, BinaryJSONField


class UForm(Model):
    """
       A lightweight U-Form implementation based on PostgreSQL's JSONB Binary
       JSON datatype. PostgreSQL's Binary JSON enables the storage of key-value
       pairs tied to a UUID. See https://en.wikipedia.org/wiki/U-form
       Serial IDs are kept to provide query performance where UUIDs are not
       required. UUIDs are provided to guarantee identity universally and
       eliminate data silos.
    """
    id = PrimaryKeyField()
    uuid = UUIDField(default=uuid4)  # FIXME: move uuid init to PostgreSQL
    attrs = BinaryJSONField()

    @classmethod
    def store(cls, **kv):
        """
        Takes a dictionary and sets the JSON attrs based on the dict.
        """
        cls.create(attrs=kv)

    @classmethod
    def add_derivative(cls, name):
        """
        Takes a name and creates the database, table, and derived uform class.
        The system calls belong in a layer above the database that uses one
        database per logged in user and one table per derived u-form class.
        This is a hack pointed in that direction. Refactor necessary.
        """
        os.system('dropdb {}'.format(name))
        os.system('createdb {}'.format(name))
        os.system('psql -d {} -a -f enable_hstore.sql'.format(name))

        db = PostgresqlExtDatabase(name, user='dwatson')
        Cls = type(name.title(), (cls,),
                   {'Meta': type('Meta', (), {'database': db})})
        Cls.create_table(fail_silently=False)
        return Cls
