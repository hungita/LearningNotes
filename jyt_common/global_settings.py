# -*- coding:utf-8 -*-

import json
import os

from jyt_common import jyt_common_helpers
from jyt_common import jyt_const
from jyt_common import jyt_sql_operation
from jyt_common.JytPythonConfigModel import JytPythonConfigModel

# import pandas as pd

jyt_const.ROOT_WORK_DIRECTORY_FULL_PATH_KEY_NAME = "ROOT_WORK_DIRECTORY_FULL_PATH"
jyt_const.ROOT_WORK_DIRECTORY_FULL_PATH = ""

jyt_const.ROOT_DATA_FILES_DIRECTORY_NAME = "DataFiles"
jyt_const.ROOT_CONFIG_FILES_DIRECTORY_NAME = "Configs"
jyt_const.JYT_PYTHON_CONFIG_FILE_NAME = "JytPythonConfig.json"
jyt_const.MODEL_CONFIG_FILE_NAME = "ModelConfig.json"


jyt_const.ROOT_DATA_FILES_DIRECTORY_FULL_PATH_KEY_NAME = "ROOT_DATA_FILES_DIRECTORY_FULL_PATH"
jyt_const.ROOT_DATA_FILES_DIRECTORY_FULL_PATH = ""

jyt_const.ROOT_CONFIG_FILES_DIRECTORY_FULL_PATH_KEY_NAME = "ROOT_CONFIG_FILES_DIRECTORY_FULL_PATH"
jyt_const.ROOT_CONFIG_FILES_DIRECTORY_FULL_PATH = ""

jyt_const.JYT_PYTHON_CONFIG_FILE_FULL_PATH_KEY_NAME = "JYT_PYTHON_CONFIG_FILE_FULL_PATH"
jyt_const.JYT_PYTHON_CONFIG_FILE_FULL_PATH = ""

jyt_const.MODEL_CONFIG_FILE_FULL_PATH_KEY_NAME = "MODEL_CONFIG_FILE_FULL_PATH"
jyt_const.MODEL_CONFIG_FILE_FULL_PATH = ""

jyt_const.JYT_PYTHON_CONFIG_MODEL_KEY_NAME = "JYT_PYTHON_CONFIG_MODEL"
jyt_const.MODEL_CONFIG_MODEL_KEY_NAME = "MODEL_CONFIG_MODEL"
jyt_const.JYT_PYTHON_CONFIG_MODEL = None
jyt_const.MODEL_CONFIG_MODEL = None


jyt_const.PREDICTED_TEMPERATURE_DATA_DICT = {}
# jyt_const.SWITCH_DICT = {}
jyt_const.EXCEPTION_DATA_list = []

jyt_const.JYT_DATA_OPERATOR_KEY_NAME = "JYT_DATA_OPERATOR"
jyt_const.JYT_DATA_OPERATOR = None

jyt_const.DATA_BASE_NAME = 'Arithmetic.db'

jyt_const.DATA_BASE_FILE_FULL_PATH_KEY_NAME = "DATA_BASE_FILE_FULL_PATH"
jyt_const.DATA_BASE_FILE_FULL_PATH = ""

# 数据表名集合
jyt_const.DATA_TABLE_NAME_LIST = ['jyt_plc_training_data']
# 训练数据表
jyt_const.DATA_TRAINING_TABLE_NAME = 'jyt_plc_training_data'
# 建议参数标记数据表
jyt_const.DATA_SIGN_TABLE_NAME = 'jyt_plc_sign_data'
# 异常数据表
jyt_const.DATA_EXCEPTION_TABLE_NAME = 'jyt_plc_exception_data'
# 标准数据表
jyt_const.DATA_STANDARD_TABLE_NAME = 'jyt_plc_standard_data'

