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
# print(yaml_read.read_test_yaml(path))
import pytest
class Test_read(object):
    @pytest.mark.parametrize("args",yaml_read.read_test_yaml(path))
    def test_add_article(self,args):
        print(args)
if __name__ == '__main__':
    # pytest.main(["-vs", Read.py::test])
    # Test_read().test_add_article()
    pytest.main(['-s', 'test.py'])
    # pytest.main(['-s', 'test.py::Test_read::test_add_article'])

