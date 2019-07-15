import json
import numpy as np
import os


class MyEncoder(json.JSONEncoder):

    def default(self, obj):

        if isinstance(obj, np.integer):
            return int(obj)
        elif isinstance(obj, np.floating):
            return float(obj)
        elif isinstance(obj, np.ndarray):
            return obj.tolist()
        else:
            return super(MyEncoder, self).default(obj)

    def write_client_datafile_json(target_dir_path, file_name, postfix, ret_content):
        if not os.path.exists(target_dir_path):
            os.makedirs(target_dir_path)
            with open(target_dir_path + file_name + postfix, 'w')as outfile:
                json.dump(ret_content, outfile, cls=MyEncoder)
                return
