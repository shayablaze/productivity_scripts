"""Redirect HTTP requests to another server."""

import asyncio
import sys
from mitmproxy import options
from mitmproxy.tools import dump
# https://a.blazemeter.com/app/#/accounts/1376201/workspaces/1419699/projects/1679992/tests/14524348
class RequestLogger:
    def request(self, flow):
        print('whats up i am here finally')
        print(flow.request)
        try:
            import json
            body = json.loads(flow.request.content)
            print("Request Body:", body['name'])
            body['name'] = 'nachon at yodaat'
            flow.request.content = json.dumps(body).encode('utf-8')
        except json.JSONDecodeError:
            print("The body is not JSON")

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
print('starting the proxy')
asyncio.run(start_proxy('127.0.0.1', 4444))