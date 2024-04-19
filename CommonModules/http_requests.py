import requests
import paramiko
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
        return res.json()
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
class SshCurl_v1(object):
    def ssh_execute_command(self,hostname, username, password, command):
        ssh = paramiko.SSHClient()
        ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())
        ssh.connect(hostname, username=username, password=password)
        stdin, stdout, stderr = ssh.exec_command(command)
        output = stdout.read().decode()
        error = stderr.read().decode()
        print(output)
        ssh.close()
        return output, error
# if __name__ == "__main__":
#     hostname = "120.26.192.77"
#     username = "root"
#     password = "Watts0nicqw12QW!@"
#     # command = '''curl -X GET  -H "Access-Token: eyJhbGciOiJIUzI1NiJ9.eyJzdWIiOiIxNjk1OTgyODQ0ODk2NzU5ODA5IiwiYXVkIjoid2ViIiwiZXhwIjoxNzEzMzE5NjQzfQ.FvcNu4Dwn1BVa5mjDyfcF6m-Tkmsvl3Hx5RD7jJLNAM" -H "Platform: web" -H "Accept-Language: en-us"  http://121.40.203.12:8888/workOrder/count?status=0'''
#     # command ='''curl -X POST  -H "Access-Token: eyJhbGciOiJIUzI1NiJ9.eyJzdWIiOiIxNjk1OTgyODQ0ODk2NzU5ODA5IiwiYXVkIjoid2ViIiwiZXhwIjoxNzEzMzE5NjQzfQ.FvcNu4Dwn1BVa5mjDyfcF6m-Tkmsvl3Hx5RD7jJLNAM" -H "Platform: web" -H "Accept-Language: en-us" -d '{"timestamp": 1711594159707, "wattMateSn": "WMT0328001", "zoneId": "Asia/Shanghai", "softwareVersion": "V1.2.3", "maxPower": 9000, "maxGridPower": 5000, "currentPower": 2000, "heatingCoefK": 2.88, "elecUsage24h": 1888, "injection": 1500, "purchase": 1000, "supportModeList": [0, 1, 2], "currentMode": 0, "timeMode": 0, "maxTemp": 650, "allDayTargetTemp": 450, "initStatus": 0, "light1Status": 0, "light2Status": 0, "light3Status": 0, "light4Status": 0, "light5Status": 0, "emsComStatus": 0, "meterComStatus": 0, "pcsComStatus": 0, "gridAccessStatus": 0, "pcsAccessStatus": 0, "workStatus": 0, "heaterInfoList": [{"type": 1, "targetTemp": 400, "currentPower": 1200, "currentTemp": 380, "elecUsage24h": 180, "workStatus": 0}], "planList": [{"endTime": 0, "startTime": 60, "targetTemp": 30}, {"endTime": 120, "targetTemp": 180, "startTime": 40}, {"targetTemp": 240, "startTime": 320, "endTime": 50}, {"targetTemp": 0, "endTime": 0, "startTime": 0}, {"endTime": 0, "startTime": 0, "targetTemp": 0}]}' http://172.18.30.87:8888/gateway/wattmate'''
#     # command = '''curl -X POST -d "{'timestamp': 1711594159707, 'wattMateSn': 'WMT0328001', 'zoneId': 'Asia/Shanghai', 'softwareVersion': 'V1.2.3', 'maxPower': 9000, 'maxGridPower': 5000, 'currentPower': 2000, 'heatingCoefK': 2.88, 'elecUsage24h': 1888, 'injection': 1500, 'purchase': 1000, 'supportModeList': [0, 1, 2], 'currentMode': 0, 'timeMode': 0, 'maxTemp': 650, 'allDayTargetTemp': 450, 'initStatus': 0, 'light1Status': 0, 'light2Status': 0, 'light3Status': 0, 'light4Status': 0, 'light5Status': 0, 'emsComStatus': 0, 'meterComStatus': 0, 'pcsComStatus': 0, 'gridAccessStatus': 0, 'pcsAccessStatus': 0, 'workStatus': 0, 'heaterInfoList': [{'type': 1, 'targetTemp': 400, 'currentPower': 1200, 'currentTemp': 380, 'elecUsage24h': 180, 'workStatus': 0}], 'planList': [{'endTime': 0, 'startTime': 60, 'targetTemp': 30}, {'endTime': 120, 'targetTemp': 180, 'startTime': 40}, {'targetTemp': 240, 'startTime': 320, 'endTime': 50}, {'targetTemp': 0, 'endTime': 0, 'startTime': 0}, {'endTime': 0, 'startTime': 0, 'targetTemp': 0}]}" http://172.18.30.87:8888/gateway/wattmate'''
#     command = '''curl -X POST -H "Content-Type:application/json"  -d '{"timestamp": 1711594159707, "wattMateSn": "wattmate_test2841", "zoneId": "Asia/Shanghai", "softwareVersion": "V1.2.3", "maxPower": 9000, "maxGridPower": 5000, "currentPower": 2000, "heatingCoefK": 2.88, "elecUsage24h": 1888, "injection": 1500, "purchase": 1000, "supportModeList": [0, 1, 2], "currentMode": 0, "timeMode": 0, "maxTemp": 650, "allDayTargetTemp": 450, "initStatus": 0, "light1Status": 0, "light2Status": 0, "light3Status": 0, "light4Status": 0, "light5Status": 0, "emsComStatus": 0, "meterComStatus": 0, "pcsComStatus": 0, "gridAccessStatus": 0, "pcsAccessStatus": 0, "workStatus": 0, "heaterInfoList": [{"type": 1, "targetTemp": 400, "currentPower": 1200, "currentTemp": 380, "elecUsage24h": 180, "workStatus": 0}], "planList": [{"endTime": 0, "startTime": 60, "targetTemp": 30}, {"endTime": 120, "targetTemp": 180, "startTime": 40}, {"targetTemp": 240, "startTime": 320, "endTime": 50}, {"targetTemp": 0, "endTime": 0, "startTime": 0}, {"endTime": 0, "startTime": 0, "targetTemp": 0}]}' http://172.18.30.87:8888/gateway/wattmate'''
#     output, error = SshCurl_v1().ssh_execute_command(hostname, username, password, command)
#     if output:
#         print("命令执行结果：")
#         print(output)
#     if error:
#         print("命令执行错误：")
#         print(error)


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
