from django.shortcuts import render,HttpResponse
import json
from apiauth import auth
from django.views.decorators.csrf import csrf_exempt,csrf_protect
from django.views import View


class Host_api(View):
    @csrf_exempt							# 不使用csrf验证
    def dispatch(self, request, *args, **kwargs):
        print('before')
        result = super(Host_api,self).dispatch(request, *args, **kwargs)
        print('after')
        return result

    @auth.apiauth
    def get(self,request):
        # 查询函数
        data = {'a':'abc','b':'123'}
        return HttpResponse(json.dumps({'status': 'ok'}))

    @auth.apiauth
    def post(self,request):
        # 添加函数
        print(request.method)
        print(request.GET.get('name'))
        return HttpResponse(json.dumps({'status': 'ok'}))


    @auth.apiauth
    def delete(self,request):
        # 删除函数
        print(request.method)
        print(request.GET.get('name'))
        return HttpResponse(json.dumps({'status': 'ok'}))

    @auth.apiauth
    def put(self,request):
        # 更新函数
        print(request.method)
        print(request.GET.get('name'))
        return HttpResponse(json.dumps({'status':'ok'}))

