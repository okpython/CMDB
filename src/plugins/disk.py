from .base import BasePlugin
import os
import re
import traceback
from .base import BasePlugin
from  lib.response import BaseResponse

class DiskPlugin(BasePlugin):

    def windows(self):
        output = self.shell_cmd("ipconfig")
        return output

    def linux(self):
        response = BaseResponse()
        try:
            # 如果是测试模式的话，就读取我们事先写好在文件中的数据
            if self.test_mode:

                output = self.shell_cmd("ipconfig")
                return output
        except Exception as e:
            pass
        return