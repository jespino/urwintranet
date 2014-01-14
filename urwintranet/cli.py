# -*- coding: utf-8 -*-

"""
urwintranet.cli
~~~~~~~~~~~~~
"""

from urwintranet.api.client import IntranetClient
from urwintranet.core import IntranetCore
from urwintranet.config import Configuration, DEFAULTS
from urwintranet.executor import Executor


def main():
    config = Configuration()
    config.load()
    client = IntranetClient(config.host)
    if config.auth_token:
        client.set_auth_token(config.auth_token)
    executor = Executor(client)
    program = IntranetCore(executor, config, authenticated=config.auth_token)
    program.run()
