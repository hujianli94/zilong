#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json
from oslo_config import cfg
from oslo_log import log as logging
import requests
from requests.auth import HTTPBasicAuth

CONF = cfg.CONF
CONF.import_group('docker', 'zilong.common.docker.config')

LOG = logging.getLogger(__name__)


def send_request(resource, method="GET", **kwargs):
    # The verify=false param in the request should be removed eventually
    url = CONF.docker.url + resource
    httpuser = CONF.docker.username
    httppwd = CONF.docker.password
    resp = None
    try:
        resp = requests.request(method, url, verify=False, auth=HTTPBasicAuth(httpuser, httppwd), **kwargs)
    except requests.exceptions.RequestException as e:
        LOG.error(e)
    return resp


def get_containers():
    resp = send_request('/containers/json')
    if resp and resp.status_code == 200:
        return resp.json()
    else:
        LOG.error("Failed to get containers: %s", resp.text)
        return []


def get_container_details(container_id):
    resp = send_request(f'/containers/{container_id}/json')
    if resp and resp.status_code == 200:
        return resp.json()
    else:
        LOG.error("Failed to get container details: %s", resp.text)
        return {}


def get_images():
    resp = send_request('/images/json')
    if resp and resp.status_code == 200:
        return resp.json()
    else:
        LOG.error("Failed to get images: %s", resp.text)
        return []


def get_image_details(image_id):
    resp = send_request(f'/images/{image_id}/json')
    if resp and resp.status_code == 200:
        return resp.json()
    else:
        LOG.error("Failed to get image details: %s", resp.text)
        return {}


def get_system_info():
    resp = send_request('/info')
    if resp and resp.status_code == 200:
        return resp.json()
    else:
        LOG.error("Failed to get system info: %s", resp.text)
        return {}
