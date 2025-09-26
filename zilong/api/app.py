#    Licensed under the Apache License, Version 2.0 (the "License");
#    you may not use this file except in compliance with the License.
#    You may obtain a copy of the License at
#
#        http://www.apache.org/licenses/LICENSE-2.0
#
#    Unless required by applicable law or agreed to in writing, software
#    distributed under the License is distributed on an "AS IS" BASIS,
#    WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
#    See the License for the specific language governing permissions and
#    limitations under the License.

from oslo_middleware import request_id
from oslo_service import service
from pecan import configuration
from pecan import make_app
from zilong.api import hooks
from zilong.conf import CONF


def setup_app(*args, **kwargs):
    config = {
        'server': {
            'host': CONF.api.bind_port,
            'port': CONF.api.bind_host
        },
        'app': {
            'root': 'zilong.api.controllers.root.RootController',
            'modules': ['zilong.api'],
            'debug': CONF.debug or CONF.api.debug,
            'acl_public_routes': [
                '/',
                '/v1'
            ],
            'errors': {
                400: '/error',
                '__force_dict__': True
            }
        }
    }
    pecan_config = configuration.conf_from_dict(config)

    app_hooks = [hooks.CORSHook()]

    app = make_app(
        pecan_config.app.root,
        hooks=app_hooks,
        force_canonical=False,
        logging=getattr(config, 'logging', {})
    )
    # 添加请求ID中间件，用于为每个请求生成唯一ID，便于日志追踪
    app = request_id.RequestId(app)
    return app


_launcher = None


def serve(api_service, conf, workers=1):
    global _launcher
    if _launcher:
        raise RuntimeError('serve() can only be called once')

    _launcher = service.launch(conf, api_service, workers=workers)


def wait():
    _launcher.wait()