jyt_const.furnace_temperature = '炉体温度'
jyt_const.furnace_body_pressure = '炉体压力'
jyt_const.furnace_level = '炉体液位'
jyt_const.exhaust_temperature = '排烟温度'
jyt_const.inlet_temperature = '进口温度'
jyt_const.output_temperature = '汇管温度'
jyt_const.manifold_temperature ='出口温度'
jyt_const.import_pressure = '进口压力'
jyt_const.outlet_pressure = '出口压力'
jyt_const.furnace_pressure = '炉膛压力'
jyt_const.oxygen_content = '氧含量'
jyt_const.ambient_temperature = '环境温度'
jyt_const.furnace_tube_temperature_1 = '炉管温度1'
jyt_const.furnace_tube_temperature_2 = '炉管温度2'
jyt_const.furnace_tube_temperature_3 = '炉管温度3'
jyt_const.furnace_tube_temperature_4 = '炉管温度4'
jyt_const.furnace_tube_temperature_5 = '炉管温度5'
jyt_const.furnace_tube_temperature_6 = '炉管温度6'
jyt_const.flammable_gas = '可燃气体'
jyt_const.gas_flow = '燃气流量'
jyt_const.water_flow = '水流量'
jyt_const.gas_pressure = '燃气压力'
jyt_const.current = '电流'
jyt_const.buffer_section_level = '缓冲段液位'
jyt_const.return_tank_level = '回水缸液位'
jyt_const.backwater_pressure = '回水缸压力'
jyt_const.backwater_tank_temperature = '回水缸温度'
jyt_const.water_level = '分水缸液位'
jyt_const.water_dividing_cylinder_pressure = '分水缸压力'
jyt_const.water_separator_temperature = '分水缸温度'
jyt_const.main_valve_opening = '主气阀开度'
jyt_const.main_damper_opening = '主风门开度'
jyt_const.micro_valve_opening = '微气阀开度'
jyt_const.breeze_door_opening = '微风门开度'
jyt_const.threshold_value = '提阀值'
jyt_const.flue_actuator_opening = '烟道执行器开度'
jyt_const.supply_of_heat = '供给热量'
jyt_const.effective_output = '有效输出量'
jyt_const.heating_furnace_load_rate = '加热炉负荷率'
jyt_const.combustion_load = '燃烧负荷'
jyt_const.excess_air_coefficient = '过剩空气系数'
jyt_const.smoke_loss = '排烟损失'
jyt_const.heat_loss = '散热损失'
jyt_const.positive_balance_efficiency = '正平衡效率'
jyt_const.counterbalance_efficiency = '反平衡效率'
jyt_const.average_efficiency = '平均效率'
jyt_const.gas_accumulation = '燃气累计量'
jyt_const.energy_accumulation = '电能累计量'
jyt_const.cumulative_amount_of_water_consumption = '水消耗累计量'
jyt_const.total_gas_accumulation = '总燃气累计量'
jyt_const.burner_firing_times = '燃烧器点火次数'
jyt_const.burner_running_time = '燃烧器运行时间'
jyt_const.system_running_time = '系统已运行时间'
jyt_const.low_calorific_value_of_gas = '燃气低热值'
jyt_const.upper_limit_of_outlet_temperature='热水炉出口温度上限'
jyt_const.lower_limit_of_outlet_temperature='热水炉出口温度下限'
jyt_const.upper_limit_of_outlet_temperature_other='参水炉出口温度上限'
jyt_const.lower_limit_of_outlet_temperature_other='参水炉出口温度下限'
jyt_const.upper_limit_exhaust_temperature='排烟温度上限'
jyt_const.lower_limit_exhaust_temperature='排烟温度下限'
jyt_const.upper_limit_oxygen_content='氧含量上限'
jyt_const.lower_limit_oxygen_content='氧含量下限'
jyt_const.upper_limit_furnace_temperature='炉体温度上限'
jyt_const.lower_limit_furnace_temperature='炉体温度下限'


