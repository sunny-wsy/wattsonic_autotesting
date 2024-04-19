# encoding='utf-8'
import pytest
import random,sys,os,json
import time
#将工程目录添加到sys.path中
sys_path = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
sys.path.append(sys_path)
from API_autotesting.CommonModules import get_info,http_requests,yaml_util
info=get_info.Get_info()
request=http_requests.HttpRequest_v1()
sslcurl=http_requests.SshCurl_v1()
yaml_read=yaml_util.YamlUtil()
path='/data.yaml'
url=yaml_read.read_test_yaml(path)['base']['url']
username=yaml_read.read_test_yaml(path)['base']['username']
password=yaml_read.read_test_yaml(path)['base']['password']
#获取headers
headers=info.login(url,username,password)
cache={}
class Test_004_plant(object):
    # #时区列表
    # urlx1=info.get_urlx('timezone',path)
    # @pytest.mark.parametrize('urlx',urlx1)
    # @pytest.mark.run(order=1)
    # def test_timezonelist(self,urlx):
    #     request.requests_get(url,urlx,headers)
    #创建电站，不绑定设备，货币默认，绑定已有终端用户
    urlx1=info.get_urlx('creatplant1',path)
    data1=info.get_data('creatplant1',path)
    #电站名称不可以重复
    plantName='plant_test'+str(random.randint(0,1000))
    data1['plantName']=plantName
    urlxdata1=[]
    urlxdata1.append((urlx1[0],data1))
    @pytest.mark.parametrize("urlx,data",urlxdata1)
    @pytest.mark.run(order=1)
    def test_creatplant1(self,urlx,data):
        res=request.requests_post_data(url,urlx,data,headers)
        cache['plant_id']=res['data']
    #导入设备-二代低压，且位数为12位
    urlx1=info.get_urlx('importproduct1',path)
    data1=info.get_data('importproduct1',path)
    #sn不可以重复
    devicesn='dev_test'+str(random.randint(1000,9999))
    productSnList= [
        {
            "innerSn": devicesn,
            "outerSn": devicesn
        }]
    cache['device_batsn1']=devicesn
    data1['productSnList']=productSnList
    urlxdata1=[]
    urlxdata1.append((urlx1[0],data1))
    @pytest.mark.parametrize("urlx,data",urlxdata1)
    @pytest.mark.run(order=2)
    def test_importproduct1(self,urlx,data):
        request.requests_post_data(url,urlx,data,headers)
    #导入设备-热水器
    urlx1=info.get_urlx('importproduct2',path)
    data1=info.get_data('importproduct2',path)
    #sn不可以重复
    devicesn='wattmate_test'+str(random.randint(1000,9999))
    productSnList= [
        {
            "innerSn": devicesn,
            "outerSn": devicesn
        }]
    cache['devicesn_wat']=devicesn
    data1['productSnList']=productSnList
    urlxdata1=[]
    urlxdata1.append((urlx1[0],data1))
    @pytest.mark.parametrize("urlx,data",urlxdata1)
    @pytest.mark.run(order=3)
    def test_importproduct2(self,urlx,data):
        request.requests_post_data(url,urlx,data,headers)
    #导入设备-二代高压
    #导入设备-三代锐能
    #设备上报,二代低压
    urlx1=yaml_read.read_test_yaml(path)['gatewaybat1']['request']['url']
    hostname=yaml_read.read_test_yaml(path)['gatewaybat1']['request']['hostname']
    username1=yaml_read.read_test_yaml(path)['gatewaybat1']['request']['username']
    password1=yaml_read.read_test_yaml(path)['gatewaybat1']['request']['password']
    data1=info.get_data('gatewaybat1',path)
    bauSn=cache['device_batsn1']
    #iotsn不可以重复
    iotSn='iot'+bauSn
    data1['iotSn']=iotSn
    data1['bauSn']=bauSn
    data1['bcuInfoList'][0]['bcuSn']=bauSn
    timestamp=int(time.time())*1000
    data1['timestamp']=timestamp
    command='curl -X POST -H "Content-Type:application/json"  -d '+"'"+json.dumps(data1)+"'"+' '+urlx1
    # command='''curl -X POST -d '{"timestamp": 1711594159707, "wattMateSn": "WMT0328001", "zoneId": "Asia/Shanghai", "softwareVersion": "V1.2.3", "maxPower": 9000, "maxGridPower": 5000, "currentPower": 2000, "heatingCoefK": 2.88, "elecUsage24h": 1888, "injection": 1500, "purchase": 1000, "supportModeList": [0, 1, 2], "currentMode": 0, "timeMode": 0, "maxTemp": 650, "allDayTargetTemp": 450, "initStatus": 0, "light1Status": 0, "light2Status": 0, "light3Status": 0, "light4Status": 0, "light5Status": 0, "emsComStatus": 0, "meterComStatus": 0, "pcsComStatus": 0, "gridAccessStatus": 0, "pcsAccessStatus": 0, "workStatus": 0, "heaterInfoList": [{"type": 1, "targetTemp": 400, "currentPower": 1200, "currentTemp": 380, "elecUsage24h": 180, "workStatus": 0}], "planList": [{"endTime": 0, "startTime": 60, "targetTemp": 30}, {"endTime": 120, "targetTemp": 180, "startTime": 40}, {"targetTemp": 240, "startTime": 320, "endTime": 50}, {"targetTemp": 0, "endTime": 0, "startTime": 0}, {"endTime": 0, "startTime": 0, "targetTemp": 0}]}' http://172.18.30.87:8888/gateway/wattmate'''
    urlxdata1=[]
    urlxdata1.append((hostname,username1,password1,command))
    @pytest.mark.parametrize("hostname,username,password,command",urlxdata1)
    @pytest.mark.run(order=4)
    def test_gatewayproduct1(self,hostname,username,password,command):
        sslcurl.ssh_execute_command(hostname,username,password,command)
    #设备上报,热水器
    urlx1=yaml_read.read_test_yaml(path)['gatewaywat']['request']['url']
    hostname=yaml_read.read_test_yaml(path)['gatewaywat']['request']['hostname']
    username1=yaml_read.read_test_yaml(path)['gatewaywat']['request']['username']
    password1=yaml_read.read_test_yaml(path)['gatewaywat']['request']['password']
    data1=info.get_data('gatewaywat',path)
    wattMateSn=cache['devicesn_wat']
    data1['wattMateSn']=wattMateSn
    timestamp=int(time.time())*1000
    data1['timestamp']=timestamp
    command='curl -X POST -H "Content-Type:application/json"  -d '+"'"+json.dumps(data1)+"'"+' '+urlx1
    urlxdata1=[]
    urlxdata1.append((hostname,username1,password1,command))
    @pytest.mark.parametrize("hostname,username,password,command",urlxdata1)
    @pytest.mark.run(order=5)
    def test_gatewayproduct2(self,hostname,username,password,command):
        sslcurl.ssh_execute_command(hostname,username,password,command)
    #查询子系统所有产品的序列号和型号，获取subSysId,获取二代低压的subSysId,
    urlx1=info.get_urlx('subSys',path)
    productSn=cache['device_batsn1']
    urlx2=urlx1[0]+'/'+productSn
    urlx3=[]
    urlx3.append(urlx2)
    @pytest.mark.parametrize("urlx",urlx3)
    @pytest.mark.run(order=6)
    def test_subSysIdbat1(self,urlx):
        res=request.requests_get(url,urlx,headers)
        cache['subSysId_bat1']=res['data']['subSysId']
        # print (cache)
    #查询子系统所有产品的序列号和型号，获取subSysId,获取热水器subSysId
    urlx1=info.get_urlx('subSys',path)
    productSn=cache['devicesn_wat']
    urlx2=urlx1[0]+'/'+productSn
    urlx3=[]
    urlx3.append(urlx2)
    @pytest.mark.parametrize("urlx",urlx3)
    @pytest.mark.run(order=7)
    def test_subSysIdwat(self,urlx):
        res=request.requests_get(url,urlx,headers)
        cache['subSysId_wat']=res['data']['subSysId']
        # print (cache)
    #绑定设备，创建电站中绑定,绑定二代低压
    urlx1=info.get_urlx('creatplant2',path)
    data1=info.get_data('creatplant2',path)
    #电站名称不可以重复
    plantName='plant_test'+str(random.randint(0,1000))
    data1['plantName']=plantName
    outerSn=cache['device_batsn1']
    subSysParams=[{"outerSn":outerSn,"subSysName":"设备","checkCode":"123456"}]
    data1['subSysParams']=subSysParams
    urlxdata1=[]
    urlxdata1.append((urlx1[0],data1))
    @pytest.mark.parametrize("urlx,data",urlxdata1)
    @pytest.mark.run(order=8)
    def test_creatplant2(self,urlx,data):
        subSysId=cache['subSysId_bat1']
        data['subSysParams'][0]['subSysId']=subSysId
        request.requests_post_data(url,urlx,data,headers)
    #绑定设备，在已经创建的电站中绑定
    urlx1=info.get_urlx('subSysbindPlant',path)
    data1=info.get_data('subSysbindPlant',path)
    urlxdata1=[]
    urlxdata1.append((urlx1[0],data1))
    @pytest.mark.parametrize('urlx,data',urlxdata1)
    @pytest.mark.run(order=9)
    def test_subSysbindPlant(self,urlx,data):
        plantId=cache['plant_id']
        outerSn=cache['devicesn_wat']
        subSysIds=cache['subSysId_wat']
        data['plantId']=plantId
        data['subSysParams'][0]['outerSn']=outerSn
        data['subSysParams'][0]['subSysId']=subSysIds
        request.requests_put_data(url,urlx,data,headers)
    #解绑设备，与电站解绑

    #产品喝子系统的关系


    #删除设备
    #
#执行接口
if __name__ == '__main__':
    pytest.main(['-s', 'test_004_plant.py'])
    # pytest.main(['-s', 'test_004_plant.py::Test_004_plant::test_creatplant1'])
    # pytest.main(['-s', 'test_004_plant.py::Test_004_plant::test_importproduct1','test_004_plant.py::Test_004_plant::test_gatewayproduct1','test_004_plant.py::Test_004_plant::test_subSysIdbat1','test_004_plant.py::Test_004_plant::test_creatplant2'])
    # pytest.main(['-s', 'te    # pytest.main(['-s','test_004_plant.py::Test_004_plant::test_creatplant1' ,'test_004_plant.py::Test_004_plant::test_importproduct2','test_004_plant.py::Test_004_plant::test_gatewayproduct2','test_004_plant.py::Test_004_plant::test_subSysIdwat','test_004_plant.py::Test_004_plant::test_subSysbindPlant'])st_004_plant.py::Test_004_plant::test_importproduct1','test_004_plant.py::Test_004_plant::test_gatewayproduct1','test_004_plant.py::Test_004_plant::test_subSysIdbat1'])
