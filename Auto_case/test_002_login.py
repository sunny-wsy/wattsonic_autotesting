# encoding='utf-8'
import pytest
import os,sys
#将工程目录添加到sys.path中
sys_path = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
sys.path.append(sys_path)
from API_autotesting.CommonModules import get_info,http_requests,yaml_util
info=get_info.Get_info()
request=http_requests.HttpRequest_v1()
yaml_read=yaml_util.YamlUtil()
path='/data.yaml'
url=yaml_read.read_test_yaml(path)['base']['url']
# username=yaml_read.read_test_yaml(path)['base']['username2']
# password=yaml_read.read_test_yaml(path)['base']['password2']
#获取headers
headers1=info.get_headers('login',path)[0]
cache={}
# headers2=info.login(url,username,password)
class Test_002_login(object):
    #登录
    urlxdata1=info.get_urlx_headers_data('login',path)
    @pytest.mark.parametrize("urlx,data,headers",urlxdata1)
    @pytest.mark.run(order=1)
    def test_login(self,urlx,data,headers):
        res=request.requests_post_data(url,urlx,data,headers1)
        accessToken=res['data']['accessToken']
        cache['Access-Token']=accessToken
        # params = ['createTime', 'updateTime', 'status', 'staffCode', 'id', 'mcid', 'muid']
        # for i in params:
        #     assert i in res.text
    #查询当前用户
    urlx2=info.get_urlx('user_current',path)
    @pytest.mark.parametrize('urlx',urlx2)
    @pytest.mark.run(order=2)
    def test_user_current(self,urlx):
        headers1['Access-Token']=cache['Access-Token']
        request.requests_get(url,urlx,headers1)
    # #修改当前用户密码，密码的旧密码和新密码不能相同，所以该接口可能无法进行自动化。
    # urlx_data3=info.get_urlxdata('password',path)
    # print(urlx_data3)
    # @pytest.mark.parametrize('urlx,data',urlx_data3)
    # @pytest.mark.run(order=3)
    # def test_password(self,urlx,data):
    #     request.requests_put_data(url,urlx,data,headers2)
#执行接口
if __name__ == '__main__':
    pytest.main(['-s', 'test_002_login.py'])