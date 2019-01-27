#coding:utf-8

from src.client import Agent
from src.client import SSH
from src.client import Salt
from conf import settings

def client():
    if settings.MODE == "agent":
        cli = Agent()
    elif settings.MODE == "ssh":
        cli = SSH()
    elif settings.MODE == "salt":
        cli = Salt()
    else:
        raise Exception("请配置资产采集模式，如：agent,ssh,salt")
    cli.process()