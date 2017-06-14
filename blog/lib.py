import hashlib

import base64


class Lib:
    def __init__(self):
        pass

    @staticmethod
    def md5encode(string):
        # 参数必须是byte类型，否则报Unicode-objects must be encoded before hashing错误
        m = hashlib.md5(string.encode(encoding='utf-8'))
        return m.hexdigest()

    @staticmethod
    def base64encode(string):
        encodestring = base64.b64encode(string.encode('utf-8'))
        return str(encodestring, 'utf-8')

    @staticmethod
    def base64decode(string):
        return base64.b64decode(string).decode()
