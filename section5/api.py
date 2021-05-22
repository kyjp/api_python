# 楽天api

import requests
import os
import pandas as pd
from dotenv import load_dotenv

URL = 'https://app.rakuten.co.jp/services/api/IchibaItem/Search/20170706'

load_dotenv()

API_ID = os.environ['RAKUTEN_API_ID']

params = {
    'applicationId': API_ID,
    'format': 'json',
    'keyword': 'バスローブ',
    'minPrice': 10000
}

res = requests.post(URL, params)
# print(res.status_code)
result = res.json()
items = result['Items']
# print(len(items))
# print(pd.DataFrame(items)[:3])
items = [item['Item'] for item in items]
df = pd.DataFrame(items)
# print(df.columns)
columns = ['itemCode', 'itemName', 'catchcopy', 'itemCaption', 'itemPrice',
           'shopCode', 'shopName', 'reviewCount', 'shopUrl', 'availability',
           'reviewAverage', 'itemUrl']
df = df[columns]
# print(df[:3])
new_columns = ['商品コード', '商品名', 'キャッチコピー', '商品説明', '商品価格',
               '店コード', '店名', 'レビュー数', '店舗URL', '販売可能', 'レビュー平均点', '商品URL']

df.columns = new_columns
# print(df[:1])
# print(df.dtypes)

# print(df.head())
# print(df.sort_values('商品価格', ascending=True))
# print(df.max())
# print(df.describe())
print(df[df['レビュー数'] > 20])
