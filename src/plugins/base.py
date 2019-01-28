from conf import settings

class BasePlugin(object):

    def __init__(self):
        self.test_mode = settings.TEST_MODE
        self.mode_list = ["SSH", "Salt", "Agent"]
        if settings.MODE in self.mode_list:
            self.mode = settings.MODE
        else:
            raise Exception("配置文件错误")

    def ssh(self, cmd):
        import paramiko

        private_key = paramiko.RSAKey.from_private_key_file(settings.SSH_PRIVATE_KEY)
        ssh = paramiko.SSHClient()
        ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy)
        ssh.connect(hostname=self.hostname, port=settings.SSH_PORT, username=settings.SSH_USER, pkey=private_key)
        stdin, stdout, stderr = ssh.exec_command(cmd)
        result = stdout.read()
        ssh.close()
        return result

    def agent(self, cmd):
        import subprocess
        output = subprocess.Popen([cmd], stdout=subprocess.PIPE, shell=True).communicate()
        return output[0]

    def salt(self, cmd):
        pass

    def shell_cmd(self, cmd):
        if self.mode not in self.mode_list:
            raise Exception("settings.mode must be one of ['agent', 'salt', 'ssh']")
        # 根据函数名(func_name)，获得函数对象
        func = getattr(self, self.mode.lower())
        output = func(cmd)
        return output
        # if self.mode == "SSH":
        #     ret = self.ssh(cmd)
        # elif self.mode == "Salt":
        #     ret = self.salt(cmd)
        # else:
        #     ret = self.agent(cmd)
        # return ret

    def execute(self):
        ret = self.shell_cmd("查看平台命令")
        if ret == "linux":
            return self.linux()

        elif ret == "windows":
            return self.windows()

        else:
            raise Exception("只支持windows和Linux")

    def linux(self):
        raise Exception("......")

    def windows(self):
        raise Exception("......")
