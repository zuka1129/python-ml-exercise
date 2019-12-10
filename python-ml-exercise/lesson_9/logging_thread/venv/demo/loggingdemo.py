import logging as log
import logging

#打印日志
# log.basicConfig(level='DEBUG', filename='mylog')
# log.debug('this is an debug info')
# log.info('this is an information')
# log.warning('this is warning information')
# log.error('this is error information')

#格式设置举例
# LOG_FORMAT = '%(asctime)s -%(levelname)s -%(message)s'
# DATA_FORMAT = '%Y/%m/%d %H:%M:%S'
# log.basicConfig(filename='my.log', level=log.DEBUG, format=LOG_FORMAT, datefmt=DATA_FORMAT)
# log.debug('this is an debug info')
# log.info('this is an information')
# log.warning('this is warning information')
# log.error('this is error information')

#第一步：创建logger对象
logger = log.getLogger('mylogger')
logger.setLevel('DEBUG')

#第二步：创建各种处理器
#1、创建文件处理器，输入到文件
file_handler = log.FileHandler(filename='test.log', mode='a', encoding='UTF-8')
#2、创建流处理器，输入到控制台
stream_handler = log.StreamHandler()
#3、错误日志单独输入到一个文件
error_handler = log.FileHandler('error.log', mode='a', encoding='UTF-8')
error_handler.setLevel(log.ERROR)

#将所有处理器添加到logger中
lists = [file_handler, stream_handler, error_handler]
for handler in lists:
    logger.addHandler(handler)

#格式化
formatter = logging.Formatter(fmt='%(asctime)s -%(name)s -%(levelname)s -%(message)s', datefmt='%Y/%m/%d %H:%M:%S')

#设置格式化针对每个处理器进行分别设置
lists = [file_handler, stream_handler, error_handler]
for handler in lists:
    handler.setFormatter(formatter)
#过滤器
my_filter = logging.Filter('test')
file_handler.addFilter(my_filter)
stream_handler.addFilter(my_filter)
error_handler.addFilter(my_filter)

logger.info('test filter')
logger.info('this is an information, something is terrible')
logger.error('this is error information something')
logger.debug('this is an debug info something')