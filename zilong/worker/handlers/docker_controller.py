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

import json
from oslo_log import log as logging
from zilong.common.docker import api as docker_api
import requests

LOG = logging.getLogger(__name__)


class Handler(object):
    """Valence Node RPC handler.

    These are the backend operations. They are executed by the backend ervice.
    API calls via AMQP (within the ReST API) trigger the handlers to be called.

    """

    def __init__(self):
        super(Handler, self).__init__()

    # Docker Operations
    def list_containers(self, context):
        LOG.debug("RPC: list_containers")
        containers = docker_api.get_containers()
        return containers

    def get_container_details(self, context, container_id):
        LOG.debug("RPC: get_container_details for %s", container_id)
        container = docker_api.get_container_details(container_id)
        return container

    def list_images(self, context):
        LOG.debug("RPC: list_images")
        images = docker_api.get_images()
        return images

    def get_image_details(self, context, image_id):
        LOG.debug("RPC: get_image_details for %s", image_id)
        image = docker_api.get_image_details(image_id)
        return image

    def get_system_info(self, context):
        LOG.debug("RPC: get_system_info")
        info = docker_api.get_system_info()
        return info
