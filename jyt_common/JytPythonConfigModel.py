# -*- coding:utf-8 -*-

"""

时间: 2018/10/8 9:44

作者: lanymy

文件: JytPythonConfigModel.py

描述: 配置表实体类

其它:

"""
# import demjson
import json


class JytPythonConfigModel(object):
    """
    配置表实体类
    """

    def __init__(self):
        self.TimerNums = None
        self.PlcFunctionMaps = {}
        self.FurnaceGroups = {}
        pass

    @classmethod
    def map_json_dict(cls, json_dict):
        model = cls()
        model.__dict__ = json_dict
        return model
        pass

    pass


if __name__ == '__main__':

    # from jyt_common.PlcFunctionMapModel import PlcFunctionMapModel
    from jyt_common import global_settings

    global_settings.init_global_settings()
    config_json = global_settings.jyt_const.JYT_PYTHON_CONFIG_MODEL

    # furanceid = '111'
    # global groupid
    # global type
    # for FurnaceGroup in config_json.FurnaceGroups:
    #     if FurnaceGroup:
    #         furnaces = FurnaceGroup['Furnaces']
    #         for furnace in furnaces:
    #             if furnace['EquipmentId'] == furanceid:
    #                 groupid = FurnaceGroup['GroupId']
    #                 type = furnace['Type']
    #                 break

    jytPythonConfigModel = JytPythonConfigModel()
    jytPythonConfigModel.TimerNums = "123"

    for i in range(10):
        mapKey = "key" + str(i)
        mapValue = "value" + str(i)

        # plcFunctionMapModel = PlcFunctionMapModel()
        # plcFunctionMapModel.PlcFunctionMapKey = "key" + str(i)
        # plcFunctionMapModel.PlcFunctionMapValue = "value" + str(i)
        #
        # jytPythonConfigModel.PlcFunctionMaps.append(plcFunctionMapModel)
        jytPythonConfigModel.PlcFunctionMaps[mapKey] = mapValue
        pass

    json1 = json.dumps(jytPythonConfigModel, default=lambda obj: obj.__dict__, indent=4)
    print(json1)
    print(global_settings.jyt_const.JYT_PYTHON_CONFIG_FILE_FULL_PATH)

    with open(global_settings.jyt_const.JYT_PYTHON_CONFIG_FILE_FULL_PATH, 'w') as f:
        f.write(json1)
        pass

    json2 = None

    # with open(global_settings.jyt_const.JYT_PYTHON_CONFIG_FILE_FULL_PATH, 'r') as f:
    #     json2 = f.read()
    #     pass

    print(json2)

    aModel = json.loads(json2)

    pass
