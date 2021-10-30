import requests

URL = "https://sbelqis.intelgx.com/graphql"


class Belqis:
    headers = None

    def __init__(self, token):
        self.headers = {'Authorization': f'JWT {token}'}

    def diac(self, sentence):
        try:
            query = """
                query{
                    diac(sentence:"%s")
                }
            """ % sentence
            res = requests.post(
                URL, json={'query': query}, headers=self.headers)

            if res.ok:
                return res.json()
            return {'errors': [{'message': res.reason}]}
        except Exception as e:
            return {'errors': [{'message': str(e)}]}
