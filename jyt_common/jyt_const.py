# -*- coding:utf-8 -*-
"""

时间: 2016年01月07日

作者: lanyanmiyu@qq.com

文件: jyt_const.py

描述: 常量类

其它:

"""

import sys


class JytConst(object):
    class JytConstError(TypeError):
        pass

    def __setattr__(self, key, value):
        # if self.__dict__.has_key(key):
        if key in self.__dict__:
            raise self.JytConstError("Changing const.{0}".format(key))
        else:
            self.__dict__[key] = value
        pass

    def __getattr__(self, key):
        if key in self.__dict__:
            return self.key
        else:
            return None
        pass

    def set_const_value(self,key,value):
        """
        设置常量属性值
        :param key: 常量名称
        :param value: 要设置的常量值
        :return:
        """
        if key in self.__dict__:
            self.__dict__[key] = value
            pass
        pass

    pass


sys.modules[__name__] = JytConst()

if __name__ == '__main__':
    from jyt_common import jyt_const

    jyt_const.AAA = 123
    print(jyt_const.AAA)
    jyt_const.set_const_value("AAA",456)
    print(jyt_const.AAA)
    # JytConst.AAA = 123
    # JytConst.AAA = 456
    # print(JytConst.AAA)
    pass
