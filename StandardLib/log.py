# coding=utf-8
import logging

DEBUG = logging.DEBUG
INFO = logging.INFO
WARNING = logging.WARNING
ERROR = logging.ERROR
CRITICAL = logging.CRITICAL


# 日志等级
level_names = {
    logging.DEBUG: "DEBUG",
    logging.INFO: "INFO",
    logging.WARNING: "WARNING",
    logging.ERROR: "ERROR",
    logging.CRITICAL: "CRITICAL",
}

# logging.warning("Warning!!!")
# logging.info("Nothing~")
# logging.debug("Debug..")
# logging.error("Error!")


def example1():
    logging.basicConfig(level=logging.INFO)
    # logging.basicConfig(level=logging.DEBUG)
    logger = logging.getLogger(__name__)
    # logger.setLevel(DEBUG)
    logger.info('Start reading database')

    records = {'john': 55, 'tome': 66}
    logger.debug('Records:%s', records)
    logger.info('Updating records...')

    logger.info('Finish updating records')


def example2():
    # 写入日志文件，创建文件handler，设置写入等级，设置日志信息格式，将日志handler添加至日志
    logging.basicConfig(level=logging.INFO)
    logger = logging.getLogger(__name__)
    logger.setLevel(logging.INFO)
    handler = logging.FileHandler('test.log')
    handler.setLevel(logging.INFO)
    formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')
    handler.setFormatter(formatter)
    logger.addHandler(handler)
    logger.info('Hello test')


if __name__ == '__main__':
    example1()
    example2()