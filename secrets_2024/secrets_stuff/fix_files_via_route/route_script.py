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
position_map = {}
def censor_strings_in_file(position_map, strings_to_censor, file_name):
    try:
        with open(file_name, 'r+') as file:
            # Move to the last processed position
            file.seek(0, 2)  # Move to the end of the file to capture its size
            file_size = file.tell()
            print(f'current file size is {file_size}')
            if not file_name in position_map:
                position_map[file_name] = 0
            last_position = position_map[file_name]
            # Check if there's new content
            if file_size > last_position:
                file.seek(last_position)  # Move to the last processed position
                new_content = file.read()
                print('here is the new content')
                print('')
                print(new_content)
                print('')
                print('end of new content')
                # Replace each string in the list with ***********
                for string in strings_to_censor:
                    # new_content = new_content.replace(string, 'goodword123')
                    new_content = new_content.replace(string, '***********')

                # Write the updated new content back to the file
                file.seek(last_position)
                file.write(new_content)
                file.truncate()

                # Update the last position to the current end of the file
                last_position = file_size
                print('the updated content is ')
                print(new_content)
                print(f'now i will sleep for no reason before upload and last_position is {last_position}')
                print(f"Processed new content up to position {last_position}.")
                position_map[file_name] = last_position
            else:
                print("No new content to process.")

    except FileNotFoundError:
        print(f"Error: The file '{file_name}' does not exist.")
    except Exception as e:
        print(f"An error occurred: {e}")
    return last_position



@app.route('/do-this', methods=['POST'])
def do_this():
    global position_map
    print(f"Hiiiiiii!!!!!! and here is counter {position_map}")
    strings = ["badword", "Badword"]
    print('do i get here i wait for you')
    file_path = request.args.get('file_path')
    print(f'i got this file path right here {file_path}')
    last_position = censor_strings_in_file(position_map, strings, file_path)
    print(f'last position is {last_position}' )


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