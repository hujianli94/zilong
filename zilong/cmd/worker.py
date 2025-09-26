#!/usr/bin/env python

# Copyright (c) 2016 Intel, Inc.
#
#    Licensed under the Apache License, Version 2.0 (the "License"); you may
#    not use this file except in compliance with the License. You may obtain
#    a copy of the License at
#
#         http://www.apache.org/licenses/LICENSE-2.0
#
#    Unless required by applicable law or agreed to in writing, software
#    distributed under the License is distributed on an "AS IS" BASIS, WITHOUT
#    WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied. See the
#    License for the specific language governing permissions and limitations
#    under the License.

"""Starter script for the zilong worker service."""

import os
from oslo_log import log as logging
from oslo_service import service
from zilong.common import rpc_service
from zilong.conf import CONF
from zilong.worker.handlers import docker_controller
from zilong import version
import sys
import uuid

LOG = logging.getLogger(__name__)


def main():
    CONF(sys.argv[1:], project='zilong',
         version=version.version_string())

    logdir = CONF.log_dir
    if logdir:
        is_exists = os.path.exists(logdir)
        if not is_exists:
            os.makedirs(logdir)
    logging.setup(CONF, 'zilong-worker')
    LOG.info("Logging enabled!")
    LOG.debug("command line: %s", " ".join(sys.argv))
    if CONF.debug:
        logging.getLogger('oslo_messaging').setLevel(logging.DEBUG)
        logging.getLogger('zilong').setLevel(logging.DEBUG)
    LOG.info(('Starting zilong-worker in PID %s'), os.getpid())
    LOG.debug("Configuration:")

    worker_id = uuid.uuid4()
    endpoints = [
        # node_controller.Handler(),
        docker_controller.Handler()
    ]

    server = rpc_service.Service.create(CONF.worker.topic,
                                        worker_id, endpoints,
                                        binary='zilong-worker')
    launcher = service.launch(CONF, server)
    launcher.wait()


if __name__ == '__main__':
    main()
