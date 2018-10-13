from flask import Flask
app = Flask(__name__)

@app.route('/hugo')
def hugo():
    return 'hugo'

@app.route('/user/<username>')
def user(username):
    return username

if __name__ == '__main__':
      app.run(host='0.0.0.0', port=8080)