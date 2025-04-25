import os
import sys

import numpy as np
import pandas as pd
import dill

from src.exception import CustomException

print("utils.py loaded successfully")

def save_object(file_path, obj):
    try:
        dir_path = os.path.dirname(file_path)

        os.makedirs(dir_path, exist_ok=True)

        with open(file_path, "wb") as file_obj:
            dill.dump(obj, file_obj)
        print(f"Object saved successfully at: {file_path}")    

    except Exception as e:
        print(f"Failed to save object:{e}")
        raise CustomException(e, sys)
    
