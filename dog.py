from playhouse.postgres_ext import PostgresqlExtDatabase, BinaryJSONField
from uform import UForm

db = PostgresqlExtDatabase('dogs', user='dwatson')


class Dog(UForm):
    pass

    @classmethod
    def get(cls):
        pass

    class Meta:
        database = db

Dog.drop_table(fail_silently=True)
Dog.create_table(fail_silently=True)

if __name__ == '__main__':
    for d in [{'name': 'Keiko', 'age': 7},
              {'name': 'Goose', 'age': 13},
              {'name': 'Maxwell', 'age': 11}]:
        Dog.store(**d)
