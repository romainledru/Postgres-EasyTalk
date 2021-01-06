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

## Postgresql query tools (in progress)

- CREATE
- INSERT
- SELECT

## INPUT / OUTPUT EXAMPLE

### CREATE example

* Input

```python
myTable = Table("table1")
pattern = {
    'primary': False,
    'length': 58,
    'compulsory': False,
}
myTable.add_varcharField("StrEntry1", pattern)
myTable.add_booleanField("BooleanEntry1")
myTable.add_intField("IntEntry1")
myTable.add_floatField("FloatEntry1")
myTable.write_TABLE()
```

* Output

```python
CREATE TABLE table1 (StrEntry1 VARCHAR(58), BooleanEntry1 BOOLEAN, IntEntry1 INT, FloatEntry1 REAL, id INT);
```

### INSERT example

* Input

```python
insertQuery = Insert(myTable)
entry = {
    'StrEntry1': 'hello',
    'BooleanEntry1': True,
    'IntEntry1': 45,
    'FloatEntry1': 35.65,
}
insertQuery.write_ENTRY(entry)
```

* Output

```python
INSERT INTO table1 (StrEntry1, BooleanEntry1, IntEntry1, FloatEntry1) VALUES (hello, True, 45, 35.65);
```

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
