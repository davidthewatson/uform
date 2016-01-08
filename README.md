# UForm

This is a novel implementation of the U-form abstract data type using PostgreSQL's JSONB Binary JSON field for attribute storage.

This short implementation is merely a Proof of Concept. It does not attempt to be feature complete, scalable, or attain perfection. However, it does provide a working implementation that may achieve some features associated with models such as Entity Attribute (EAV) or Datomic's 5 tuple.

There is considerable history to the development of the UForm going back to MIT's Michael Dertouzos and his E-form, which inspired the U-form work at MAYA Design. Full disclosure: I was an employee at MAYA Design.

See [wikipedia](https://en.wikipedia.org/wiki/U-form) for more information on the U-form.

The code provided here is based on [PeeWee](https://peewee.readthedocs.org/en/latest/) to establish the PostgreSQL connection, models, and attributes. This simplifies the code dramatically.

## Installation and Configuration

0. Install the python requirements:

        pip install -r requirements.txt
0. Replace user variable with your postgres user in dog.py:

        db = PostgresqlExtDatabase('dogs', user='dwatson')
0. Create the database:

        createdb dogs
0. Enable the HSTORE extension:

        \c dogs
        create extension hstore;
0. Run the script:

        python dog.py
0. Examine the database:

        SELECT * FROM dog;
        "id","uuid","attrs"
        1,"012E201B-83BF-45E0-AD92-7EA9FC768464","{\"age\": 7, \"name\": \"Keiko\"}"
        2,"3590BD6B-F2BB-406A-8E93-80EE17AFF13A","{\"age\": 13, \"name\": \"Goose\"}"
        3,"85D3E0A7-7C8F-4B67-94E7-E0568A2D8ED3","{\"age\": 11, \"name\": \"Maxwell\"}"
0. Examine the attributes of a particular dog:

        SELECT * FROM dog WHERE attrs->>'name' = 'Keiko';
        "id","uuid","attrs"
        1,"012E201B-83BF-45E0-AD92-7EA9FC768464","{\"age\": 7, \"name\": \"Keiko\"}"

## Further Exploration

More advanced queries are left as an exercise for the reader. Suffice it so say that the full-power of PostgreSQL is available and that query results on attributes are extremely fast provided that you create GIN indexes.

It's pretty trivial to create REST interfaces for these models using [PostgREST](http://postgrest.com/). PostgREST even enables querying the JSONB attributes through HTTP query parameters.
