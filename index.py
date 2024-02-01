import streamlit as st
import requests
import pandas as pd

st.title('Samyang Japan')

# ブランド一覧取得
url_brands = 'http://127.0.0.1:8000/brands'
res = requests.get(url_brands)
brands = res.json()
# ブランド名をキー、ブランドIDをバリュー
brands_name = {}
for brand in brands:
    brands_name[brand['brand_name']] = brand['brand_id']

# 容器一覧取得
url_states = 'http://127.0.0.1:8000/states'
res = requests.get(url_states)
states = res.json()
# 容器名をキー、容器IDをバリュー
states_name = {}
for state in states:
    states_name[state['state_name']] = state['state_id']

# 味一覧取得
url_tastes = 'http://127.0.0.1:8000/tastes'
res = requests.get(url_tastes)
tastes = res.json()
# 味名をキー、味IDをバリュー
tastes_name = {}
for taste in tastes:
    tastes_name[taste['taste_name']] = taste['taste_id']

# 商品一覧取得
url_items = 'http://127.0.0.1:8000/items'
res = requests.get(url_items)
items = res.json()
# 商品名をキー、商品IDをバリュー
items_name = {}
for item in items:
    items_name[item['item_name']] = item['item_id']

st.write('## 商品一覧')
df_items = pd.DataFrame(items)

brands_id = {}
for brand in brands:
    brands_id[brand['brand_id']] = brand['brand_name']

states_id = {}
for state in states:
    states_id[state['state_id']] = state['state_name']

tastes_id = {}
for taste in tastes:
    tastes_id[taste['taste_id']] = taste['taste_name']

# IDを各値に変更
to_brand_name = lambda x: brands_id[x]
to_state_name = lambda x: states_id[x]
to_taste_name = lambda x: tastes_id[x]

# 特定の列に適用
df_items['brand_id'] = df_items['brand_id'].map(to_brand_name)
df_items['state_id'] = df_items['state_id'].map(to_state_name)
df_items['taste_id'] = df_items['taste_id'].map(to_taste_name)

df_items = df_items.rename(columns={
    'item_name':'商品名',
    'brand_id':'ブランド名',
    'state_id':'容器名',
    'taste_id':'味',
    'item_bfl':'辛さ',
    'item_price':'価格',
    'item_id':'商品ID',
})

st.table(df_items)