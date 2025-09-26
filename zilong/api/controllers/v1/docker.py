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

from oslo_config import cfg
from oslo_log import log as logging
import pecan
from pecan import expose
from pecan import request
from pecan import response
from pecan.rest import RestController
from zilong.worker import api as worker_api

CONF = cfg.CONF
LOG = logging.getLogger(__name__)


## Docker Controller
class ContainerDetailController(RestController):
    def __init__(self, container_id):
        self.container_id = container_id

    @expose(template='json')
    def get(self):
        LOG.debug("GET /containers/%s", self.container_id)
        rpcapi = worker_api.API(context=request.context)
        container = rpcapi.get_container_details(container_id=self.container_id)
        if not container:
            pecan.abort(404)
        return container


class ImageDetailController(RestController):
    def __init__(self, image_id):
        self.image_id = image_id

    @expose(template='json')
    def get(self):
        LOG.debug("GET /images/%s", self.image_id)
        rpcapi = worker_api.API(context=request.context)
        image = rpcapi.get_image_details(image_id=self.image_id)
        if not image:
            pecan.abort(404)
        return image


class ContainersController(RestController):
    @expose(template='json')
    def get_all(self):
        LOG.debug("GET /containers")
        rpcapi = worker_api.API(context=request.context)
        containers = rpcapi.list_containers()
        return containers

    @expose()
    def _lookup(self, container_id, *remainder):
        if container_id:
            return ContainerDetailController(container_id), remainder
        else:
            pecan.abort(404)


class ImagesController(RestController):
    @expose(template='json')
    def get_all(self):
        LOG.debug("GET /images")
        rpcapi = worker_api.API(context=request.context)
        images = rpcapi.list_images()
        return images

    @expose()
    def _lookup(self, image_id, *remainder):
        if image_id:
            return ImageDetailController(image_id), remainder
        else:
            pecan.abort(404)


class SystemController(RestController):
    @expose(template='json')
    def get(self):
        LOG.debug("GET /system/info")
        rpcapi = worker_api.API(context=request.context)
        info = rpcapi.get_system_info()
        return info


class DockerController(RestController):
    containers = ContainersController()
    images = ImagesController()
    system = SystemController()

    @expose(template='json')
    def get(self):
        LOG.debug("GET /docker")
        return {
            "containers": "/docker/containers",
            "images": "/docker/images",
            "system": "/docker/system"
        }
