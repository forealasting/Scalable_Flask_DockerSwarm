from flask import Flask, request, current_app, g
import time
import datetime

app = Flask(__name__)


def fib(n):
    if n == 0:
        return 0
    elif n == 1:
        return 1
    fib_prev = 0
    fib_curr = 1
    for i in range(2, n + 1):
        fib_next = fib_prev + fib_curr
        fib_prev = fib_curr
        fib_curr = fib_next

    return fib_curr

def fib_recursive(n):
    if n == 0:
        return 0
    elif n == 1:
        return 1
    else:
        return fib_recursive(n - 1) + fib_recursive(n - 2)

# Before each request
@app.before_request
def before_request():
    g.start_time = time.time()


# After request handler
@app.after_request

def after_request(response):
    t = time.time() - g.start_time
    current_app.logger.debug(f"Time used: {time.time() - g.start_time}")

    path = 'output.txt'
    f = open(path, 'a')
    data = str(t) + '\n'
    f.write(data)
    f.close()

    return response

@app.route('/ping', methods=['GET', 'POST'])
def ping():
    if request.method == 'POST':
        # just calculate
        # 0 1 1 2 3 5...
        ans = fib(0)
        # print(ans)
        return 'Datetime:' + str(datetime.datetime.now()) + 'Post Request and Get answer: ' + str(ans)

    else:
        ans = fib(5)
        # print(ans)
        return 'Datetime:' + str(datetime.datetime.now()) + 'Get Request and Get answer: ' + str(ans)

if __name__ == '__main__':
    app.run('0.0.0.0', port=4567, debug=True, threaded=True)  # debug : Can Auto-Reload & error trace


                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                            