import asyncio
import pandas as pd
from airstack.execute_query import AirstackClient

async def fetchTokenData():
    api_client = AirstackClient(api_key='58e9d545875542babaae511117a58cef')

    query1 = """
 query MyQuery($name1: Address!, $name2: Address!) {
  TokenBalances(
    input: {filter: {tokenAddress: {_eq: $name1}}, blockchain: ethereum}
  ) {
    TokenBalance {
      chainId
      blockchain
      amount
      lastUpdatedTimestamp
      id
    }
  }
  test2: TokenTransfers(
    input: {filter: {tokenAddress: {_eq: $name2}}, blockchain: ethereum}
  ) {
    TokenTransfer {
      chainId
      blockchain
      id
      amount
    }
  }
}
  """
    variables1 = {
        "name1": "0x1130547436810db920fa73681c946fea15e9b758",
        "name2": "0xf4eced2f682ce333f96f2d8966c613ded8fc95dd",
    }

    execute_query_client = api_client.create_execute_query_object(query=query1, variables=variables1)
    query_response = await execute_query_client.execute_paginated_query()
    if query_response.has_next_page:
        next_page_response = await query_response.get_next_page
    if next_page_response.has_prev_page:
        prev_page_response = await next_page_response.get_prev_page
    
    query = """
     query MyQuery($name1: Address!) {
      test1: TokenBalances(
        input: {filter: {tokenAddress: {_eq: $name1}}, blockchain: ethereum}
      ) {
        pageInfo {
          nextCursor
          prevCursor
        }
        TokenBalance {
          chainId
          blockchain
          amount
          lastUpdatedTimestamp
          id
        }
      }
    }
      """
    variables = {
        "name1": "0x1130547436810db920fa73681c946fea15e9b758",
    }


    tokentransfer_df = pd.DataFrame(query_response.data['test2']['TokenTransfer'])
    execute_query_client = api_client.create_execute_query_object(query=query, variables=variables)
    query_response = await execute_query_client.execute_query()

    tokenbalance_df = pd.DataFrame(query_response.data['test1']["TokenBalance"])
    return [tokentransfer_df, tokenbalance_df]

asyncio.run(fetchTokenData())