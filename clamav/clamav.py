#!/usr/bin/env python3

#   Copyright 2014-2018 PUNCH Cyber Analytics Group
#
#   Licensed under the Apache License, Version 2.0 (the "License");
#   you may not use this file except in compliance with the License.
#   You may obtain a copy of the License at
#
#       http://www.apache.org/licenses/LICENSE-2.0
#
#   Unless required by applicable law or agreed to in writing, software
#   distributed under the License is distributed on an "AS IS" BASIS,
#   WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
#   See the License for the specific language governing permissions and
#   limitations under the License.
"""
Overview
========

Scan attachments with ClamAV

"""

import clamd
from configparser import ConfigParser
from typing import List, Dict, Optional

from stoq.plugins import WorkerPlugin
from stoq import Payload, RequestMeta, WorkerResponse, ExtractedPayload, PayloadMeta

CLASS_ATTRIBUTES = [
    'hashpayload', 'saveresults', 'daemon', 'interval', 'timeout', 'host', 'port', 'socket'
]

class SMTPPlugin(WorkerPlugin):
    def __init__(self, config: ConfigParser, plugin_opts: Optional[Dict]) -> None:
        super().__init__(config, plugin_opts)

        self.hashpayload: bool = False
        self.saveresults: bool = True
        self.daemon: str = 'socket'
        self.interval: int = 60
        self.timeout: int = 10
        self.host: str = '127.0.0.1'
        self.port: int = 3310
        self.socket: str = '/var/run/clamav/clamd.ctl'

        for name in CLASS_ATTRIBUTES:
            self._parse_option(plugin_opts, name)

    def _parse_option(self, plugin_opts, name):
        if plugin_opts and name in plugin_opts:
            self[name] = plugin_opts[name]
        elif config.has_option('options', name):
            self[name] = config.getboolean('options', name)

    def scan(self, payload: Payload, request_meta: RequestMeta) -> WorkerResponse:
        message_json = '{"TEST":"TEST"}'
        return WorkerResponse(message_json, errors=None, extracted=None)
