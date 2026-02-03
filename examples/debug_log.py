#!/usr/bin/env python3

import logging
import os

from jmaplib import Client
from jmaplib.logging import log
from jmaplib.methods import CoreEcho

# Create basic console logger
logging.basicConfig()

# Set jmaplib log level to DEBUG
log.setLevel(logging.DEBUG)

# Create and configure client
client = Client.create_with_api_token(
    host=os.environ["JMAP_HOST"], api_token=os.environ["JMAP_API_TOKEN"]
)

# Call JMAP API method
# The request and response JSON content will be logged to the console
client.request(CoreEcho(data=dict(hello="world")))

# Example output:
#
# DEBUG:jmaplib:Sending JMAP request {"using": ["urn:ietf:params:jmap:core"], "methodCalls": [["Core/echo", {"hello": "world"}, "single.Core/echo"]]}    # noqa: E501
# DEBUG:jmaplib:Received JMAP response {"methodResponses":[["Core/echo",{"hello":"world"},"single.Core/echo"]]}                                          # noqa: E501
