import os
import pytest
import sqlite3


@pytest.fixture()
def keep_db():
    return False


@pytest.fixture()
def session(keep_db):
    filename = 'tests/data/test.db'
    try:
        os.remove(filename)
    except FileNotFoundError:
        pass
    connection = sqlite3.connect(filename)
    db_session = connection.cursor()
    db_session.execute('''create table tt (id char)''')
    for idnum in range(10):
        db_session.execute(f'''INSERT INTO tt VALUES ("{idnum}")''')
    connection.commit()

    yield db_session

    connection.close()
    if not keep_db:
        os.remove(filename)


def test_select(session):
    session.execute("select * from tt")
    results = [int(item[0]) for item in session.fetchall()]
    assert results == list(range(10))
