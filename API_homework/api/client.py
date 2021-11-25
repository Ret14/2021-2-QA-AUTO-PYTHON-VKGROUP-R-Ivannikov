import logging
import os.path
import random
import string
import time
import json
import requests

logger = logging.getLogger('test')
MAX_RESPONSE_LENGTH = 300


class ApiClient:

    segment_id = None
    camp_id = None
    csrf = None
    image_id = None

    def __init__(self, user, password, repo_root):
        self.user = user
        self.password = password
        self.session = requests.Session()
        self.repo_root = repo_root

    def headers_csrf(self):
        return {'X-CSRFToken': self.csrf}

    @staticmethod
    def generate_string(length=10):
        letters = string.ascii_lowercase
        return ''.join(random.choice(letters) for i in range(length-4)) + str(int(time.time()) % 10000)

    def get_csrf(self):
        resp = self.session.request(method='GET', url='https://target.my.com/csrf/')
        return resp.cookies.get('csrftoken')

    def post_segment(self):
        query = {
            'fields': 'relations__object_type,relations__object_id,relations__params,relations__params__score,'
                      'relations__id,relations_count,id,name,pass_condition,created,campaign_ids,users,flags'
        }
        with open(os.path.join(self.repo_root, 'api/segment_pattern.json'), 'r') as f:
            segment_payload = json.load(f)

        segment_payload['name'] = self.generate_string()
        self.log_pre(url='https://target.my.com/api/v2/remarketing/segments.json', summary='Creating segment')
        resp = self.session.request(method='POST', url='https://target.my.com/api/v2/remarketing/segments.json',
                                    json=segment_payload, params=query, headers=self.headers_csrf())
        self.log_post(resp)
        self.segment_id = json.loads(resp.text)['id']

    def delete_segment(self):
        self.log_pre(url=f'https://target.my.com/api/v2/remarketing/segments/{self.segment_id}.json',
                     summary=f'Deleting segment with id {self.segment_id}')
        response = self.session.request(method='DELETE', headers=self.headers_csrf(),
                                        url=f'https://target.my.com/api/v2/remarketing/segments/{self.segment_id}.json'
                                        )
        self.log_post(response)

    def segment_exist_check(self):
        response = self.session.request(url=f'https://target.my.com/api/v2/remarketing/segments/{self.segment_id}.json',
                                        method='GET')
        return response.ok

    def post_camp(self, image_id):
        headers = {
            'X-Campaign-Create-Action': 'new',
            'X-CSRFToken': self.csrf,
        }
        with open(os.path.join(self.repo_root, 'api/camp_pattern.json'), 'r') as f:
            camp_payload = json.load(f)

        camp_payload['name'] = self.generate_string()
        camp_payload['banners'][0]['content']['image_240x400']['id'] = image_id

        self.log_pre(url='https://target.my.com/api/v2/campaigns.json', summary='Creating campaign')
        resp = self.session.request(method='POST', url='https://target.my.com/api/v2/campaigns.json',
                                    headers=headers, json=camp_payload, allow_redirects=True)
        self.log_post(resp)
        self.camp_id = json.loads(resp.text)['id']
        return resp

    def camp_discard(self):
        data = {"status": "deleted"}
        headers = {
            'X-CSRFToken': self.csrf,
            'X-Target-Sudo': self.user
        }
        self.log_pre(url=f'https://target.my.com/api/v2/campaigns/{self.camp_id}.json',
                     summary=f'Deleting campaign with id {self.camp_id}')
        resp = self.session.request(method='POST', headers=headers, json=data,
                                    url=f'https://target.my.com/api/v2/campaigns/{self.camp_id}.json')
        self.log_post(resp)

    def post_image(self, image_path):
        file = {
            'file': open(image_path, 'rb'),
            'data': '{"width": 0, "height": 0,}'
        }
        headers = {
            'X-CSRFToken': self.csrf
        }
        self.log_pre(url='https://target.my.com/api/v2/content/static.json', expected_status=200,
                     summary='Uploading image')
        resp = self.session.request(method='POST', headers=headers, files=file,
                                    url='https://target.my.com/api/v2/content/static.json')
        self.log_post(resp)
        return json.loads(resp.text)['id']

    def target_authorize(self):
        headers = {
            'Referer': 'https://target.my.com/'
        }
        data = {
            'email': self.user,
            'password': self.password,
            'continue': 'https://target.my.com/auth/mycom?state=target_login%3D1%26ignore_opener%3D1#email',
            'failure': 'https://account.my.com/login/'
        }
        self.log_pre(url='https://auth-ac.my.com/auth?lang=ru&nosavelogin=0', expected_status=200,
                     summary='Logging into')
        response = self.session.request(method='POST', data=data, headers=headers, allow_redirects=True,
                                        url='https://auth-ac.my.com/auth?lang=ru&nosavelogin=0')
        self.log_post(response)
        self.session.request(method='GET', url='https://target.my.com/dashboard')
        self.csrf = self.get_csrf()

    def camp_exist_check(self):
        resp = self.session.request(url='https://target.my.com/api/v2/campaigns.json?fields=id%2Cname%'
                                        '2Cpackage_priced_event_type%2Cautobidding_mode&sorting=-id&'
                                        'limit=10&offset=0&_status__in=active',
                                    method='GET')
        return [c['id'] for c in json.loads(resp.text)['items'] if c['id'] == self.camp_id]

    @staticmethod
    def log_pre(url, summary, expected_status=200):
        logger.info(f' * {summary} * Performing request:\n'
                    f'URL: {url}\n'
                    f'expected status: {expected_status}\n')

    @staticmethod
    def log_post(response):
        log_str = f'RESPONSE STATUS: {response.status_code}'

        if len(response.text) > MAX_RESPONSE_LENGTH:
            if logger.level == logging.INFO:
                logger.info(f'{log_str}\n'
                            f'RESPONSE CONTENT: COLLAPSED due to response size > {MAX_RESPONSE_LENGTH}. '
                            f'Use DEBUG logging.\n'
                            f'{response.text[:MAX_RESPONSE_LENGTH]}'
                            )
            elif logger.level == logging.DEBUG:
                logger.info(f'{log_str}\n'
                            f'RESPONSE CONTENT: {response.text}\n\n'
                            )
        else:
            logger.info(f'{log_str}\n'
                        f'RESPONSE CONTENT: {response.text}\n'
                        )
