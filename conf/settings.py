#coding:utf-8
import os

BASEDIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
MODE = 'Agent'

TEST_MODE = True

PLUGINS = {
    "disk":"src.plugins.disk.DiskPlugin",
    "mem":"src.plugins.meme.MemPlugin",
    "nic":"src.plugins.nic.Nicplugin"
}