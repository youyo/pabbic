#!/usr/bin/env python
# coding: utf-8

import fire
from zabbix.api import ZabbixAPI
import os
import json


class Pabbic():
    def __init__(self):
        pass

    def get_disabled_host(self):
        params = {'filter': {'status': 1}, 'output': 'extend'}
        zapi = self.__auth()
        resp = self.__request(zapi, 'host.get', params)
        print(json.dumps(resp['result']))

    def __request(self, zapi, method, params):
        resp = zapi.do_request(method, params)
        return resp

    def __auth(self):
        zapi = ZabbixAPI(
            url=os.environ["PABBIC_URL"],
            user=os.environ["PABBIC_USER"],
            password=os.environ["PABBIC_PASSWORD"])
        return zapi


if __name__ == '__main__':
    fire.Fire(Pabbic)
