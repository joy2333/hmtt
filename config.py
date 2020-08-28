# 发布文章的标题数据
import logging.handlers
import os

PUB_ARITCAL_TITLE = None

BASE_DIR = os.path.dirname(os.path.abspath(__file__))


def log_basic_config():
    # 1.创建日志器
    logger = logging.getLogger()
    # 2.设置日志级别
    logger.setLevel(logging.INFO)
    # 3.创建处理器
    Is = logging.StreamHandler()
    Iht = logging.handlers.TimedRotatingFileHandler(BASE_DIR + '/log/hmtt_test.log', when='midnight', interval=1,
                                                    backupCount=2)
    # 4.创建格式化器
    formatter = logging.Formatter(
        fmt='%(asctime)s %(levelname)s [%(name)s] [%(filename)s(%(funcName)s:%(lineno)d)] - %(message)s')
    # 5.将格式化器绑定到处理器
    Is.setFormatter(formatter)
    Iht.setFormatter(formatter)
    # 6.将处理器添加到日志器
    logger.addHandler(Is)
    logger.addHandler(Iht)
