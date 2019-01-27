#coding:utf-8

# agent形式
# 1.采集资产
# 2.将资产数据发送到API（POST）

# SSH形式
# 1.获取今日未采集主机列表
# 2.采集资产
# 3.将资产数据发送到API(POST)

# Salt形式
# 1.获取今日未采集主机列表
# 2.采集资产
# 3.将资产数据发送到API（POST）


"""
思路：
agent和ssh、salt不一样的地方就是不需要向api去获取未采集的主机列表
相同点是需要采集资产，然后将资产数据发送到api
那么我们可以先写一个基类（这个基类只有三个类的共同的方法），让agent，ssh,salt都可以继承
再写一个基类，这个基类（这个类只有ssh,salt这两个类公共的方法），让ssh,salt去继承
"""

class BaseClient(object):
    def send_data(self, data_dict):
        pass

class Agent(BaseClient):
    def file_host(self):
        # 读取nid文件中的内容，文件中的内容是主机名
        # 设备第一次启动的时候就会把主机名写入nid文件
        # 这样就算用户在电脑上操作了修改设备名也没事，因为主机名已经写入了文件
        # 如果重装系统肯定会把文件给删了，那么如何解决这个问题呢？
        # 答：重装系统的时候也是通过cmdb来操作，在重装的时候我们已经知道需要重装的电脑的主机名是什么
        # 那么我们重装的时候就把这台电脑的主机名设备为原来写入在文件中的主机名
        f = open("nid")
        data = f.read()
        f.close()
        if data:
            return data

    def process(self):
        # 1.采集资产信息
        from .plugins import pack
        data_dict = pack()
        hostname = self.file_host()
        if hostname:
            data_dict["hostname"] = hostname
        else:
            # 获取当前主机名
            # 写入nid文件
            data_dict['hostname'] = "asdfasdf"
        # 2.将资产数据发送到API(POST)
        self.send_data(data_dict)

class SBaseClient(BaseClient):
    # 获取今日未采集主机列表
    def get_host(self):
        pass

class SSH(SBaseClient):
    def process(self):
    # 1.获取今日未采集主机列表
        host_list = self.get_host()
        for host in host_list:
            # 2.采集资产
            data_dict = {}
            # 3.将资产数据发送到API（POST）
            self.send_data(data_dict)

class Salt(SBaseClient):

    def process(self):
        # 1.获取今日未采集主机列表
        host_list = self.get_host()
        for host in host_list:
            # 2.采集资产
            data_dict = {}
            # 3.将资产数据发送到API（POST）
            self.send_data(data_dict)
