"""
Simple wrapper for Python's logging module
"""

import time, sys
from logging import getLogger, StreamHandler, FileHandler, Formatter
from logging import INFO

class MyLogger(object):
    """
    Very simplistic logger with several settings defaulted.

    If no arguments are specified the logger will do nothing,
    so it is recommended to either set verbose to True, specify
    a filename to log to, or both.
    """
    def __init__(self, logger_name=__name__, make_unique=True, loglevel=INFO, 
                 filename=None, verbose=False, 
                 stdout_format='%(created)f,%(message)s',
                 tofile_format='%(created)f,%(message)s'):
        """
        :Parameters:
         - `logger_name`: name for logger
         - `make_unique`: whether to append a unique timestamp to the name
         - `loglevel`: which messages to log
         - `filename`: If this is set, log messages to a file
         - `verbose`: If this is True, log messages to stdout
         - `stdout_format`: string format for stdout messages
         - `tofile_format`: string format for messages in log file
        """
        if make_unique:
            logger_name = logger_name + str(time.time())
        self.logger = getLogger(logger_name)
        self.logger.setLevel(loglevel)
        if filename:
            handler = FileHandler(filename)
            handler.setFormatter(Formatter(fmt=tofile_format))
            self.logger.addHandler(handler)
        if verbose:
            handler = StreamHandler(sys.stdout)
            handler.setFormatter(Formatter(fmt=stdout_format))
            self.logger.addHandler(handler)

    def log(self, msg, level=INFO):
        """
        Send a message to the logger. The level will be decoded and the
        correct logging method called.

        :Parameters:
         - `msg`: Message being logged
         - `level`: (str) how severe the message is.
        """
        if type(level) is str:
            level = level.lower()
        if level == "debug":
            self.logger.debug(msg)
        elif level == INFO or level == "info":
            self.logger.info(msg)
        elif level == "warning":
            self.logger.warning(msg)
        elif level == "error":
            self.logger.error(msg)
        elif level == "critical":
            self.logger.critical(msg)
        else:
            self.logger.error("Invalid log level {0} for message {1}".format(level, msg))
