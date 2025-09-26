#!/usr/bin/env python
# -*- coding: utf-8 -*-
from oslo_config import cfg

# Configurations
docker_opts = [
    cfg.StrOpt('url',
               default='http://localhost:2375',
               help=("The URL of the Docker daemon")),
    cfg.StrOpt('username',
               default='',
               help=("Username for Docker authentication")),
    cfg.StrOpt('password',
               default='',
               help=("Password for Docker authentication"))]

docker_conf_group = cfg.OptGroup(name='docker', title='Docker options')
cfg.CONF.register_group(docker_conf_group)
cfg.CONF.register_opts(docker_opts, group=docker_conf_group)
