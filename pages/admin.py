import streamlit as st
import requests
import json
import pandas as pd

def authenticate(username, password):
    return username == "aaa" and password == "123"

def item_create_page():
    st.title("商品登録")

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

    with st.form(key='item_create'):
        item_name: str = st.text_input('商品名')
        brand_name: str = st.selectbox('ブランド',brands_name.keys())
        state_name: str = st.selectbox('容器',states_name.keys())
        taste_name: str = st.selectbox('味',tastes_name.keys())
        item_bfl: int = st.number_input('辛さ', step=1, min_value=0, max_value=5)
        item_price: int = st.number_input('価格', step=1, min_value=0)
        submit_button = st.form_submit_button(label='登録')

    if submit_button:
        brand_id: int = brands_name[brand_name]
        state_id: int = states_name[state_name]
        taste_id: int = tastes_name[taste_name]
        
        data = {
            'item_name': item_name,
            'brand_id': brand_id,
            'state_id': state_id,
            'taste_id': taste_id,
            'item_bfl': item_bfl,
            'item_price': item_price
        }
        
        # 商品登録
        url = 'http://127.0.0.1:8000/items'
        res = requests.post(
            url,
            data=json.dumps(data)
        )
        if res.status_code == 200:
            st.success('登録完了')
            
        else:
            st.write(res.status_code)
            st.json(res.json())

def item_update_page():
    st.title("商品更新")
    
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
    # df_items.columns = ['商品名', 'ブランドID', '容器ID', '味ID', '辛さ', '価格', 'アイテムID']

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

    with st.form(key='item_update'):
        item_name: str = st.selectbox('商品名', items_name.keys())
        brand_name: str = st.selectbox('ブランド',brands_name.keys())
        state_name: str = st.selectbox('容器',states_name.keys())
        taste_name: str = st.selectbox('味',tastes_name.keys())
        item_bfl: int = st.number_input('辛さ', step=1, min_value=0, max_value=5)
        item_price: int = st.number_input('価格', step=1, min_value=0)
        submit_button = st.form_submit_button(label='更新')

    if submit_button:
        item_id: int = items_name[item_name]
        brand_id: int = brands_name[brand_name]
        state_id: int = states_name[state_name]
        taste_id: int = tastes_name[taste_name]
        
        data = {
            'item_name': item_name,
            'brand_id': brand_id,
            'state_id': state_id,
            'taste_id': taste_id,
            'item_bfl': item_bfl,
            'item_price': item_price
        }
        
        # 商品更新
        url = f'http://127.0.0.1:8000/items/{item_id}'
        res = requests.put(
            url,
            data=json.dumps(data)
        )
        if res.status_code == 200:
            st.success('更新完了')
            
        else:
            st.write(res.status_code)
            st.json(res.json())

def item_delete_page():
    st.title("商品削除")
    
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
    # df_items.columns = ['商品名', 'ブランドID', '容器ID', '味ID', '辛さ', '価格', 'アイテムID']

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

    with st.form(key='item_delete'):
        item_name: str = st.selectbox('商品名', items_name.keys())
        submit_button = st.form_submit_button(label='削除')

    if submit_button:
        item_id: int = items_name[item_name]
        
        data = {'item_name': item_name}

        # 商品削除
        url = f'http://127.0.0.1:8000/items/{item_id}'
        res = requests.delete(url)
    
        if res.status_code == 200:
            st.success('削除完了')
            
        else:
            st.write(res.status_code)
            st.json(res.json())

def brand_create_page():
    st.title('ブランド登録')

    # ブランド一覧取得
    url_brands = 'http://127.0.0.1:8000/brands'
    res = requests.get(url_brands)
    brands = res.json()
    # ブランド名をキー、ブランドIDをバリュー
    brands_name = {}
    for brand in brands:
        brands_name[brand['brand_name']] = brand['brand_id']

    st.write('## ブランド一覧')
    df_brands = pd.DataFrame(brands)
    st.table(df_brands)

    with st.form(key='brand'):
        brand_name: str = st.text_input('ブランド名')
        data = {
            'brand_name': brand_name
        }
        submit_button = st.form_submit_button(label='登録')

    if submit_button:
        url = 'http://127.0.0.1:8000/brands'
        res = requests.post(
            url,
            data=json.dumps(data)
        )
        if res.status_code == 200:
            st.success('登録完了')

def state_create_page():
    st.title('容器登録')

    # 容器一覧取得
    url_states = 'http://127.0.0.1:8000/states'
    res = requests.get(url_states)
    states = res.json()
    # 容器名をキー、容器IDをバリュー
    states_dict = {}
    for state in states:
        states_dict[state['state_name']] = state['state_id']

    st.write('## 容器一覧')
    df_states = pd.DataFrame(states)
    st.table(df_states)

    with st.form(key='state'):
        state_name: str = st.text_input('容器名')
        data = {
            'state_name': state_name
        }
        submit_button = st.form_submit_button(label='登録')

    if submit_button:
        url = 'http://127.0.0.1:8000/states'
        res = requests.post(
            url,
            data=json.dumps(data)
        )
        if res.status_code == 200:
            st.success('登録完了')

def taste_create_page():
    st.title('味登録')

    # 味一覧取得
    url_tastes = 'http://127.0.0.1:8000/tastes'
    res = requests.get(url_tastes)
    tastes = res.json()
    # 味名をキー、味IDをバリュー
    tastes_dict = {}
    for taste in tastes:
        tastes_dict[taste['taste_name']] = taste['taste_id']

    st.write('## 味一覧')
    df_tastes = pd.DataFrame(tastes)
    st.table(df_tastes)

    with st.form(key='taste'):
        taste_name: str = st.text_input('味名')
        data = {
            'taste_name': taste_name
        }
        submit_button = st.form_submit_button(label='登録')

    if submit_button:
        url = 'http://127.0.0.1:8000/tastes'
        res = requests.post(
            url,
            data=json.dumps(data)
        )
        if res.status_code == 200:
            st.success('登録完了')

def main():
    if "user" not in st.session_state:
        st.session_state.user = {"authenticated": False}

    username = st.text_input("Username")
    password = st.text_input("Password", type="password")

    if st.button("Login"):
        if authenticate(username, password):
            st.session_state.user["authenticated"] = True
            st.success("ログイン成功")
            
        else:
            st.session_state.user["authenticated"] = False
            st.error("ログイン失敗")

    if st.session_state.user.get("authenticated", False):
        selected_page = st.radio("ページ選択", ["商品登録", "商品更新", "商品削除", "ブランド登録", "容器登録", "味登録"])

        if selected_page == "商品登録":
            item_create_page()
        elif selected_page == "商品更新":
            item_update_page()
        elif selected_page == "商品削除":
            item_delete_page()
        elif selected_page == "ブランド登録":
            brand_create_page()
        elif selected_page == "容器登録":
            state_create_page()
        elif selected_page == "味登録":
            taste_create_page()

if __name__ == "__main__":
    main()
