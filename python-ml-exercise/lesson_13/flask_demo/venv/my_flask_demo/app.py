from flask import Flask
app = Flask(__name__)

@app.route('/haha')
def hello_world():
    return 'helloworldSSSSSS'

# if __name__ == '__main__':
#     #app.run()
#     app.run(host='0.0.0.0', debug=True, port=8080)

#通过配置文件载入
app.config.from_object('config')
app.run(host='127.0.0.1', debug=app.config['DEBUG'], port=5001)