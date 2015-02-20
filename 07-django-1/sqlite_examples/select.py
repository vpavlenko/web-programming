import sqlite3


con = sqlite3.connect('../testingplatform/db.sqlite3')


def print_query_results(query):
    print(query)
    cur = con.cursor()
    cur.execute(query)

    rows = cur.fetchall()

    for row in rows:
        print('\t', row)


print_query_results("SELECT * FROM lessons_lesson")
print_query_results("SELECT * FROM lessons_submission WHERE problem_id = 1")
