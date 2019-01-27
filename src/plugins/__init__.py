from conf import settings
"""
这里是打包程序，以后别人导入plugins包就直接加载pack函数的代码
而不用我们自己去另外建立一个py文件
"""
def pack():
    response = {}
    for k,v in settings.PLUGINS.items():
        import importlib
        m_path,classname = v.rsplit('.', maxsplit=1)
        # 这里采用了反射的方法，通过字符串找到了与字符串名字相对应的类
        m = importlib.import_module(m_path)
        cls = getattr(m, classname)
        response[k] = cls().execute()
    return response