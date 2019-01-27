# 只放置可执行文件
# from src.scripts import client
#
# if __name__ == '__main__':
#     client()

# 导入一个py文件时
# from src.plugins import disk
# 加载文件夹下的disk.py文件
# 加载就是把disk.py文件执行一遍放在内存中

# 导入文件夹(包，模块，类库)
from src import plugins
# 我们这里导入了plugins，那么就会把plugins中的__init__文件都执行一遍，放在内存中
# 用这种模式的好处就是把功能都封装在了plugins中
# 加载文件夹下的init.py文件
# 导入plugins的时候，会默认导入__init__文件，而且只导入这个一个文件
data_dict = plugins.pack()