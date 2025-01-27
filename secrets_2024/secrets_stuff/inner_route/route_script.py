from flask import Flask
import threading
import time
import requests
import asyncio
from mitmproxy import options
from mitmproxy.tools import dump
# Flask app to handle incoming requests
app = Flask(__name__)
from flask import request
counter = 1
@app.route('/do-this', methods=['POST'])
def do_this():
    global counter
    file_path = request.args.get('file_path')
    print(f'i got this file path {file_path}')
    counter += 1
    print(f"Hiiiiiii!!!!!! and here is counter {counter}")
    return "OK", 200

def run_flask():
    app.run(host='0.0.0.0', port=5555)

def periodic_caller():
    while True:
        try:
            response = requests.get('http://localhost:5555/do-this')
            print(f"Called yyyyy /do-this: {response.status_code}")
        except Exception as e:
            print(f"Error calling /do-this: {e}")
        time.sleep(200)

class RequestLogger:
    def request(self, flow):
        print('whats up i am here finally')
        # host = flow.request.headers['host']
        print(flow.request)
        print(flow.request.headers['Host'])

async def start_proxy(host, port):
    opts = options.Options(listen_host=host, listen_port=port)

    master = dump.DumpMaster(
        opts,
        with_termlog=False,
        with_dumper=False,
    )
    master.addons.add(RequestLogger())

    await master.run()
    return master

if __name__ == "__main__":

    flask_thread = threading.Thread(target=run_flask, daemon=True)
    flask_thread.start()
    print('zzz starting the proxy')
    asyncio.run(start_proxy('127.0.0.1', 4444))
    print('after starting the server')


    # Start the Flask app in a separate thread


    # Start the periodic caller
    # periodic_caller()