def init_global_settings():
    """
    初始化
    :return:
    """

    # 初始化 根工作 路径
    # current_root_directory_full_path = os.getcwd()
    current_file_full_path = os.path.abspath(__file__)
    # current_file_full_name = os.path.basename(__file__)
    # current_file_full_path = jyt_common_helpers.find_file_full_path(current_root_directory_full_path,
    #                                                                 current_file_full_name)
    current_root_work_directory_full_path = os.path.dirname(os.path.dirname(current_file_full_path))

    jyt_const.set_const_value(jyt_const.ROOT_WORK_DIRECTORY_FULL_PATH_KEY_NAME, current_root_work_directory_full_path)
    current_root_work_directory_full_path = jyt_const.ROOT_WORK_DIRECTORY_FULL_PATH

    root_data_files_directory_full_path = os.path.join(current_root_work_directory_full_path,
                                                       jyt_const.ROOT_DATA_FILES_DIRECTORY_NAME)
    jyt_const.set_const_value(jyt_const.ROOT_DATA_FILES_DIRECTORY_FULL_PATH_KEY_NAME,
                              root_data_files_directory_full_path)

    data_base_file_full_path = os.path.join(root_data_files_directory_full_path,
                                            jyt_const.DATA_BASE_NAME)
    jyt_const.set_const_value(jyt_const.DATA_BASE_FILE_FULL_PATH_KEY_NAME,
                              data_base_file_full_path)

    root_config_files_directory_full_path = os.path.join(current_root_work_directory_full_path,
                                                         jyt_const.ROOT_CONFIG_FILES_DIRECTORY_NAME)
    jyt_const.set_const_value(jyt_const.ROOT_CONFIG_FILES_DIRECTORY_FULL_PATH_KEY_NAME,
                              root_config_files_directory_full_path)

    jyt_python_config_file_full_path = os.path.join(root_config_files_directory_full_path,
                                                    jyt_const.JYT_PYTHON_CONFIG_FILE_NAME)
    jyt_const.set_const_value(jyt_const.JYT_PYTHON_CONFIG_FILE_FULL_PATH_KEY_NAME, jyt_python_config_file_full_path)

    model_config_file_full_path = os.path.join(root_config_files_directory_full_path,
                                                    jyt_const.MODEL_CONFIG_FILE_NAME)
    jyt_const.set_const_value(jyt_const.MODEL_CONFIG_FILE_FULL_PATH_KEY_NAME, model_config_file_full_path)

    jyt_common_helpers.init_folder(root_data_files_directory_full_path)
    jyt_common_helpers.init_folder(root_config_files_directory_full_path)
    jyt_const.set_const_value(jyt_const.JYT_DATA_OPERATOR_KEY_NAME, jyt_sql_operation.Singleton.instance())


    json_string = None

    jyt_const.JYT_DATA_OPERATOR.init(jyt_const.DATA_BASE_FILE_FULL_PATH, jyt_const.DATA_TABLE_NAME_LIST)
    # 初始化 配置表
    if not os.path.exists(jyt_python_config_file_full_path):
        jyt_python_config_model = JytPythonConfigModel()
        jyt_python_config_model.TimerNums = 123
        jyt_python_config_model.PlcFunctionMaps["PlcFunctionIdMapKey"] = "PlcFunctionIdMapValue"
        json_string = json.dumps(jyt_python_config_model, default=lambda obj: obj.__dict__, indent=4)
        # print(json_string)
        with open(jyt_python_config_file_full_path, 'w', encoding="utf-8") as f:
            f.write(json_string)
            pass
        with open(model_config_file_full_path, 'w', encoding="utf-8") as f:
            f.write(json_string)
            pass
        pass



    with open(jyt_python_config_file_full_path, 'r', encoding="utf-8") as f:
        json_string = f.read()
        pass


    # if json_string:
    #     json_dict = json.loads(json_string)
    #     jyt_python_config_model = JytPythonConfigModel.map_json_dict(json_dict)
    #     if jyt_python_config_model:
    #         jyt_const.set_const_value(jyt_const.JYT_PYTHON_CONFIG_MODEL_KEY_NAME,
    #                                   jyt_python_config_model)
    #         pass
    #     pass
    #
    # pass



    if json_string:
        json_dict = {}
        if json_string.startswith(u'\ufeff'):
            content = json_string.encode('utf8')[3:].decode('utf8')
            json_dict = json.loads(content)
        else:
            json_dict = json.loads(json_string)
        jyt_python_config_model = JytPythonConfigModel.map_json_dict(json_dict)
        if jyt_python_config_model:
            jyt_const.set_const_value(jyt_const.JYT_PYTHON_CONFIG_MODEL_KEY_NAME,
                                      jyt_python_config_model)
            pass

        pass
    pass

    json_string_model = None

    # jyt_const.JYT_DATA_OPERATOR.init(jyt_const.DATA_BASE_FILE_FULL_PATH, jyt_const.DATA_TABLE_NAME_LIST)
    # 初始化 配置表
    if not os.path.exists(model_config_file_full_path):
        model_config_model = JytPythonConfigModel()
        model_config_model.TimerNums = 123
        model_config_model.PlcFunctionMaps["PlcFunctionIdMapKey"] = "PlcFunctionIdMapValue"
        json_string_model = json.dumps(model_config_model, default=lambda obj: obj.__dict__, indent=4)
        # print(json_string)
        with open(model_config_file_full_path, 'w', encoding="utf-8") as f:
            f.write(json_string_model)
            pass
        with open(model_config_file_full_path, 'w', encoding="utf-8") as f:
            f.write(json_string_model)
            pass
        pass

    with open(model_config_file_full_path, 'r', encoding="utf-8") as f:
        json_string_model = f.read()
        pass

    if json_string_model:
        model_json_dict = {}
        if json_string_model.startswith(u'\ufeff'):
            model_content = json_string_model.encode('utf8')[3:].decode('utf8')
            model_json_dict = json.loads(model_content)
        else:
            model_json_dict = json.loads(json_string_model)
        model_config_model = JytPythonConfigModel.map_json_dict(model_json_dict)
        if model_config_model:
            jyt_const.set_const_value(jyt_const.MODEL_CONFIG_MODEL_KEY_NAME,
                                      model_config_model)
            pass

        pass
    pass

    A=jyt_const.JYT_PYTHON_CONFIG_MODEL
    B=jyt_const.MODEL_CONFIG_MODEL

