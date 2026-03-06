# -*- encoding=utf8 -*-
__author__ = "yuanyuanjiang"
__title__  = "设备信息"


from airtest.core.api import *
from airtest.report.report import LogToHtml
from airtest.report.report import simple_report
from poco.drivers.unity3d import UnityPoco
from airtest.core.assertions import *
import traceback


path_file = os.path.dirname(os.path.abspath(__file__))
auto_setup(__file__,logdir=True,devices=["android://127.0.0.1:5037/222bfc1f"])


def contains(a, b):
    return b in a

# connect_device("Android://127.0.0.1:5037/47260DLAQ00445")
start_app("com.msdk.deltafinder")
sleep(3)

#获取did和aid接口

width = G.DEVICE.display_info['width']
height = G.DEVICE.display_info['height']
x=0.75*width
y=0.92*height
touch([x,y])
sleep(5)



#点击初始化
try:
    touch(Template(r"tpl1770620990572.png", record_pos=(-0.094, -0.787), resolution=(1080, 2400)))

    #     poco(text="初始化日志").click()
    # poco("Main Camera").offspring("InitLog").offspring("TitleText").click()
    sleep(2)
    poco = UnityPoco()
    poco("Main Camera").offspring("InitMSDKBtn").click()
    sleep(2)
    touch(Template(r"tpl1766999479423.png", record_pos=(-0.429, -0.74), resolution=(700, 1120)))
    # poco("Main Camera").offspring("leftBtn").focus([0.3, 1.0]).click()
    sleep(2)


    #账号服务——获取账号
    poco(text="账号服务").click()
    poco(text="获取 Account ID").focus([0.5,0.8]).click()
    res = poco("bottomLayer").offspring("Viewport").child("Content").get_text()
    res_suc = "resultCode = 0"
    assert_equal(contains(res,res_suc),True, "获取账号成功.")
    sleep(2)


    # 获取用户信息
    poco(text="清除").focus([0.5, 0.8]).click()
    poco(text="获取用户信息").focus([0.5, 0.8]).click()
    res = poco("bottomLayer").offspring("Viewport").child("Content").get_text()
    res_suc = "code = 0"
    assert_equal(contains(res,res_suc),True, "获取账号详情成功.")
    sleep(2)

    #重置账号
    poco(text="清除").focus([0.5, 0.8]).click()
    poco(text="账号重置").focus([0.5, 0.8]).click()
    res = poco("bottomLayer").offspring("Viewport").child("Content").get_text()
    res_suc = "resultCode = 0"
    assert_equal(contains(res,res_suc),True, "获取账号详情成功.")
    sleep(2)


    #账号注销
    poco(text="账号注销相关").focus([0.5, 0.8]).click()
    assert_equal(poco("bindState").get_text(), "未注销", "账号为未注销状态")
    poco(text="注销账号").click()
    poco(text="确认").focus([0.5, 0.8]).click()
    sleep(2)
    assert_equal(poco("bindState").get_text(), "冷静期", "账号为冷静期状态")
    poco(text="取消注销").click()
    poco(text="确认").focus([0.5, 0.8]).click()
    sleep(2)
    assert_equal(poco("bindState").get_text(), "未注销", "账号为未注销状态")
except Exception as e:
    log(e, snapshot=True)

finally:
    #生成测试报告
    h1 = LogToHtml(script_root=path_file, log_root=path_file + "\\" + "log",
                   export_dir=r"D:\test", logfile=path_file + "\log\log.txt", lang='en',                            plugins=["poco.utils.airtest.report","airtest_selenium.report"])
    h1.report()
    stop_app("com.msdk.deltafinder")



