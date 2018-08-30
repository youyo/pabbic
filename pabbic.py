#!/usr/bin/env python3
# coding: utf-8

import fire
from zabbix.api import ZabbixAPI
import os
import json


class Pabbic():
    def __init__(self):
        pass

    def get_screen_with_no_host_registration(self, format='json'):
        response = {
            'count': 0
        }
        params = {'output': 'extend', 'sortfield': 'screenid'}
        zapi = self.__auth()
        resp = self.__request(zapi, 'screen.get', params)
        for result in resp['result']:
            params = {'output': 'extend', 'screenids': result['screenid'], 'countOutput': True}
            resp = self.__request(zapi, 'screenitem.get', params)
            if resp['result'] == '0':
                response['count'] += 1
        if format == 'text':
            print(response['count'])
        else:
            print(json.dumps(response))

    def get_disabled_host(self, format='json'):
        params = {'filter': {'status': 1}, 'output': 'extend'}
        zapi = self.__auth()
        resp = self.__request(zapi, 'host.get', params)
        if format == 'text':
            hosts = []
            for h in resp['result']:
                hosts.append(h['host'])
            print('\n'.join(hosts))
        else:
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