if __name__ == '__main__':
    # import os
    # from jyt_common import jyt_common_helpers
    # from jyt_common import jyt_const
    # from jyt_common import global_settings

    init_global_settings()
    # jyt_sql_operation.init(jyt_const.ROOT_WORK_DIRECTORY_FULL_PATH, jyt_const.DATA_TABLE_NAME_LIST)
    # print("aaaa")

    print(jyt_const.ROOT_WORK_DIRECTORY_FULL_PATH)
    print(jyt_const.ROOT_DATA_FILES_DIRECTORY_FULL_PATH)
    print(jyt_const.ROOT_CONFIG_FILES_DIRECTORY_FULL_PATH)
    print(jyt_const.JYT_PYTHON_CONFIG_FILE_FULL_PATH)
    print(jyt_const.MODEL_CONFIG_FILE_FULL_PATH)
    print(jyt_const.JYT_PYTHON_CONFIG_MODEL)
    print(jyt_const.MODEL_CONFIG_MODEL)

    # furnace_temperature_model_params = jyt_const.MODEL_CONFIG_MODEL.furnace_temperature_model_params
    # print(furnace_temperature_model_params)


    # exhaust_temperature = plcFunctionMaps[jyt_const.exhaust_temperature]

    # print(exhaust_temperature)

    # furnace_temperature_fid =  jyt_const.JYT_PYTHON_CONFIG_MODEL.PlcFunctionMaps[jyt_const.furnace_temperature]
    # jyt_const.JYT_PYTHON_CONFIG_MODEL.PlcFunctionMaps[jyt_const.furnace_body_pressure]
    # jyt_const.JYT_PYTHON_CONFIG_MODEL.PlcFunctionMaps[jyt_const.furnace_level]
    # a=jyt_const.JYT_PYTHON_CONFIG_MODEL.Dataframe_col[jyt_const.exhaust_temperature]
    # print(a)
    # jyt_const.JYT_PYTHON_CONFIG_MODEL.PlcFunctionMaps[jyt_const.inlet_temperature]
    # b= jyt_const.JYT_PYTHON_CONFIG_MODEL.Dataframe_col[jyt_const.output_temperature]
    # print(b)
    # jyt_const.JYT_PYTHON_CONFIG_MODEL.PlcFunctionMaps[jyt_const.import_pressure]
    # jyt_const.JYT_PYTHON_CONFIG_MODEL.PlcFunctionMaps[jyt_const.outlet_pressure]
    # jyt_const.JYT_PYTHON_CONFIG_MODEL.PlcFunctionMaps[jyt_const.furnace_pressure]
    # c=jyt_const.JYT_PYTHON_CONFIG_MODEL.PlcFunctionMaps[jyt_const.oxygen_content]
    # print(c)
    # jyt_const.JYT_PYTHON_CONFIG_MODEL.PlcFunctionMaps[jyt_const.ambient_temperature]
    # jyt_const.JYT_PYTHON_CONFIG_MODEL.PlcFunctionMaps[jyt_const.furnace_tube_temperature_1]
    # jyt_const.JYT_PYTHON_CONFIG_MODEL.PlcFunctionMaps[jyt_const.furnace_tube_temperature_2]
    # jyt_const.JYT_PYTHON_CONFIG_MODEL.PlcFunctionMaps[jyt_const.furnace_tube_temperature_3]
    # jyt_const.JYT_PYTHON_CONFIG_MODEL.PlcFunctionMaps[jyt_const.furnace_tube_temperature_4]
    # jyt_const.JYT_PYTHON_CONFIG_MODEL.PlcFunctionMaps[jyt_const.furnace_tube_temperature_5]
    # jyt_const.JYT_PYTHON_CONFIG_MODEL.PlcFunctionMaps[jyt_const.furnace_tube_temperature_6]
    # jyt_const.JYT_PYTHON_CONFIG_MODEL.PlcFunctionMaps[jyt_const.flammable_gas]
    # d=jyt_const.JYT_PYTHON_CONFIG_MODEL.PlcFunctionMaps[jyt_const.gas_flow]
    # print(d)
    # jyt_const.JYT_PYTHON_CONFIG_MODEL.PlcFunctionMaps[jyt_const.water_flow]
    # jyt_const.JYT_PYTHON_CONFIG_MODEL.PlcFunctionMaps[jyt_const.gas_pressure]
    # jyt_const.JYT_PYTHON_CONFIG_MODEL.PlcFunctionMaps[jyt_const.current]
    # jyt_const.JYT_PYTHON_CONFIG_MODEL.PlcFunctionMaps[jyt_const.buffer_section_level]
    # jyt_const.JYT_PYTHON_CONFIG_MODEL.PlcFunctionMaps[jyt_const.return_tank_level]
    # jyt_const.JYT_PYTHON_CONFIG_MODEL.PlcFunctionMaps[jyt_const.backwater_pressure]
    # jyt_const.JYT_PYTHON_CONFIG_MODEL.PlcFunctionMaps[jyt_const.backwater_tank_temperature]
    # jyt_const.JYT_PYTHON_CONFIG_MODEL.PlcFunctionMaps[jyt_const.water_level]
    # jyt_const.JYT_PYTHON_CONFIG_MODEL.PlcFunctionMaps[jyt_const.water_dividing_cylinder_pressure]
    # jyt_const.JYT_PYTHON_CONFIG_MODEL.PlcFunctionMaps[jyt_const.water_separator_temperature]
    # jyt_const.JYT_PYTHON_CONFIG_MODEL.PlcFunctionMaps[jyt_const.main_valve_opening]
    # jyt_const.JYT_PYTHON_CONFIG_MODEL.PlcFunctionMaps[jyt_const.main_damper_opening]
    # jyt_const.JYT_PYTHON_CONFIG_MODEL.PlcFunctionMaps[jyt_const.micro_valve_opening]
    # jyt_const.JYT_PYTHON_CONFIG_MODEL.PlcFunctionMaps[jyt_const.breeze_door_opening]
    # jyt_const.JYT_PYTHON_CONFIG_MODEL.PlcFunctionMaps[jyt_const.threshold_value]
    # jyt_const.JYT_PYTHON_CONFIG_MODEL.PlcFunctionMaps[jyt_const.flue_actuator_opening]
    # jyt_const.JYT_PYTHON_CONFIG_MODEL.PlcFunctionMaps[jyt_const.supply_of_heat]
    # jyt_const.JYT_PYTHON_CONFIG_MODEL.PlcFunctionMaps[jyt_const.effective_output]
    # jyt_const.JYT_PYTHON_CONFIG_MODEL.PlcFunctionMaps[jyt_const.heating_furnace_load_rate]
    # jyt_const.JYT_PYTHON_CONFIG_MODEL.PlcFunctionMaps[jyt_const.combustion_load]
    # jyt_const.JYT_PYTHON_CONFIG_MODEL.PlcFunctionMaps[jyt_const.excess_air_coefficient]
    # jyt_const.JYT_PYTHON_CONFIG_MODEL.PlcFunctionMaps[jyt_const.smoke_loss]
    # jyt_const.JYT_PYTHON_CONFIG_MODEL.PlcFunctionMaps[jyt_const.heat_loss]
    # jyt_const.JYT_PYTHON_CONFIG_MODEL.PlcFunctionMaps[jyt_const.positive_balance_efficiency]
    # jyt_const.JYT_PYTHON_CONFIG_MODEL.PlcFunctionMaps[jyt_const.counterbalance_efficiency]
    # jyt_const.JYT_PYTHON_CONFIG_MODEL.PlcFunctionMa[jyt_const.average_efficiency]
    # jyt_const.JYT_PYTHON_CONFIG_MODEL.PlcFunctionMaps[jyt_const.gas_accumulation]
    # jyt_const.JYT_PYTHON_CONFIG_MODEL.PlcFunctionMaps[jyt_const.energy_accumulation]
    # jyt_const.JYT_PYTHON_CONFIG_MODEL.PlcFunctionMaps[jyt_const.cumulative_amount_of_water_consumption]
    # jyt_const.JYT_PYTHON_CONFIG_MODEL.PlcFunctionMaps[jyt_const.total_gas_accumulation]
    # jyt_const.JYT_PYTHON_CONFIG_MODEL.PlcFunctionMaps[jyt_const.burner_firing_times]
    # jyt_const.JYT_PYTHON_CONFIG_MODEL.PlcFunctionMaps[jyt_const.burner_running_time]
    # jyt_const.JYT_PYTHON_CONFIG_MODEL.PlcFunctionMaps[jyt_const.system_running_time]
    # jyt_const.JYT_PYTHON_CONFIG_MODEL.PlcFunctionMaps[jyt_const.low_calorific_value_of_gas]

    pass
