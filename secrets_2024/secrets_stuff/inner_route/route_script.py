from flask import Flask
import threading
import time
import requests

# Flask app to handle incoming requests
app = Flask(__name__)

@app.route('/do-this', methods=['GET'])
def do_this():
    print("Hiiiiiii!!!!!!")
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
        time.sleep(20)

if __name__ == "__main__":
    # Start the Flask app in a separate thread
    flask_thread = threading.Thread(target=run_flask, daemon=True)
    flask_thread.start()

    # Start the periodic caller
    periodic_caller()