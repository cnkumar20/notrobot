import logging
import os
from typing import Any
APP_ROOT = "/usr/src/app" if "APP_ROOT" not in os.environ else os.environ["APP_ROOT"]

print(APP_ROOT)
class SingletonLogger:
    _logger: Any = None

    def __init__(self,name:str):
        self._logger_name= name
        self._logger = None
        self._fh: Any= None
        self._sh: Any= None
        self.formatter: logging.Formatter = logging.Formatter(
            fmt = '%(asctime)s - %(name)s - %(levelname)s - %(message)s',
            datefmt = '%Y-%m-%d %H:%M:%S'
        )
        self.log_level = logging.DEBUG
    
    def _init_logger(self):

        SingletonLogger._logger = logging.getLogger(self._logger_name)
        SingletonLogger._logger.setLevel(logging.DEBUG)

        SingletonLogger._sh = logging.StreamHandler()
        SingletonLogger._sh.setLevel(logging.DEBUG)
        SingletonLogger._sh.setFormatter(self.formatter)

        SingletonLogger._fh: logging.FileHandler = logging.FileHandler(
            f"{APP_ROOT}/logs/{self._logger_name}.log"
        )
        SingletonLogger._fh.setLevel(logging.DEBUG)
        SingletonLogger._fh.setFormatter(self.formatter)

        SingletonLogger._logger.addHandler(SingletonLogger._sh)
        SingletonLogger._logger.addHandler(SingletonLogger._fh)
    
    def get_logger(self):
        """
        return the logger, init if necessary
        """
        # pylint is not smart enough to recognized that
        # the self._logger is from logging.get_logger()
        # so it complains about missing members. The code works perferct well.
        # pylint: disable=no-member # [locall-disabled]
        # if self._logger_name not in logging.root.manager.loggerDict:
        if SingletonLogger._logger is None:
            self._init_logger()
            SingletonLogger._logger.info("logger initialized")
            SingletonLogger._logger.info("log level %s", self.log_level)
        # pylint: disable=broad-exception-raised # [locall-disabled]
        if SingletonLogger._logger is None:
            raise Exception("empty logger")
        return SingletonLogger._logger
