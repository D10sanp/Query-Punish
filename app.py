from flask import Flask, render_template, request
import sqlite3

app = Flask(__name__)

DATABASE = "database.db"

def run_query(query):
    conn = sqlite3.connect(DATABASE)
    cursor = conn.cursor()
    try:
        cursor.execute(query)
        results = cursor.fetchall()
        conn.close()
        if not query.strip().lower().startswith("select"):
            return None, "Only SELECT queries are allowed."

    except Exception as e:
        conn.close()
        return None, str(e)

@app.route("/")
def index():
    return render_template("index.html")

@app.route("/case1", methods=["GET", "POST"])
def case1():
    result = None
    error = None
    success = False

    if request.method == "POST":
        user_query = request.form["query"]

        result, error = run_query(user_query)

        # Expected answer
        if result == [("Liam O’Connor",)]:
            success = True

    return render_template("case.html", result=result, error=error, success=success)

if __name__ == "__main__":
    app.run(debug=True)
