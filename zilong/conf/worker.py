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

WORKER_OPTS = [
    cfg.StrOpt('topic',
               default='zilong-worker',
               help='The queue to add zilong worker tasks to.')
]

OS_INTERFACE_OPTS = [
    cfg.StrOpt('os_admin_url',
               help='Admin URL of Openstack'),
    cfg.StrOpt('os_tenant',
               default='admin',
               help='Tenant for Openstack'),
    cfg.StrOpt('os_user',
               default='admin',
               help='User for openstack'),
    cfg.StrOpt('os_password',
               default='addmin',
               help='Password for openstack')
]

worker_conf_group = cfg.OptGroup(name='worker',
                                 title='Zilong worker options')

os_conf_group = cfg.OptGroup(name='undercloud',
                             title='Zilong Openstack interface options')


def register_opts(conf):
    conf.register_group(worker_conf_group)
    conf.register_opts(WORKER_OPTS, group=worker_conf_group)

    conf.register_group(os_conf_group)
    conf.register_opts(OS_INTERFACE_OPTS, group=os_conf_group)


def list_opts():
    return {
        worker_conf_group: WORKER_OPTS,
        os_conf_group: OS_INTERFACE_OPTS
    }
