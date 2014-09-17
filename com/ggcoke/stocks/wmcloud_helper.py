#!/usr/bin/python
# -*- coding: utf-8 -*-

__author__ = 'ggcoke'

import http_util

HOST = 'api.wmcloud.com'
PORT = 9763
WMCLOUD_VERSION = '1.0.0'
TOKEN = 'token'


class WMCloudHelper(object):

    def __init__(self):
        self.net_util = http_util.HttpUtils(HOST, PORT, True)

    def get(self, path, headers={}):
        if self.net_util is not None:
            return self.net_util.get(path, headers)

    @staticmethod
    def create_header():
        """
        Create a request header with authorization token

        :return: request header
        """
        return {"Authorization": "Bearer " + TOKEN}

    @staticmethod
    def create_path(api_type, api_name, **kw):
        """
        Create request url with params

        :param api_type: type of request api
        :param api_name: name of request api
        :param kw: params of request
        :return: an url with params
        """
        ret = None
        if (api_type is not None) and (api_name is not None):
            ret = '/' + api_type + \
                  '/' + WMCLOUD_VERSION + \
                  '/' + api_name + '?'
            for k, v in kw.iteritems():
                ret += (k + '=')
                if v is not None:
                    ret += v
                ret += '&'

            ret = ret.rstrip('&')

        return ret





