# import paramiko
# def ssh_execute_command(hostname, username, password, command):
#     ssh = paramiko.SSHClient()
#     ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())
#     ssh.connect(hostname, username=username, password=password)
#     stdin, stdout, stderr = ssh.exec_command(command)
#     output = stdout.read().decode()
#     error = stderr.read().decode()
#     ssh.close()
#     return output, error
# if __name__ == "__main__":
#     hostname = "120.26.192.77"
#     username = "root"
#     password = "Watts0nicqw12QW!@"
#     # command = '''curl -X GET  -H "Access-Token: eyJhbGciOiJIUzI1NiJ9.eyJzdWIiOiIxNjk1OTgyODQ0ODk2NzU5ODA5IiwiYXVkIjoid2ViIiwiZXhwIjoxNzEzMzE5NjQzfQ.FvcNu4Dwn1BVa5mjDyfcF6m-Tkmsvl3Hx5RD7jJLNAM" -H "Platform: web" -H "Accept-Language: en-us"  http://121.40.203.12:8888/workOrder/count?status=0'''
#     # command ='''curl -X POST  -H "Access-Token: eyJhbGciOiJIUzI1NiJ9.eyJzdWIiOiIxNjk1OTgyODQ0ODk2NzU5ODA5IiwiYXVkIjoid2ViIiwiZXhwIjoxNzEzMzE5NjQzfQ.FvcNu4Dwn1BVa5mjDyfcF6m-Tkmsvl3Hx5RD7jJLNAM" -H "Platform: web" -H "Accept-Language: en-us" -d '{"timestamp": 1711594159707, "wattMateSn": "WMT0328001", "zoneId": "Asia/Shanghai", "softwareVersion": "V1.2.3", "maxPower": 9000, "maxGridPower": 5000, "currentPower": 2000, "heatingCoefK": 2.88, "elecUsage24h": 1888, "injection": 1500, "purchase": 1000, "supportModeList": [0, 1, 2], "currentMode": 0, "timeMode": 0, "maxTemp": 650, "allDayTargetTemp": 450, "initStatus": 0, "light1Status": 0, "light2Status": 0, "light3Status": 0, "light4Status": 0, "light5Status": 0, "emsComStatus": 0, "meterComStatus": 0, "pcsComStatus": 0, "gridAccessStatus": 0, "pcsAccessStatus": 0, "workStatus": 0, "heaterInfoList": [{"type": 1, "targetTemp": 400, "currentPower": 1200, "currentTemp": 380, "elecUsage24h": 180, "workStatus": 0}], "planList": [{"endTime": 0, "startTime": 60, "targetTemp": 30}, {"endTime": 120, "targetTemp": 180, "startTime": 40}, {"targetTemp": 240, "startTime": 320, "endTime": 50}, {"targetTemp": 0, "endTime": 0, "startTime": 0}, {"endTime": 0, "startTime": 0, "targetTemp": 0}]}' http://172.18.30.87:8888/gateway/wattmate'''
#     # command = '''curl -X POST -d "{'timestamp': 1711594159707, 'wattMateSn': 'WMT0328001', 'zoneId': 'Asia/Shanghai', 'softwareVersion': 'V1.2.3', 'maxPower': 9000, 'maxGridPower': 5000, 'currentPower': 2000, 'heatingCoefK': 2.88, 'elecUsage24h': 1888, 'injection': 1500, 'purchase': 1000, 'supportModeList': [0, 1, 2], 'currentMode': 0, 'timeMode': 0, 'maxTemp': 650, 'allDayTargetTemp': 450, 'initStatus': 0, 'light1Status': 0, 'light2Status': 0, 'light3Status': 0, 'light4Status': 0, 'light5Status': 0, 'emsComStatus': 0, 'meterComStatus': 0, 'pcsComStatus': 0, 'gridAccessStatus': 0, 'pcsAccessStatus': 0, 'workStatus': 0, 'heaterInfoList': [{'type': 1, 'targetTemp': 400, 'currentPower': 1200, 'currentTemp': 380, 'elecUsage24h': 180, 'workStatus': 0}], 'planList': [{'endTime': 0, 'startTime': 60, 'targetTemp': 30}, {'endTime': 120, 'targetTemp': 180, 'startTime': 40}, {'targetTemp': 240, 'startTime': 320, 'endTime': 50}, {'targetTemp': 0, 'endTime': 0, 'startTime': 0}, {'endTime': 0, 'startTime': 0, 'targetTemp': 0}]}" http://172.18.30.87:8888/gateway/wattmate'''
#     command = '''curl -X POST -H "Content-Type:application/json"  -d '{"timestamp": 1711594159707, "wattMateSn": "wattmate_test2841", "zoneId": "Asia/Shanghai", "softwareVersion": "V1.2.3", "maxPower": 9000, "maxGridPower": 5000, "currentPower": 2000, "heatingCoefK": 2.88, "elecUsage24h": 1888, "injection": 1500, "purchase": 1000, "supportModeList": [0, 1, 2], "currentMode": 0, "timeMode": 0, "maxTemp": 650, "allDayTargetTemp": 450, "initStatus": 0, "light1Status": 0, "light2Status": 0, "light3Status": 0, "light4Status": 0, "light5Status": 0, "emsComStatus": 0, "meterComStatus": 0, "pcsComStatus": 0, "gridAccessStatus": 0, "pcsAccessStatus": 0, "workStatus": 0, "heaterInfoList": [{"type": 1, "targetTemp": 400, "currentPower": 1200, "currentTemp": 380, "elecUsage24h": 180, "workStatus": 0}], "planList": [{"endTime": 0, "startTime": 60, "targetTemp": 30}, {"endTime": 120, "targetTemp": 180, "startTime": 40}, {"targetTemp": 240, "startTime": 320, "endTime": 50}, {"targetTemp": 0, "endTime": 0, "startTime": 0}, {"endTime": 0, "startTime": 0, "targetTemp": 0}]}' http://172.18.30.87:8888/gateway/wattmate'''
#     output, error = ssh_execute_command(hostname, username, password, command)
#     if output:
#         print("命令执行结果：")
#         print(output)
#     if error:
#         print("命令执行错误：")
#         print(error)
import json
a={"plantName":"0417001","region":"AD","timezone":"Asia/Shanghai","address":"MXX6+46 台湾南投縣信義鄉人和村","longitude":120.960515,"latitude":23.69781,"plantPicture":"wattdesk/plant-pic.png","sex":2,"ownerName":"wer3423@#@","email":"jena98@163.com","password":"6289","installerId":"1703689154564096002","ownerType":1,"mobileSuffix":"6289","localCurrency":"CNY","gridPricePerKWh":0.5234,"subSysParams":[{"outerSn":"wattmate_test7440","subSysName":"设备","checkCode":"123456","subSysId":"1780424336515710977"}]}
b=json.dumps(a)
print(a)