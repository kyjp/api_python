# ホットペッパーapi
import os
from dotenv import load_dotenv
import requests
import pandas as pd

URL = 'http://webservice.recruit.co.jp/hotpepper/gourmet/v1/'

load_dotenv()

API_KEY = os.environ['RECUEST_API_KEY']

params = {
    'key': API_KEY,
    'keyword': '沖縄',
    'format': 'json',
    'count': 100
}

res = requests.get(URL, params)
result = res.json()
items = result['results']['shop']
print(len(items))
# 表形式に変形
pd.DataFrame()
df = pd.DataFrame(items)
# print(df)
# print(df.head())
# 欲しい情報をオブジェクトから取得
df = df[['name', 'address', 'wifi']]
print(df)
# インデックスを削除してcsvに書き出し
df.to_csv('hotpepper.csv', index=False)
