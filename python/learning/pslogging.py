import logging

fmt_str = "%(asctime)s:%(levelname)ss:%(process)s:%(message)s"

logging.basicConfig(level=logging.DEBUG, format=fmt_str)
#logging.basicConfig(level=logging.DEBUG, format=fmt_str, filename='error.log')

logging.warning('warning msg')
logging.error('error msg')
logging.critical('critical msg')
logging.debug('debug msg')
logging.info('info msg')
