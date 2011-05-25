import time, sys
from logging import getLogger, StreamHandler, FileHandler, Formatter
from logging import DEBUG, INFO, WARNING, ERROR, CRITICAL

class MyLogger(object):
    def __init__(self, logger_name, make_unique=False, loglevel=INFO, 
                 filename=None, verbose=False, 
                 stdout_format='%(created)f,%(message)s',
                 tofile_format='%(created)f,%(message)s'):
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

    def log(self, level=INFO, msg):
        if level == DEBUG:
            self.logger.debug(msg)
        elif level == INFO:
            self.logger.info(msg)
        elif level == WARNING:
            self.logger.warning(msg)
        elif level == ERROR:
            self.logger.error(msg)
        elif level == CRITICAL:
            self.logger.critical(msg)
        else:
            self.logger.error("Invalid log level {0} for message {1}".format(level, msg))
