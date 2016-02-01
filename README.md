# UForm

This is a novel implementation of the U-form abstract data type using PostgreSQL's JSONB Binary JSON field for attribute storage. 

The inspiration for the U-fom goes back to Michael Dertouzos [book](https://en.wikipedia.org/wiki/U-form#cite_note-1) which introduced the E-form. I did not invent the U-Form. I did work at MAYA Design where the U-Form was created. 

My hope is to keep the idea alive in Open Source Software. While there are many similar models now such as Entity-Attribute-Value (EAV) or Datomic's 5-tuple, few of these existed when the U-Form was created. 

See [wikipedia](https://en.wikipedia.org/wiki/U-form) for more information on the U-form.

The code provided here is based on [PeeWee](https://peewee.readthedocs.org/en/latest/) to establish the PostgreSQL connection, models, and attributes. This simplifies the code dramatically.

## Installation and Configuration

0. Clone the repository:

        https://github.com/davidthewatson/uform.git
0. Change directories:

        cd uform
0. Make a virtualenv:

        mkvirtualenv uform
0. Install the python requirements:

        pip install -r requirements.txt
0. Replace user variable with your postgres user in uform.py:

        db = PostgresqlExtDatabase(name, user='dwatson')
0. Run the script:

        python example.py
0. Examine the database:

        SELECT * FROM cats;
        "id","uuid","attrs"
        1,"012E201B-83BF-45E0-AD92-7EA9FC768464","{\"age\": 7, \"name\": \"Keiko\"}"
        2,"3590BD6B-F2BB-406A-8E93-80EE17AFF13A","{\"age\": 13, \"name\": \"Goose\"}"
        3,"85D3E0A7-7C8F-4B67-94E7-E0568A2D8ED3","{\"age\": 11, \"name\": \"Maxwell\"}"
0. Examine the attributes of a particular cat:

        SELECT * FROM cats WHERE attrs->>'name' = 'Keiko';
        "id","uuid","attrs"
        1,"012E201B-83BF-45E0-AD92-7EA9FC768464","{\"age\": 7, \"name\": \"Keiko\"}"

## Further Exploration

More advanced queries are left as an exercise for the reader. Suffice it so say that the full power of PostgreSQL is available and that query results on attributes are extremely fast provided that you create GIN indexes.

It's trivial to create REST interfaces for these models using [PostgREST](http://postgrest.com/). PostgREST even enables querying the JSONB attributes through HTTP query parameters.
