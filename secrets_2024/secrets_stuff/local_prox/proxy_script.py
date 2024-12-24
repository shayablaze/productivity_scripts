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
            secrets_list = ['really', 'sit']
            flow.request.content = self.replace_secrets_with_stars([flow.request.content], secrets_list)[0]
            print('i finished the switch part')
            # body = json.loads(flow.request.content)
            # print("Request Body:", body['name'])
            # body['name'] = 'bemabe'
            # flow.request.content = json.dumps(body).encode('utf-8')
            print(json.loads(flow.request.content))
        except Exception as e:
            print(f"i got exception {str(e)}")
    def replace_secrets_with_stars(self, byte_list, secrets_list):
        """
        Replaces occurrences of secret strings in a list of bytes with '****'.

        Args:
            byte_list (list of bytes): The list of bytes to process.
            secrets (list of str): The list of secrets to replace.

        Returns:
            list of bytes: A new list of bytes with the secrets replaced by '****'.
        """
    # Convert secrets to bytes
        secrets_bytes = [secret.encode('utf-8') for secret in secrets_list]

        # Process each byte entry
        result = []
        for byte_entry in byte_list:
            for secret_bytes in secrets_bytes:
                byte_entry = byte_entry.replace(secret_bytes, b'metal_rules')
            result.append(byte_entry)

        return result

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