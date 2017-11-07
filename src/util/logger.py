import logging


class bcolors:
    HEADER = '\033[95m'
    OKBLUE = '\033[94m'
    OKGREEN = '\033[92m'
    WARNING = '\033[93m'
    FAIL = '\033[91m'
    ENDC = '\033[0m'
    BOLD = '\033[1m'
    UNDERLINE = '\033[4m'


class Logger:

    def __init__(self, cls_name):
        consoleHandler = logging.StreamHandler()
        logFormatter = logging.Formatter("[%(asctime)s]" + "[%(name)s][%(levelname)-5.5s] %(message)s")
        consoleHandler.setFormatter(logFormatter)

        self.logger = logging.getLogger(cls_name)
        self.logger.setLevel(logging.DEBUG)
        self.logger.addHandler(consoleHandler)

    def debug(self, msg, *args, **kwargs):
        msg = bcolors.OKBLUE + msg + bcolors.ENDC
        self.logger.debug(msg, *args, **kwargs)

    def set_log_level(self, level):
        self.logger.setLevel(level)


class LoggerFactory:

    logger_dict = {}

    '''
    def get_instance(self):
        if self.instance is None:
            self.instance = Logger()
        return self.instance
    '''
    @staticmethod
    def get_logger(cls_name):
        if cls_name in LoggerFactory.logger_dict:
            # return exist logger
            return LoggerFactory.logger_dict.get(cls_name, None)
        else:
            new_logger = Logger(cls_name)
            LoggerFactory.logger_dict[cls_name] = new_logger
            return new_logger
