import requests
import json


def request(url, method):
    kwargs = {'allow_redirects': True,
              'data': '{"auth": {"identity": {"password": {"user": {"password": "welcome", "name": "admin"...son',
              'Content-Type': 'application/json', 'OpenStack-API-Version': 'volume 3.40',
              'User-Agent': 'python-cinderclient'}
    kwargs.setdefault('headers', kwargs.get('headers', {}))
    kwargs['headers']['Accept'] = 'application/json'

    # if osprofiler_web:
    #     kwargs['headers'].update(osprofiler_web.get_trace_id_headers())
    #
    # if 'body' in kwargs:
    #     kwargs['headers']['Content-Type'] = 'application/json'
    #     kwargs['data'] = json.dumps(kwargs.pop('body'))
    # api_versions.update_headers(kwargs["headers"], self.api_version)
    #
    # if self.global_request_id:
    #     kwargs['headers'].setdefault(REQ_ID_HEADER, self.global_request_id)

    resp = requests.request(
        method,
        url,
        kwargs)

    body = None
    if resp.text:
        try:
            body = json.loads(resp.text)
        except ValueError as e:
            print ("Load http response text error: %s", e)

    if resp.status_code >= 400:
        print ('error')
        print (resp)
        print (body)


if __name__ == '__main__':
    url = 'http://172.10.1.11/identity/v3/auth/tokens'
    method = 'POST'

    request(url, method)
