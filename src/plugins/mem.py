from .base import BasePlugin

class MemPlugin(BasePlugin):

    def windows(self):
        output = self.shell_cmd("asdf")
        # 一般不会直接让我们输出没有处理过的数据，这里我们采用正则表达式来提取数据
        return output

    def linux(self):
        output = self.shell_cmd("asdf")
        return output