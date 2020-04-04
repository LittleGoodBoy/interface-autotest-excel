import os

# 获取上上一级的路径，也就是ATP目录的绝对路径作为根路径
BASE_PATH = os.path.dirname(
	os.path.dirname(os.path.abspath(__file__))
)
# 发邮件相关参数：HOST、USER、PASSWORD
MAIL_HOST='smtp.163.com'
MAIL_USER='xxxxx@163.com'
MAIL_PASSWRD = 'xxxxx'

# 接收邮件的用户名
TO = [
	'xxxx@qq.com',
]

# 指定当前日志级别
LEVEL = 'debug'
# 拼接存放日志的路径
LOG_PATH = os.path.join(BASE_PATH,'logs')
# 拼接存放测试用例的路径
CASE_PATH = os.path.join(BASE_PATH,'cases')
# 定义日志的文件名称
LOG_NAME='xxxx.log'

