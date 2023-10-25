api = 'xxxxxxxxxxxxxxxxxx'

# *** 1. Pythonでローカルサーバーの準備

from bottle import *

# --- CORSへの対応 https://qiita.com/rysk_lunch/items/d7cc7cd8ab5fa1714312

@hook('after_request')
def enable_cors():
    response.headers['Access-Control-Allow-Origin'] = '*'
    response.headers['Access-Control-Allow-Methods'] = '*'
    response.headers['Access-Control-Allow-Headers'] = '*'

@route('/', method='OPTIONS')
def response_for_options(**kwargs):
    return {}

# --- CORSへの対応ここまで

@post('/')
def index():
    page_text = html_to_text(request.json['page'])
    description = gpt(page_text)
    return description


# *** 2. ChatGPTのAPIを使う準備

import openai
openai.api_key = api

def message(role, text):
    return { 'role': role, 'content': text }

system = message('system', """
適当なHTMLファイルから抜き出した文字列を渡すため、概要を抽出して簡潔に内容を日本語で説明をしてください。
""")

def gpt(text):
    response = openai.ChatCompletion.create(
        model='gpt-3.5-turbo',
        messages=[system] + [message('user', text)]
    )

    return response['choices'][0]['message']['content']


# *** 3. HTMLファイルの加工

from bs4 import BeautifulSoup

def html_to_text(html):
    soup = BeautifulSoup(html, 'html.parser')
    return '/n'.join(soup.stripped_strings)

# run localhost
try:
    run(host='0.0.0.0', port=8000, reloader=True)
except KeyboardInterrupt:
    pass
