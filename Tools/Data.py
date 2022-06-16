"""
导入该类可以对数据进行操作
用法：
Data.SaveData(_data, _path) # 保存数据到本地
_data = Data.LoadData(_path) # 从本地读取数据
"""
import pickle

import Tools.SendLog as SendLog


def SaveData(_data, _path):
    with open(_path, 'wb') as f:
        pickle.dump(_data, f)
    SendLog.PrintInfo(f"保存数据到{_path}中...")


def LoadData(_path):
    with open(_path, 'rb') as f:
        _data = pickle.load(f)
    SendLog.PrintInfo(f"从{_path}中读取数据...")
    return _data


if __name__ == '__main__':
    class StationConfig:
        def __init__(self):
            self.a = 1
            self.b = 2
            self.c = 3
    _save = StationConfig()

    # 测试：保存数据到本地data.bin
    print(f"保存数据数据{_save.a}，{_save.b}，{_save.c}")
    SaveData(_save, 'data.bin')

    # 测试：从本地data.bin读取数据到内存中
    _load = LoadData('data.bin')
    print(f"读取数据{_load.a}，{_load.b}，{_load.c}")
