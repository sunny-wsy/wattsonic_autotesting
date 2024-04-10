import requests
from requests.sessions import Session
# class HttpRequest_v1(object):
#     """直接发请求不记录cookies信息"""
#     def request(self, method, url, data=None, headers=None, cookies=None, json=None):
#         method = method.lower()
#         if method == 'post':
#             if json:  # 判断传参方式是否为json
#                 res = requests.post(url=url, json=json, headers=headers, cookies=cookies)
#                 return res
#             else:
#                 res = requests.post(url=url, data=data, headers=headers, cookies=cookies)
#                 return res
#         elif method == 'get':
#             res = requests.get(url=url, params=data, headers=headers, cookies=cookies)
#             return res
#         elif method == 'delete':
#             res = requests.delete(url=url, params=data, headers=headers, cookies=cookies)
#             return res
#         elif method == 'put':
#             if json:  # 判断传参方式是否为json
#                 res = requests.put(url=url, json=json, headers=headers, cookies=cookies)
#                 return res
#             else:
#                 res = requests.put(url=url, data=data, headers=headers, cookies=cookies)
#                 return res
#
#
# class HttpRequest_v2(object):
#     """利用Session对象来记录cookies信息"""
#
#     def __init__(self):
#         """
#         初始化创建Session对象
#         """
#         self.re = Session()
#
#     def request(self, method, url, data=None, headers=None, cookies=None, json=None):
#         if method == 'post':
#             if json:
#                 res = self.re.post(url=url, json=json, headers=headers, cookies=cookies)
#                 return res
#             else:
#                 res = self.re.post(url=url, data=data, headers=headers, cookies=cookies)
#                 return res
#         elif method == 'get':
#             res = self.re.get(url=url, params=data, headers=headers, cookies=cookies)
#             return res
#         elif method == 'delete':
#             res = self.re.delete(url=url, params=data, headers=headers, cookies=cookies)
#             return res
#         elif method == 'put':
#             if json:  # 判断传参方式是否为json
#                 res = self.re.put(url=url, json=json, headers=headers, cookies=cookies)
#                 return res
#             else:
#                 res = self.re.put(url=url, data=data, headers=headers, cookies=cookies)
#                 return res
#
#     def close(self):
#         """
#         关闭初始化时的Session对象
#         """
#         self.re.close()
class HttpRequest_v1(object):
    def requests_post_data(self,url,urlx,data,headers):
        url2=url+urlx
        print (url2)
        res=requests.post(url2,json=data,headers=headers)
        print (res.status_code)
        print (res.json())
        return res.json()
    # def requests_post(self,url,urlx,data):
    #     url2=url+urlx
    #     print (url2)
    #     res=requests.post(url2,json=data)
    #     print (res.status_code)
    #     print (res.json())
    def requests_get(self,url,urlx,headers):
        url2=url+urlx
        print (url2)
        res=requests.get(url2,headers=headers)
        print (res.status_code)
        print (res.json())
    def requests_get_params(self,url,urlx,params,headers):
        url2=url+urlx+params
        print (url2)
        res=requests.get(url2,headers=headers)
        print (res.status_code)
        print (res.json())
    def requests_get_data(self,url,urlx,data,headers):
        url2=url+urlx
        print (url2)
        res=requests.get(url2,params=data,headers=headers)
        print (res.status_code)
        print (res.json())
    def requests_get_json(self,url,urlx,data,headers):
        url2=url+urlx
        print (url2)
        res=requests.get(url2,json=data,headers=headers)
        print (res.status_code)
        print (res.json())
    def requests_put_data(self,url,urlx,data,headers):
        url2=url+urlx
        print (url2)
        res=requests.put(url2,json=data,headers=headers)
        print (res.status_code)
        print (res.json())
    def requests_put_params(self,url,urlx,params,headers):
        url2=url+urlx+params
        print (url2)
        res=requests.put(url2,headers=headers)
        print (res.status_code)
        print (res.json())

# a=HttpRequest_v1()
# url='http://121.40.203.12:8888'
# urlx='/v2/plant/statistics'
# username="lyy@wattsonic.com"
# password="Wattsonic"
# def login():
#     url1=url+'/login'
#     # print (url1)L
#     data={"password": password, "username":username }
#     headers={'Accept-Language':'en-us','Platform':'web'}
#     res=requests.post(url1,json=data,headers=headers)
#     print (res.json())
#     token=res.json()['data']['accessToken']
#     return token
# token=login()
# headers={"Access-Token":token,'Platform':'web','Accept-Language':'en-us'}
# # headers={"Access-Token":"eyJhbGciOiJIUzI1NiJ9.eyJzdWIiOiIxNjk1OTgyODQ0ODk2NzU5ODA5IiwiYXVkIjoid2ViIiwiZXhwIjoxNzAwNzk0MzM2fQ._haTfq1UPp6IRX-I5pSvWL0S37V-z4EYS_Gxf1T6BbM",'Platform':'web','Accept-Language':'en-us'}
# print (headers)
# a.requests_get(url,urlx,headers)
