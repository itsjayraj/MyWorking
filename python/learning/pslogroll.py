import logging
from logging.handlers import RotatingFileHandler
import glob
from os import stat


fmt_str = "%(asctime)s:%(name)s:%(levelname)s:%(process)s:%(message)s"
logger = logging.getLogger()
logger.setLevel(level=logging.DEBUG)

fmt = logging.Formatter(fmt_str)
handler = RotatingFileHandler('rollover.log', maxBytes=512, backupCount=4)
handler.setFormatter(fmt)

logger.addHandler(handler)

for i in range(1, 25):
    logger.debug('dummy log message' + str(i))

for log_file in glob.glob('roll*'):
    print log_file, ':', stat(log_file).st_size


