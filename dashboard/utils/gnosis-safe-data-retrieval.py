# Using existing Subgraph https://thegraph.com/hosted-service/subgraph/gjeanmart/gnosis-safe-goerli
# https://towardsdatascience.com/connecting-to-a-graphql-api-using-python-246dda927840

import requests
import json
import pandas as pd
from datetime import datetime

# Enter this URL into your browser and click "Explorer" to filter by data types
API_URL = 'https://api.thegraph.com/subgraphs/name/gjeanmart/gnosis-safe-goerli'

def prepareJSON(query):
    r = requests.post(API_URL, json={'query': query})
    return json.loads(r.text)

# Example query that retrieves 
def walletInfo(address):
    return

def firstWallet(num):
    query = """query {
        wallets(first: {}) {
            id
            creator
            network
            stamp
        }
    }""".format(num)
    json_data = prepareJSON(query)
    wallets_data = json_data['data']['wallets']
    wallets_df = pd.DataFrame(wallets_data)
    wallets_df['stamp'] = pd.to_datetime(pd.to_numeric(wallets_df['stamp']), unit='s')
    return

def firstTransactions(num):
    query = """query {
        transactions(first: {}) {
            id
            stamp
            block
            hash
        }
    }""".format(num)
    json_data = prepareJSON(query)
    transactions_data = json_data['data']['transactions']
    transactions_df = pd.DataFrame(transactions_data)
    transactions_df['stamp'] = pd.to_datetime(pd.to_numeric(transactions_df['stamp']), unit='s')
    return

