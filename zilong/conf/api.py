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

from oslo_config import cfg
from zilong.common.i18n import _

opts = [
    cfg.StrOpt('bind_host', default='0.0.0.0',
               help=(_("The host IP to bind to"))),
    cfg.IntOpt('bind_port', default=8181,
               help=(_("The port to bind to"))),
    cfg.IntOpt('api_workers', default=2,
               help=(_("number of api workers"))),
    cfg.BoolOpt('debug', default=False,
                help=(_("Enable debug mode"))),
]

opt_group = cfg.OptGroup(name='api',
                         title='Options for the zilong-api service')


def register_opts(conf):
    conf.register_group(opt_group)
    conf.register_opts(opts, group=opt_group)


def list_opts():
    return {
        opt_group: opts
    }
