import os
from common.settings import BASE_DIR

"""
Function for local debug. Clear allure directory.
"""
ALLURE_DIR = os.path.join(BASE_DIR, 'results')
if os.path.exists(ALLURE_DIR):
    for the_file in os.listdir(ALLURE_DIR):
        file_path = os.path.join(ALLURE_DIR, the_file)
        try:
            if os.path.isfile(file_path):
                os.unlink(file_path)

        except Exception as e:
            print(e)