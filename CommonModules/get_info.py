import requests,random
import os,sys
#将工程目录添加到sys.path中
sys_path = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
sys.path.append(sys_path)
from API_autotesting.CommonModules import yaml_util
yaml_read=yaml_util.YamlUtil()
class Get_info(object):
    def login(self,url,username,password):
        url1=url+'/login'
        data={"password": password, "username":username }
        headers2={'Accept-Language':'en-us','Platform':'web'}
        res=requests.post(url1,json=data,headers=headers2)
        print (res.json())
        token=res.json()['data']['accessToken']
        headers={"Access-Token":token,'Platform':'web','Accept-Language':'en-us'}
        # print (headers)
        return headers
    def get_urlx(self,name,path):
        urlx=[]
        urlx.append(yaml_read.read_test_yaml(path)[name]['request']['url'])
        return urlx
    def get_headers(self,name,path):
        urlx=[]
        urlx.append(yaml_read.read_test_yaml(path)[name]['request']['headers'])
        return urlx
    def get_data(self,name,path):
        data=yaml_read.read_test_yaml(path)[name]['request']['data']
        return data
    def get_urlxdata(self,name,path):
        urlx=[]
        value=((yaml_read.read_test_yaml(path)[name]['request']['url']),((yaml_read.read_test_yaml(path)[name]['request']['data'])))
        urlx.append(value)
        return urlx
    def get_urlx_headers_data(self,name,path):
        urlx=[]
        value=((yaml_read.read_test_yaml(path)[name]['request']['url']),(yaml_read.read_test_yaml(path)[name]['request']['data']),(yaml_read.read_test_yaml(path)[name]['request']['headers']))
        urlx.append(value)
        return urlx
# urlxdata1=info.get_data('login',path)
# urlxdata1=Get_info().get_urlxdata('queryByCode','/data.yaml')
# print ((urlxdata1))
# urlx3=Get_info().get_urlx('companyregister','/data.yaml')
# data3=Get_info().get_data('companyregister','/data.yaml')
# print (data3)
# company_name='company_test'+str(random.randint(0,1000))
# email='test_email'+str(random.randint(0,1000))+'@163.com'
# data3['company_name']=company_name
# data3['email']=email
# print (data3)
# urlx3.append(data3)
# print (urlx3)
# urlxdata3=[]
# urlxdata3.append((urlx3[0],data3))
# print (urlxdata3)
# url='http://121.40.203.12:8888'
# # urlx='/v2/plant/statistics'
# username="lyy@wattsonic.com"
# password="Wattsonic"
# Get_headers().login(url,username,password)