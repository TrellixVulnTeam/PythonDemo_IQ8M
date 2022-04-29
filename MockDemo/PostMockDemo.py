#!/usr/bin/python
# -*- coding: utf-8 -*-
# @Time: 2022/2/17 11:13 上午
# @Author: xiajian
# @File: PostMockDemo.py
# @description: 启动一个post请求的接口服务,通过参数的key返回对应擦值


import json

import flask

server = flask.Flask(__name__)  # 创建一个服务，把当前这个python文件当做一个服务


@server.route('/data', methods=['post'])
def post_json():
    if flask.request.is_json:
        print(flask.request.json)
        name = flask.request.json.get('name')  # 获取json请求体的第一个参数的值
        age = flask.request.json.get('age')  # 获取json请求体的第二个参数的值
        data = {'name': name, 'age': age}
        # 构建响应头域和状态码
        resp = flask.make_response(json.dumps(data, ensure_ascii=False))
        resp.status = "888"
        resp.content_type = "application/json"
        resp.headers[
            "python"] = "python flask"
        return resp
    else:
        return json.dumps({'msg': '请传json格式参数'}, ensure_ascii=False)


if __name__ == '__main__':
    print("http://127.0.0.1:5010/data")
    server.run(debug=True, port=5010, host='127.0.0.1')  # 指定访问端口、host
