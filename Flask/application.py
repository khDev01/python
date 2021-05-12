from flask import Flask, render_template, request
import sqlite3
import sys

app = Flask(__name__)

@app.route('/')
def index():
   return render_template("index.html", name=request.args.get("name", "secondArg_default value"))

# dynamic url
@app.route('/lesson/<lessonNumber>')
def lesson(lessonNumber):
    TheNumber = lessonNumber
    rows = None
    # data = None
    # print(__name__, fle=sys.stderr)

    def create_connection(db_file):
        conn = None
        try:
            conn = sqlite3.connect(db_file)
        except Error as e:
            print(e)
        return conn

    def select_all_lesson(conn):
        cur = conn.cursor()
        searchString = "SELECT * FROM BOOK1 WHERE Lesson={}".format(TheNumber)
        cur.execute(searchString)
        rows = cur.fetchall()
        for row in rows:
            print(row, file=sys.stderr)
        return rows

    def main():
        database = "MedinaArabic1.db"
        # create a database connection
        conn = create_connection(database)
        with conn:
            print("Lesson {}".format(TheNumber), file=sys.stderr)
            global data
            data = select_all_lesson(conn)
        # print(data, file=sys.stderr)
    if __name__ == 'application':
        main()

    return render_template("lesson.html" , lessonNumber=lessonNumber, data=data)




















# request.args = GET
#  request.form = POST

# if __name__ == '__main__':
#    app.run()
