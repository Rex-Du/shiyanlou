"""
app:
"""
# author: rexdu
# create: 2020/6/28 22:23

import datetime
import flask
import redis

app = flask.Flask('shiyanlou-sse-chat')
app.secret_key = 'shiyanlou'
app.config['DEBUG'] = True
r = redis.StrictRedis()


@app.route('/')
def home():
    if 'user' not in flask.session:
        return flask.redirect('/login')
    user = flask.session['user']
    return flask.render_template('home.html', user=user)


def event_stream():
    pubsub = r.pubsub()
    # 使用发布订阅系统的 subscribe 方法订阅某个频道
    pubsub.subscribe('chat')
    for message in pubsub.listen():
        data = message['data']
        if type(data) == bytes:
            yield f'data: {data.decode()}\n\n'


@app.route('/login', methods=['GET', 'POST'])
def login():
    if flask.request.method == 'POST':
        flask.session['user'] = flask.request.form['user']
        return flask.redirect('/')
    return ('<form action="" method="post">User Name: <input name="user"> '
            '<input type="submit" value="login" /></form>')


@app.route('/post', methods=['POST'])
def post():
    message = flask.request.form['message']
    user = flask.session.get('user', 'anonymous')
    now = datetime.datetime.now().replace(microsecond=0).time()
    r.publish('chat', f'[{now.isoformat()}] {user}: {message}\n')
    return flask.Response(status=204)


@app.route('/stream')
def stream():
    return flask.Response(event_stream(), mimetype='text/event-stream')


if __name__ == '__main__':
    app.run()