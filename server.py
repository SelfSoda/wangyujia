# coding:utf-8
from flask import Flask, redirect
import os
import random

app = Flask(__name__)

@app.route('/')
def redi():
    urls = [
        'https://www.wjx.top/jq/21850176.aspx',
        'https://www.wjx.top/jq/22041433.aspx',
        'https://www.wjx.top/jq/22051946.aspx',
        'https://www.wjx.top/jq/22056293.aspx',
        'https://www.wjx.top/jq/22061793.aspx',
        'https://www.wjx.top/jq/22073136.aspx'
    ]
    return redirect(urls[random.randint(0,5)])

if __name__ == '__main__':
    port = int(os.environ.get('PORT', 5000))
    app.run(host='0.0.0.0',port=port)
