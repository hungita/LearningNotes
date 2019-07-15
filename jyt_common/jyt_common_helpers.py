# -*- coding:utf-8 -*-

"""

时间: 2018/9/30 8:53

作者: lanymy

文件: jyt_common_helpers.py

描述: 通用辅助方法

其它:

"""

import os

def find_file_full_path(dir_path, search_file_full_name):
    """
    从目录路径中 找指定 文件名称的 全路径
    :param dir_path: 要搜索的文件夹路径
    :param search_file_full_name: 要查找的文件名
    :return:
    """
    for root, dirs, files in os.walk(dir_path):
        for filename in files:
            if filename == search_file_full_name:
                return os.path.join(root, search_file_full_name)
    return None
    pass

def init_folder(folder_full_path):
    """
    初始化文件夹 如果不存在 则创建 文件夹
    :return:
    """
    if not os.path.exists(folder_full_path):
        os.makedirs(folder_full_path)
    pass

if __name__ == '__main__':

    from jyt_common import jyt_common_helpers

    current_root_directory_full_path = os.getcwd()
    current_file_full_path=os.path.abspath(__file__)
    current_file_full_name=os.path.basename(__file__)
    current_file_full_path = find_file_full_path(current_root_directory_full_path, current_file_full_name)
    current_work_root_directory_full_path= os.path.dirname(os.path.dirname(current_file_full_path))

    pass