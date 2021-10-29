import requests
from gql.transport.aiohttp import AIOHTTPTransport
from gql import Client, gql


class Belqis:

    def __init__(self, token):
        transport = AIOHTTPTransport(url="https://sbelqis.intelgx.com/graphql", headers={'Authorization': f'JWT {token}'})
        self.client = Client(transport=transport, fetch_schema_from_transport=True)

    def tashkeel(self, text):
        query = gql(f'''
            query {{
                tashkeel(sentence: "{text}")
            }}
        ''')
        return self.client.execute(query)['tashkeel']

    def ner(self, text):
        query = gql(f'''
            query {{
                ner(text: "{text}"){{
                    token
                    tag
                }}
            }}
        ''')
        return self.client.execute(query)['ner']

    def dictate(self, audio_url):
        query = gql(f'''
            mutation Dictate($audio: Upload!){{
                dictate(audio: $audio){{
                    text
                }}
            }}
        ''')
        with open(audio_url, 'rb') as f:
            result = self.client.execute(query, variable_values={'audio': f}, upload_files=True)
        return result['dictate']['text']

    def pronounce(self, audio_url, ref_text):
        query = gql(f'''
            mutation Pronounce($audio: Upload!,$refText: String!){{
                pronounce(audio: $audio, refText: $refText){{
                    mistakes
                    predicted
                }}
            }}
        ''')
        with open(audio_url, 'rb') as f:
            result = self.client.execute(query, variable_values={'audio': f, 'refText': ref_text}, upload_files=True)
        return result['pronounce']


    def send(self):
        try:
            res = requests.post(
                URL, json={'query': self.query}, headers=self.headers, verify=True)

            if res.ok:
                return res.json()
            return {'errors': [{'message': res.reason}]}
        except Exception as e:
            return {'errors': [{'message': str(e)}]}
