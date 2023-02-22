from flask import Flask
import datetime

app = Flask(__name__)

@app.route('/')
def today_date():
    today = datetime.date.today()
    return f"Hello, Today's date is {today}. How are you?"

@app.route('/app')
def hoge_world():
    return 'Hello!! App'

if __name__ == '__main__':
    app.run(debug=True)