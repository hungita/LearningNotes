import datetime
import sqlite3
import threading
import time

data_path = r"F:\pythonproject\JytArithmeticProject\trunk\DataFiles\Arithmetic.db"
data_table_name_list = []
data_lock = threading.Lock()
data_connection = None


class Singleton(object):
    _instance_lock = threading.Lock()

    def __init__(self):
        time.sleep(1)

    # def __del__(self):
    #     global data_connection
    #     data_connection.close()
    #     data_connection = None

    if __name__ == '__main__':
        # global_settings.init_global_settings()
        # init()
        pass

    @classmethod
    def instance(cls, *args, **kwargs):
        if not hasattr(Singleton, "_instance"):
            with Singleton._instance_lock:
                if not hasattr(Singleton, "_instance"):
                    Singleton._instance = Singleton(*args, **kwargs)
        return Singleton._instance

    @classmethod
    def get_sql_connection(cls, file_path):
        """
        获取数据库连接
        :param file_path:
        :return:
        """
        return sqlite3.connect(file_path, check_same_thread=False)

    @classmethod
    def create_data_table(cls, date=None):
        """
        创建表
        :return:
        """
        try:
            # 根据配置列表创建日表
            if data_table_name_list:
                for temp in data_table_name_list:
                    sql = f'SELECT sql FROM sqlite_master WHERE type=\'table\' AND name = \'{temp}\''
                    result = cls.fetch(sql)
                    if result:
                        string = str(result[0])
                        create_table_sql = string[string.rfind("('") + 2:string.rfind("',)")]
                        if date:
                            date_time = date
                        else:
                            date_time = datetime.datetime.now().strftime('%Y%m%d')
                        name = "if not exists " + temp + "_" + date_time
                        create_table_sql = create_table_sql.replace(temp, name).replace('\\n', '').replace('\\r', '')
                        cls.execute(create_table_sql)

        except Exception as e:
            print(e)
        pass

    @classmethod
    def get_daily_table_name(cls, table_name):
        """
        根据表名获取对应的日表
        :param table_name:
        :return:
        """
        return table_name + "_" + datetime.datetime.now().strftime('%Y%m%d')

    @classmethod
    def get_dateday_table_name(cls, table_name, datetimenow):
        """
        根据表名获取对应的日表
        :param table_name:
        :return:
        """
        result = table_name + "_" + datetimenow
        return result

    @classmethod
    def execute(cls, sql):
        """
        执行sql
        :param sql:
        :return:
        """
        global data_lock
        data_lock.acquire()
        # global data_connection
        connection = sqlite3.connect(data_path)
        connection.execute(sql)
        connection.commit()
        connection.close()
        connection = None
        data_lock.release()
        pass

    @classmethod
    def fetch(cls, sql):
        """
        获取数据
        :param sql:
        :return:
        """
        global data_lock
        data_lock.acquire()
        # conn = cls.get_sql_connection(data_path)
        # global data_connection
        connection = sqlite3.connect(data_path)
        connection.execute(sql)
        cursor = connection.cursor()
        cursor.execute(sql)
        result = cursor.fetchall()
        cursor.close()
        connection.close()
        cursor = None
        connection = None
        data_lock.release()
        return result

    @classmethod
    def init(cls, path, name_list):
        """
        初始化
        :return:
        """
        global data_path
        data_path = path
        global data_table_name_list
        data_table_name_list = name_list
        # global data_connection
        # data_connection = cls.get_sql_connection(data_path)
        cls.create_data_table()

    @classmethod
    def get_plc_datas_by_condition(cls, equipment_id, function_id_list, start_time, end_time):
        """
        根据条件调用plc数据
        (禁止跨天调用)
        :param equipment_id: 加热炉ID
        :param function_id_list: 功能区ID列表
        :param start_time: 开始时间
        :param end_time: 结束时间
        :return:
        """
        temp = ''
        temp_time = time.strptime(start_time, "%Y-%m-%d %H:%M:%S")
        date = time.strftime('%Y%m%d', temp_time)
        for function_id in function_id_list:
            temp = temp + f'max(case FunctionID when "{function_id}" then DataValue else NULL end) as "{function_id}",'
        if temp:
            temp = temp[0:-1]
            sql = f"select {temp} from jyt_plc_training_data_{date} where CreateDateTime>='{start_time}' and CreateDateTime<='{end_time}' and  EquipmentID={equipment_id} group by BatchNumber order by CreateDateTime"
            result = cls.fetch(sql)
            # global data_connection
            # cursor = data_connection.cursor()
            # cursor.execute(sql)
            # result = cursor.fetchall()
            return result

    @classmethod
    def get_row_index(cls, start_date_time, create_date_time):
        delta = create_date_time - start_date_time
        total_seconds = delta.seconds
        return int(total_seconds / 10)

    @classmethod
    def get_plc_datas_by_condition_new(cls, equipment_id, function_id_list, start_time, end_time):
        """
        根据条件调用plc数据
        (禁止跨天调用)
        :param equipment_id: 加热炉ID
        :param function_id_list: 功能区ID列表
        :param start_time: 开始时间
        :param end_time: 结束时间
        :return:
        """
        function_ids = ''
        temp_time = time.strptime(start_time, "%Y-%m-%d %H:%M:%S")
        date = time.strftime('%Y%m%d', temp_time)
        for function_id in function_id_list:
            function_ids += f"'{function_id}',"
        if function_ids:
            function_ids = function_ids[0:-1]
            sql = f"select EquipmentID,FunctionID,DataValue,strftime('%Y-%m-%d %H:%M:%S', createdatetime) as CreateDateTime from jyt_plc_training_data_{date}  where EquipmentID = {equipment_id} and FunctionID in ({function_ids}) and CreateDateTime>='{start_time}' and CreateDateTime<='{end_time}' order by  CreateDateTime"
            # global data_connection
            # cursor = data_connection.cursor()
            # cursor.execute(sql)
            # result = cursor.fetchall()
            result = cls.fetch(sql)

            start_date_time = datetime.datetime.strptime(start_time, "%Y-%m-%d %H:%M:%S")
            data_dict = {}
            for row in result:
                # time_now=row[3]
                time_now=datetime.datetime.strptime(row[3], "%Y-%m-%d %H:%M:%S")
                row_index = cls.get_row_index(start_date_time, time_now)
                if row_index not in data_dict:
                    # 初始化字典
                    temp_dict = {}
                    for fid in function_id_list:
                        temp_dict[fid] = None
                    data_dict[row_index] = temp_dict
                sub_dict = data_dict[row_index]
                sub_dict[row[1]] = row[2]

            result_list = []
            for data in data_dict.values():
                result_list.append(tuple(data.values()))
            data_dict = None
            return result_list


'''

def check_table(file_path):
    conn = sqlite3.connect(file_path)
    cursor = conn.cursor()
    cursor.execute(
        "select count(*)  from sqlite_master where type='table' and name = 'JYT_PLC_REALTIME_DATA'"
    )
    result = cursor.fetchone()
    cursor.close()
    if result[0] <= 0:
        create_data_table(file_path)
'''

# def detect_walk(dir_path, search_file):
#     """
#     查找文件包含子目录
#     :param dir_path:
#     :param search_file:
#     :return:
#     """
#     for root, dirs, files in os.walk(dir_path):
#         for filename in files:
#             if filename == search_file:
#                 return os.path.join(root, search_file)


if __name__ == '__main__':
    SL = Singleton()
    equipment_id = 1812181604310470102
    function_id_list = ['FR00100', 'FR00040', 'FR00110']
    start_time = '2019-01-05 00:00:00'
    end_time = '2019-01-05 23:59:59'
    result = SL.get_plc_datas_by_condition_new(equipment_id, function_id_list, start_time, end_time)
    print(result)