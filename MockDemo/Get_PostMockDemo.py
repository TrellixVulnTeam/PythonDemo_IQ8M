#!/usr/bin/python
# -*- coding: utf-8 -*-
# @Time: 2022/2/17 11:13 上午
# @Author: xiajian
# @File: Get_PostMockDemo.py
# @description: 启动一个get&post请求的接口服务,通过参数的key返回对应擦值

from flask import Flask, jsonify, make_response

app = Flask(__name__)
data = [
    {'key1': 'V1', 'key2': 'V2', 'id': '1'}
]
not_exist = {"msg": "task does not exist"}
keys = ['key1', 'key2', "id"]
exist = {"msg": "value is exist"}


@app.route("/dataAPI/data/<string:value>", methods=['get', 'post'])
def get_data(value):
    if len(value) > 0 and value in keys:
        for d in keys:
            print("values == ", keys)
            print("value == ", value)
            print("d == ", d)
            if value == d:
                print("data ==  ", data[0])
                print(data[0][d])
                return make_response(jsonify(data[0][d]), 200)
    else:
        return make_response(jsonify(not_exist), 404)


if __name__ == '__main__':
    print("http://127.0.0.1:8080/dataAPI/data/V1")
    app.run(host='127.0.0.1', port=8080, debug=True)
