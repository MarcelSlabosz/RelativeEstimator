import logging
import json

from relative_estimator import JiraRelativrEstimatorException


class JiraREOutputException(JiraRelativrEstimatorException):
    pass


class JSONWriter:
    def __init__(self, configuration):
        self._file = None
        self.__config = configuration
        self.__logger = logging.getLogger(__name__)
        self.__explode_config()
        self.__create_directory_if_not_exists(self._file)

    def __explode_config(self):
        self._file = self.__config['file']

    def __create_directory_if_not_exists(self, file_path):
        import os
        directory = os.path.dirname(file_path)
        if not os.path.exists(directory):
            os.makedirs(directory)

    def write_to_file(self, issues):
        file_content = {"items": issues}
        with open(self._file, "w") as out_file:
            json.dump(file_content, out_file)
