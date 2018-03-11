# -*- coding: utf-8 -*-

from django.http import HttpResponse
from django.shortcuts import render_to_response

# 表单
def search_form(request):
    return render_to_response('test1/search_form.html')

# 接收请求数据
def search(request):
    request.encoding = 'utf-8'
    text1 = int(request.GET['q'])
    text2 = int(request.GET['a'])
    sym = request.GET['s']

    def add(x, y):
        return x + y
    def subtract(x, y):
        return x - y
    def multiply(x, y):
        return x * y
    def divide(x, y):
        return x / y

    if sym == '+':
        add1 = str(add(text1, text2))
        message = '结果为: ' + add1
    elif sym == '-':
        sub1 = str(subtract(text1, text2))
        message = '结果为: ' + sub1
    elif sym == '*':
        mul1 = str(multiply(text1, text2))
        message = '结果为: ' + mul1
    elif sym == '/':
        div1 = str(divide(text1, text2))
        message = '结果为: ' + div1
    else:
        message = 'wrong'
    return HttpResponse(message)
