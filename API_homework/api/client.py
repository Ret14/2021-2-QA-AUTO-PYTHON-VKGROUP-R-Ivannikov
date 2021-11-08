import logging
import random
import string
import time
import json
from urllib.parse import urljoin
import requests
from requests.cookies import cookiejar_from_dict

logger = logging.getLogger('test')
MAX_RESPONSE_LENGTH = 400


class ApiClient:

    base_url = 'https://target.my.com/api'
    segment_id = None

    def __init__(self, user, password):
        self.user = user
        self.password = password
        self.session = requests.Session()
        self.csrf = None
        self.image_id = None

    def post_login(self):
        headers = {
            'Referer': 'https://target.my.com/'
        }
        data = {
            'email': self.user,
            'password': self.password,
            'continue': 'https://target.my.com/auth/mycom?state=target_login%3D1%26ignore_opener%3D1#email',
            'failure': 'https://account.my.com/login/'
        }
        response = requests.post(url='https://auth-ac.my.com/auth?lang=ru&nosavelogin=0',
                             data=data, headers=headers, allow_redirects=True
                             )
        return response

    @staticmethod
    def catch_cookie(response, cookie_name, set_cookie_name='Set-Cookie'):
        set_cookie = response.headers[set_cookie_name].split(';')
        return [c for c in set_cookie if cookie_name in c][0].split('=')[-1]

    def get_csrf(self):
        headers = {
            'Referer': 'https://target.my.com/dashboard'
        }
        resp = self.session.request(method='GET', url='https://target.my.com/csrf/', headers=headers)
        set_cookie = resp.headers['set-cookie'].split(';')
        return [c for c in set_cookie if 'csrftoken' in c][0].split('=')[-1]

    def collect_cookies(self, post_login_response):
        self.session.cookies = cookiejar_from_dict({
            'mc': self.catch_cookie(post_login_response.history[0], 'mc'),
            'mrcu': self.catch_cookie(post_login_response.history[0], 'mrcu'),
            'sdc': self.catch_cookie(post_login_response.history[4], 'sdc'),
            'z': self.catch_cookie(post_login_response, 'z'),
        })

    def target_authorize(self):
        post_login_response = self.post_login()
        self.collect_cookies(post_login_response)
        headers = {
            'Referer': 'https://target.my.com/auth/mycom?state=target_login%3D1%26ignore_opener%3D1'
        }
        self.session.request(method='GET', url='https://target.my.com/dashboard', headers=headers)
        self.csrf = self.get_csrf()
        self.session.cookies.set(name='csrftoken', value=self.csrf)

    def headers_xcsrf(self):
        return {
            'X-CSRFToken': self.csrf,
        }

    @staticmethod
    def generate_string(length=10):
        letters = string.ascii_lowercase
        random_string = ''.join(random.choice(letters) for i in range(length-4))
        random_string = random_string + str(int(time.time()) % 10000)
        return random_string

    def post_segment(self):
        query = {
            'fields': 'relations__object_type,relations__object_id,relations__params,relations__params__score,'
                      'relations__id,relations_count,id,name,pass_condition,created,campaign_ids,users,flags'
        }
        data = {
            "name": self.generate_string(),
            "pass_condition": 1,
            "relations": [
                {
                    "object_type": "remarketing_player",
                    "params":
                        {
                        "type": "positive",
                        "left": 365,
                        "right": 0
                    }
                }
            ],
            "logicType": "or"
        }
        data = json.dumps(data, indent=4)
        resp = self.session.request(method='POST', url='https://target.my.com/api/v2/remarketing/segments.json',
                                    data=data, params=query, headers=self.headers_xcsrf(), json=True
                                    )
        logger.info(f'Segment Got: {resp.status_code} \n Content: {resp.text}')
        segment_json = json.loads(resp.text)
        self.segment_id = segment_json['id']
        self.segment_assertion()
        # yield resp
        # self.delete_segment()

    def segment_assertion(self):
        response = self.session.request(url=f'https://target.my.com/api/v2/remarketing/segments/{self.segment_id}.json',
                                        method='GET')
        logger.info(f'Got: {response.status_code} \n Content: {response.text}')
        assert response.ok

    def delete_segment(self):
        response = self.session.request(method='DELETE', headers=self.headers_xcsrf(),
                                        url=f'https://target.my.com/api/v2/remarketing/segments/{self.segment_id}.json'
                                        )
        self.segment_gone_assertion()

    def segment_gone_assertion(self):
        response = self.session.request(url=f'https://target.my.com/api/v2/remarketing/segments/{self.segment_id}.json',
                                        method='GET')
        logger.info(f'Got: {response.status_code} \n Content: {response.text}')
        assert not response.ok
