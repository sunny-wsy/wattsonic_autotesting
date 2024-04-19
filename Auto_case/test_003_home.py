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
username=yaml_read.read_test_yaml(path)['base']['username']
password=yaml_read.read_test_yaml(path)['base']['password']
# url='http://121.40.203.12:8888'
# username="lyy@wattsonic.com"
# password="Wattsonic"
# path='\data.yaml'
#获取headers
headers=info.login(url,username,password)
print (headers)
#0，为uct，utc+8为480，utc-8为-480
class Test_003_home(object):
    #公司电站数量统计（总数量/离线数量/警告数量）
    # def test_plant_number(self):
    #     urlx='/v2/plant/statistics'
    #     request.requests_get(url,urlx,headers)
    # urlx1=[]
    # urlx1.append(yaml_read.read_test_yaml(path)['plant_number']['request']['url'])
    urlx1=info.get_urlx('plant_number',path)
    @pytest.mark.parametrize('urlx',urlx1)
    @pytest.mark.run(order=1)
    def test_plant_number(self,urlx):
        request.requests_get(url,urlx,headers)
    #开启的工单
    urlx2=info.get_urlx('wokerorder_number',path)
    @pytest.mark.parametrize('urlx',urlx2)
    @pytest.mark.run(order=2)
    def test_wokerorder_number(self,urlx):
        request.requests_get(url,urlx,headers)
    #公司电站总放电量ESG数据
    urlx3=info.get_urlx('ESG',path)
    @pytest.mark.parametrize('urlx',urlx3)
    @pytest.mark.run(order=3)
    def test_ESG(self,urlx):
        request.requests_get(url,urlx,headers)
    #公司电站最近n天日增数量（包括今天）
    urlxdata4=info.get_urlxdata('daily_grow',path)
    @pytest.mark.parametrize("urlx,data",urlxdata4)
    @pytest.mark.run(order=4)
    def test_dailygrow(self,urlx,data):
        request.requests_get_data(url,urlx,data,headers)
    #统计外部型号的占比
    urlxdata5=info.get_urlxdata('topProducts',path)
    @pytest.mark.parametrize("urlx,data",urlxdata5)
    @pytest.mark.run(order=5)
    def test_topProducts(self,urlx,data):
        request.requests_get_data(url,urlx,data,headers)
    #统计经销商对应电站数量排行
    urlxdata6=info.get_urlxdata('topDistributors',path)
    @pytest.mark.parametrize("urlx,data",urlxdata6)
    @pytest.mark.run(order=6)
    def test_topDistributors(self,urlx,data):
        request.requests_get_data(url,urlx,data,headers)
    #统计经销商对应电站装机容量排行
    urlxdata7=info.get_urlxdata('topPlants',path)
    @pytest.mark.parametrize("urlx,data",urlxdata7)
    @pytest.mark.run(order=7)
    def test_topPlants(self,urlx,data):
        request.requests_get_data(url,urlx,data,headers)
    #首页查询地球上电站坐标接口
    urlx8=info.get_urlx('maplist',path)
    @pytest.mark.parametrize('urlx',urlx8)
    @pytest.mark.run(order=8)
    def test_maplist(self,urlx):
        request.requests_get(url,urlx,headers)
    #首页搜索提示
    urlxdata9=info.get_urlxdata('searchtips',path)
    @pytest.mark.parametrize("urlx,data",urlxdata9)
    @pytest.mark.run(order=9)
    def test_searchtips(self,urlx,data):
        request.requests_get_data(url,urlx,data,headers)
#执行接口
if __name__ == '__main__':
    pytest.main(['-s', 'test_003_home.py'])