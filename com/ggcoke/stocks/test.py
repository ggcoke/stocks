#! /usr/bin/python
# -*- coding: utf-8 -*-

__author__ = 'ggcoke'

import wmcloud_helper

HOST = 'api.wmcloud.com'
PORT = 9763
TOKEN = 'token'


if __name__ == '__main__':
    params = {'field': None,
              'ticker': '000001',
              'secID': None,
              'callback': None}
    path = wmcloud_helper.WMCloudHelper.create_path('bond', 'getBond.json', **params)
    header = wmcloud_helper.WMCloudHelper.create_header()

    helper = wmcloud_helper.WMCloudHelper()
    result = helper.get(path, header)

    print(type(result))
    print(result)
    print(result['retCode'])
    print(result['data'][0]['typeName'])
