#!/usr/bin/env python

# copyright (c) 2016 Intel, Inc.
#
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

import os
import sys
from oslo_log import log as logging
from oslo_service import wsgi
from zilong.api import app
from zilong.conf import CONF
from zilong.common import rpc
from zilong import version

LOG = logging.getLogger(__name__)


def main():
    CONF(sys.argv[1:], project='zilong',
         version=version.version_string())

    logdir = CONF.log_dir
    if logdir:
        is_exists = os.path.exists(logdir)
        if not is_exists:
            os.makedirs(logdir)

    logging.setup(CONF, "zilong")
    LOG.info("Logging enabled!")
    LOG.debug("command line: %s", " ".join(sys.argv))

    rpc.init(CONF)
    application = app.setup_app()
    host = CONF.api.bind_host
    port = CONF.api.bind_port
    workers = CONF.api.api_workers

    LOG.info("Server on http://%(host)s:%(port)s with %(workers)s",
             {'host': host, 'port': port, 'workers': workers})

    service = wsgi.Server(CONF, "zilong", application, host, port)

    app.serve(service, CONF, workers)

    LOG.info("Configuration:")
    app.wait()


if __name__ == '__main__':
    main()
