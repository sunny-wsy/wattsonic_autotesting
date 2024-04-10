# encoding='utf-8'
import pytest
import random,sys,os
#将工程目录添加到sys.path中
sys_path = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
sys.path.append(sys_path)
from API_autotesting.CommonModules import get_info,http_requests,yaml_util,conn_database
# from A_Wattsonic.API_autotesting.Common import conn_database
from API_autotesting.CommonModules import *
# from API_autotesting.Common import conn_database
mysql=conn_database.Postsql()
info=get_info.Get_info()
request=http_requests.HttpRequest_v1()
yaml_read=yaml_util.YamlUtil()
path='/data.yaml'
url=yaml_read.read_test_yaml(path)['base']['url']
username=yaml_read.read_test_yaml(path)['base']['username']
password=yaml_read.read_test_yaml(path)['base']['password']
#获取headers
headers=info.login(url,username,password)
cache={}
class Test_001_register(object):
    #获取国家列表
    urlx1=info.get_urlx('countrylist',path)
    @pytest.mark.parametrize('urlx',urlx1)
    @pytest.mark.run(order=1)
    def test_countrylist(self,urlx):
        request.requests_get(url,urlx,headers)
    #根据公司Code查询公司
    urlx2=info.get_urlx('queryByCode',path)
    data2=info.get_data('queryByCode',path)
    urlxdata2=[(urlx2[0],str(data2))]
    print (urlxdata2)
    @pytest.mark.parametrize("urlx,params",urlxdata2)
    @pytest.mark.run(order=2)
    def test_queryByCode(self,urlx,params):
        request.requests_get_params(url,urlx,params,headers)
    #组织注册
    urlx3=info.get_urlx('companyregister',path)
    data3=info.get_data('companyregister',path)
    #公司名称和email不可以重复
    companyName='company_test'+str(random.randint(0,1000))
    cache['companyName']=companyName
    email='test_email'+str(random.randint(0,1000))+'@163.com'
    cache['email1']=email
    data3['companyName']=companyName
    data3['email']=email
    urlxdata3=[]
    urlxdata3.append((urlx3[0],data3))
    @pytest.mark.parametrize("urlx,data",urlxdata3)
    @pytest.mark.run(order=3)
    def test_companyregister(self,urlx,data):
        request.requests_post_data(url,urlx,data,headers)
    # #用户注册,目前页面无该功能，废弃
    # urlx4=info.get_urlx('userregister',path)
    # data4=info.get_data('userregister',path)
    # #email不可以重复
    # email='testuser_email'+str(random.randint(0,1000))+'@163.com'
    # cache['email2']=email
    # cache['password']=data4['password']
    # # print (cache)
    # data4['email']=email
    # urlxdata4=[]
    # urlxdata4.append((urlx4[0],data4))
    # @pytest.mark.parametrize("urlx,data",urlxdata4)
    # @pytest.mark.run(order=4)
    # def test_userregister(self,urlx,data):
    #     request.requests_post_data(url,urlx,data,headers)
    #终端用户注册
    urlx4=info.get_urlx('enduserregister',path)
    data4=info.get_data('enduserregister',path)
    #email不可以重复
    email='testuser_email'+str(random.randint(0,1000))+'@163.com'
    cache['email2']=email
    cache['password']=data4['password']
    # print (cache)
    data4['email']=email
    urlxdata4=[]
    urlxdata4.append((urlx4[0],data4))
    @pytest.mark.parametrize("urlx,data",urlxdata4)
    @pytest.mark.run(order=4)
    def test_userregister(self,urlx,data):
        request.requests_post_data(url,urlx,data,headers)
    #删除已经注册的公司和账号
    @pytest.mark.run(order=5)
    def test_deletedata(self):
        email1=cache['email1']
        email2=cache['email2']
        companyName=cache['companyName']
        sql1="delete from t_user where email='%s'"%email1
        sql2="delete from t_user where email='%s'"%email2
        sql3="delete from t_company  where company_name='%s'"%companyName
        mysql.delete(sql1)
        mysql.delete(sql2)
        mysql.delete(sql3)
#执行接口
if __name__ == '__main__':
    pytest.main(['-s', 'test_001_register.py'])