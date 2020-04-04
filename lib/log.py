import logging,os
from logging import handlers
from conf import setting

# 日志类
class MyLogger():
	# 初始化日志对象
	def __init__(self,file_name,level='info',backCount=5,when='D'):
		logger = logging.getLogger()  # 先实例化一个logger对象，先创建一个办公室
		logger.setLevel(self.get_level(level))  # 设置日志的级别的人
		# 控制台日志
		cl = logging.StreamHandler()
		# 文件日志
		bl = handlers.TimedRotatingFileHandler(filename=file_name, # 文件名称
											   when=when,  # 生成日志的规则,'S'表示秒,'M'表示分钟
											   interval=1, # 生成日志的频率,根据规则按照频率生成日志文件
											   backupCount=backCount, # 日志限制数量，超出则删除之前的日志
											   encoding='utf-8') # 日志文件编码格式
		# 日志输出的格式
		fmt = logging.Formatter('%(asctime)s - %(pathname)s[line:%(lineno)d] - %(levelname)s: %(message)s')
		cl.setFormatter(fmt)  # 设置控制台输出的日志格式
		bl.setFormatter(fmt)  # 设置文件里面写入的日志格式
		logger.addHandler(cl)
		logger.addHandler(bl)
		self.logger = logger

	# 根据字符串获取日志级别
	def get_level(self,str):
		level = {
			'debug':logging.DEBUG,
			'info':logging.INFO,
			'warn':logging.WARNING,
			'error':logging.ERROR
		}
		str = str.lower()
		return level.get(str)

# 拼好日志的绝对路径
path = os.path.join(setting.LOG_PATH,setting.LOG_NAME)
# 实例化一个MyLogger对象
atp_log = MyLogger(path,setting.LEVEL).logger


