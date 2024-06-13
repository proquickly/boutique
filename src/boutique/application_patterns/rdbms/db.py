import sqlite3

sql_statements = (
    "drop table if exists test",
    "create table test (id, name)",
    "insert into test values (1, 'abc')",
    "insert into test values (2, 'def')",
    "insert into test values (3, 'xyz')",
    "select id, name from test",
)


def main():
    with sqlite3.connect("data/dbms.db") as conn:
        c = conn.cursor()
        [c.execute(statement) for statement in sql_statements]
        conn.commit()
        rows = c.fetchall()
        print(rows)
        c.close()


if __name__ == "__main__":
    main()
