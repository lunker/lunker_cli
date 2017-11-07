import re
from binascii import hexlify
try:
    from urllib import quote
except ImportError:
    from urllib.parse import quote

import requests
import rsa


class NaverSession(requests.Session):

    def login(self, user_id, user_pw, do_finalize=True):
        """
            Try naver login 
        :param user_id: user id
        :param user_pw: user password 
        :param do_finalize: 
        :return: None
        """
        keys = self._get_keys()

        public_key = rsa.PublicKey(keys['evalue'], keys['nvalue'])
        raw_data = (
            chr(len(keys['sessionkey'])) + keys['sessionkey']
            + chr(len(user_id)) + user_id
            + chr(len(user_pw)) + user_pw
        ).encode()

        enc_data = rsa.encrypt(raw_data, public_key)

        login_url = 'https://nid.naver.com/nidlogin.login'
        data = {
            'enctp': 1,
            'encpw': hexlify(enc_data),
            'encnm': keys['keyname'],
            'svctype': 0,
            'url': 'https://www.naver.com/',
            'enc_url': quote('http://www.naver.com/'),
            'postDataKey': '',
            'nvlong': '',
            'saveID': '',
            'smart_level': '1',
            'id': '',
            'pw': ''
        }
        r = self.post(login_url, data=data, headers={'User-Agent': 'python-naverlogin'} )

        if 'https://nid.naver.com/login/sso/finalize.nhn' in r.text:
            if do_finalize:
                location_replace_re = re.compile(r'location\.replace\("(.+?)"\)')
                finalize_url = location_replace_re.search(r.text).group(1)

                r = self.get(finalize_url)

                return location_replace_re.search(r.text) is not None
            return True
        else:
            return False

    def logout(self):
        self.get('http://nid.naver.com/nidlogin.logout')

    def _get_keys(self):
        keys_url = 'http://static.nid.naver.com/loginv3/js/keys_js.nhn'
        r = self.get(keys_url)

        key_re = re.compile(r"(sessionkey|keyname|evalue|nvalue)\s*=\s*'(.+?)';")
        keys = dict(key_re.findall(r.text))
        keys['nvalue'] = int(keys['nvalue'], 16)
        keys['evalue'] = int(keys['evalue'], 16)

        return keys

    def create_http_get(self, url, **kwargs):
        """
        
        :param url: 
        :param kwargs:
        :rtype: requests.Response
        :return: response 
        """

        response = self.get(url, **kwargs, headers={'User-Agent': 'python-naverlogin', 'Content-Type': 'charset=KSC5601'})

        '''
        print(response)
        print(response.url)
        print(response.content)
        print("{cls_name} response\n{response}".format(cls_name=self.__class__.__name__, response=response))
        print("{cls_name} response\n{response}".format(cls_name=self.__class__.__name__, response=response.text))
        '''

        return response