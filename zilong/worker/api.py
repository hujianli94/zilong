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

"""controller API for interfacing with Other modules"""
from oslo_log import log as logging
from zilong.common import rpc_service
from zilong.conf import CONF

# The Backend API class serves as a AMQP client for communicating
# on a topic exchange specific to the workers.  This allows the ReST
# API to trigger operations on the workers.

LOG = logging.getLogger(__name__)


class API(rpc_service.API):
    def __init__(self, transport=None, context=None, topic=None):
        topic = topic or CONF.worker.topic
        super(API, self).__init__(transport, context,
                                  topic=topic)

    # Docker Operations
    def list_containers(self):
        return self._call('list_containers')

    def get_container_details(self, container_id):
        return self._call('get_container_details', container_id=container_id)

    def list_images(self):
        return self._call('list_images')

    def get_image_details(self, image_id):
        return self._call('get_image_details', image_id=image_id)

    def get_system_info(self):
        return self._call('get_system_info')
