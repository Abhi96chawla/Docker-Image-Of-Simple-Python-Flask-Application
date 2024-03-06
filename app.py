from flask import Flask
from flask import render_template
app = Flask(__name__)

@app.route('/')
def index():
  message = "Hello, World"
  return render_template('index.html', message=message)

app.run(host='0.0.0.0', port=8000)

if __name__ == "__main__": 
    app.run(debug=True)
