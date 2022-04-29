# -*- coding: utf-8 -*-
# @Time: 2022/2/17 11:13 上午
# @Author: xiajian
# @File: GetMockDemo.py
# @description: 启动一个get请求的接口服务


import json
import time

import flask

server = flask.Flask(__name__)  # 创建一个服务，把当前这个python文件当做一个服务


@server.route('/get/date_time', methods=['get'])
# @server.route()可以将普通函数转变为服务、接口的路径、请求方式，如果不写methods则默认get方法
def date_time():
    """查询字符串:无，消息体：无，返回结果：SystemTime"""
    response_data = {
        "SystemTimeObject": {
            "VIIDServerID": "123",
            "TimeMode": "1",
            "LocalTime": time.strftime('%Y%m%d%H%M%S', time.localtime(time.time())),
        }
    }
    return json.dumps(response_data, ensure_ascii=False)


if __name__ == '__main__':
    server_host = '127.0.0.1'
    server_port = 5005
    server_path = "/get/date_time"
    print("http://" + server_host + ":" + str(server_port) + server_path)
    server.run(debug=True, port=server_port, host=server_host)  # 指定访问端口、host
