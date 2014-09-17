#! /usr/bin/python
# -*- coding: utf-8 -*-

" http utils "

__author__ = 'ggcoke'

import httplib
import json
import traceback


class HttpUtils(object):
    GET = 'GET'
    POST = 'POST'

    def __init__(self, host, port=None, ssl=False):
        """
        Http utils to request using method get or post

        :param host: host of target site
        :param port: port of target site
        :param ssl: whether the connection is ssl
        :return:
        """
        if ssl:
            self.http_client = httplib.HTTPSConnection(host, port)
        else:
            self.http_client = httplib.HTTPConnection(host, port)

        print('HttpUtils init')

    def get(self, path, headers={}):
        result = None
        if self.http_client is not None:
            try:
                self.http_client.request(self.GET, path, headers=headers)
                response = self.http_client.getresponse()

                result = response.read()
                if response.status == httplib.OK:
                    result = json.loads(result)

                return result
            except Exception, e:
                traceback.print_exc()
                raise e
        return result





