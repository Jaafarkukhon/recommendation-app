from flask import Flask, render_template, request
import sqlite3

app = Flask(__name__)

def create_database():
    conn = sqlite3.connect('recommendations.db')
    cursor = conn.cursor()
    cursor.execute('''CREATE TABLE IF NOT EXISTS items (id INTEGER PRIMARY KEY AUTOINCREMENT, keyword TEXT NOT NULL, recommendation TEXT NOT NULL)''')
    cursor.execute("SELECT COUNT(*) FROM items")
    count = cursor.fetchone()[0]
    if count == 0:
        data = [("hot","Summer ☀️"),("cold","Winter ❄️"),("rain","Autumn 🍂"),("flower","Spring 🌸"),("hungry","Pizza 🍕"),("tired","Sleep 😴"),("happy","Party 🎉"),("sad","Ice Cream 🍦"),("bored","Gaming 🎮"),("cozy","Hot Chocolate ☕"),("sweet","Chocolate 🍫"),("lazy","Netflix 📺")]
        cursor.executemany("INSERT INTO items (keyword, recommendation) VALUES (?, ?)", data)
    conn.commit()
    conn.close()

@app.route('/', methods=['GET', 'POST'])
def index():
    result = None
    user_input = ''
    not_found = False
    if request.method == 'POST':
        user_input = request.form.get('user_input', '').strip().lower()
        if user_input:
            conn = sqlite3.connect('recommendations.db')
            cursor = conn.cursor()
            cursor.execute("SELECT recommendation FROM items WHERE keyword LIKE ?", ('%' + user_input + '%',))
            row = cursor.fetchone()
            conn.close()
            if row:
                result = row[0]
            else:
                not_found = True
    return render_template('index.html', result=result, user_input=user_input, not_found=not_found)

if __name__ == '__main__':
    create_database()
    app.run(host='0.0.0.0', port=5000, debug=True)
