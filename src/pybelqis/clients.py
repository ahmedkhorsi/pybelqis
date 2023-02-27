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

