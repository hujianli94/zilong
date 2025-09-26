# Copyright 2017 Huawei Technologies Co.,LTD.
# All Rights Reserved.
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
import os
import socket
from oslo_config import cfg
from oslo_log import log as logging
from zilong.common.i18n import _

opts = [
    cfg.StrOpt('auth_strategy', default='noauth',
               help=(_("The type of authentication to use"))),
    cfg.BoolOpt('allow_pagination', default=False,
                help=(_("Allow the usage of the pagination"))),
    cfg.BoolOpt('allow_sorting', default=False,
                help=(_("Allow the usage of the sorting"))),
    cfg.StrOpt('pagination_max_limit', default="-1",
               help=(_("The maximum number of items returned in a single "
                       "response, value was 'infinite' or negative integer "
                       "means no limit")))
]

service_opts = [
    cfg.HostAddressOpt('host',
                       default=socket.getfqdn(),
                       sample_default='localhost',
                       help=_('Name of this node. This can be an opaque '
                              'identifier. It is not necessarily a hostname, '
                              'FQDN, or IP address. However, the node name '
                              'must be valid within an AMQP key, and if using '
                              'ZeroMQ, a valid hostname, FQDN, or IP address.')
                       ),
    cfg.IntOpt('periodic_interval',
               default=60,
               help=_('Default interval (in seconds) for running periodic '
                      'tasks.')),
    cfg.IntOpt('periodic_interval_max',
               default=60,
               help='Max interval size between periodic tasks execution in '
                    'seconds.'),
]

path_opts = [
    cfg.StrOpt('pybasedir',
               default=os.path.abspath(
                   os.path.join(os.path.dirname(__file__), '../')),
               sample_default='/usr/lib/python/site-packages/zilong/zilong',
               help=_('Directory where the kongming python module is '
                      'installed.')),
    cfg.StrOpt('bindir',
               default='$pybasedir/bin',
               help=_('Directory where zilong binaries are installed.')),
    cfg.StrOpt('state_path',
               default='$pybasedir',
               help=_("Top-level directory for maintaining zilong's state.")),
]


def register_opts(conf):
    logging.register_options(conf)
    conf.register_opts(opts)
    conf.register_opts(service_opts)
    conf.register_opts(path_opts)
