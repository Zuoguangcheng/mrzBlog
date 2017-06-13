import hashlib


class Lib:
    def __init__(self):
        pass

    @staticmethod
    def md5encode(string):
        # 参数必须是byte类型，否则报Unicode-objects must be encoded before hashing错误
        m = hashlib.md5(string.encode(encoding='utf-8'))
        return m.hexdigest()
