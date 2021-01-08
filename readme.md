<h1 align="center">
    POSTGRES EASY TALK
</h1>

## Introduction

Postgres easy talk is an user-friendly query tool that provides an easier communication system in automated dabatabase interaction.

I propose a new query system for postgres which allow to use it easily on automated processes.

## What's in the box!

- Multiple database query
    - work simultaneously with multiple database and make them interact together!
- Static 'read-only-onces' code
    - Your next collegue can look at your 7 months ago database creation code and understand quickly how it is built.
- User-entry checkpoint control
    - Find out bugs from the source and relax. Entries are ckeched and futures bugs are prevented. The tool will not allow an entry as easy as a direct basic database query.

## Postgresql query tools

- CREATE
- INSERT
- SELECT
- DELETE
- ... in progress!

## INSTALL AND IMPORT

The version will be soon available on Pypi
```bash
python3 -m pip install easytalk
```

Then, to use the package on your project:
```python
import easytalk                 -> easytable.Table('table')
or
from easytalk import *          -> Table('table')
```

## INPUT / OUTPUT EXAMPLE

### CREATE example

* Input

```python
table = Table('articles_table')

table.add_serialField()             # automatic 'id' increment (primary key)
table.add_datetimeField()           # automatic 'created_at'
table.add_varcharField('name')      
table.add_intField('price')         # each add_ have optional attr, such as NOT NULL (by default on True)
table.add_booleanField('to_buy')

table.write_TABLE()
```

* Output

![table_CREATE](/images/table_CREATE.png)

### INSERT example

* Input

```python
i = Insert(table)

entry = {
    'name': 'item3',
    'price': 345,
    'datetime': datetime.datetime.now(),
    'to_buy': False,
}
i.write_ENTRY(entry)
```

* Output

![table_INSERT](/images/table_INSERT.png)

### READ example

* Input

```python
r = Read(table)

answer = r.find_filter()
for row in answer:
    print(row)
```

* Output

![table_SELECT](/images/table_SELECT.png)


## Contributing
Pull requests are welcome. For major changes, please open an issue first to discuss what you would like to change.

To contribute to GermanOK, follow these steps:

1. Fork this repository.
2. Create a branch: `git checkout -b <branch_name>`.
3. Make your changes and commit them: `git commit -m '<commit_message>'`
4. Push to the original branch: `git push origin <project_name>/<location>`
5. Create the pull request.

Alternatively see the GitHub documentation on [creating a pull request](https://help.github.com/en/github/collaborating-with-issues-and-pull-requests/creating-a-pull-request).

## Contact

If you want to contact me, you can reach me at romain.ledru2@gmail.com
