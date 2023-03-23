import os
import logging

import requests

FORMAT = "%(asctime)s %(levelname)s %(message)s"
logging.basicConfig(filename='scan_and_send_file.log', encoding='utf-8', level=logging.INFO, format=FORMAT)


class ScanAndSendFile:
    def __init__(self, token):
        self.token = token

    def __getFilePath(self, path):
        with os.scandir(path) as it:
            file = max(it, key=os.path.getctime)
            filePath = os.path.join(file)
            logging.info(filePath)
            return filePath

    def __sendFilePath(self, to_url, file_path):
        res = requests.post(to_url, data={'file_path': file_path, 'token': self.token})
        logging.info(res.status_code)
        return file_path, res.status_code

    def go(self, path, to_url):
        try:
            getFilePath = self.__getFilePath(path)
            result = self.__sendFilePath(to_url, getFilePath)
            return result
        except ValueError as e:
            logging.debug(e)
            return None
        except Exception as e:
            logging.exception(e)
            return None
