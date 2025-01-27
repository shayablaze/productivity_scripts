"""Redirect HTTP requests to another server."""
import logging
import asyncio
import sys
from mitmproxy import options
from mitmproxy.tools import dump
logging.getLogger('boto3').setLevel(logging.INFO)
logging.getLogger('botocore').setLevel(logging.INFO)
logging.getLogger('s3transfer').setLevel(logging.INFO)
logging.info('2 cellos starting the proxy stam ')
with open("2cellos.txt", "w") as file:
    # Write the desired text to the file
    file.write("in 2 cellos for proxy stam\n ")