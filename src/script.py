# coding:utf-8
# 采集资产：三种不同的形式

from conf import settings






class NicPlugin(BasePlugin):
    def windows(self):
        output = self.shell_cmd("asdf")
        return output

    def linux(self):
        output = self.shell_cmd("asdf")
        return output



















