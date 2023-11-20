from mypackage.utils import printStackTrace
import psycopg2

def test_printStackTrace():
    conn_postgresql = None
    try:
        conn_postgresql = psycopg2.connect(database="abc123", user="abc123", password="abc123", host="127.0.0.1",
                                           port="5432")
        print("Database opened successfully")

        cur = conn_postgresql.cursor()
        cur.execute("SELECT fname || ' ' || lname as StudentName, cid as ClassId from students")
        rows = cur.fetchall()

        for row in rows:
            print("StudentName =", row[0])
            print("ClassId =", row[1], "\n")

    except Exception:
        '''
        Printing stack trace
        '''
        original_error_msg = """--------------------------------------------------------------------------------
Error connecting postgres database:
--------------------------------------------------------------------------------
Traceback (most recent call last):
  File "pkg_example_project/tests/test_utils.py", line 7, in test_printStackTrace
    conn_postgresql = psycopg2.connect(database="abc123", user="abc123", password="abc123", host="127.0.0.1",
                      ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
  File "pkg_example_project/venv/lib/python3.11/site-packages/psycopg2/__init__.py", line 122, in connect
    conn = _connect(dsn, connection_factory=connection_factory, **kwasync)
           ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
psycopg2.OperationalError: connection to server at "127.0.0.1", port 5432 failed: Connection refused
	Is the server running on that host and accepting TCP/IP connections?

--------------------------------------------------------------------------------"""

        actual_message = printStackTrace('Error connecting postgres database')
        actual_message_neuter = actual_message.replace('/Users/paramraghavan/dev/github/', '')
        if conn_postgresql:
            conn_postgresql.close()
        assert(original_error_msg == actual_message_neuter)

