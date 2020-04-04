import yagmail
from conf import setting
from lib.log import atp_log

# 发送邮件的方法
def sendmail(title,content,attrs=None):
	m = yagmail.SMTP(host=setting.MAIL_HOST,# 邮件HOST地址
					 user=setting.MAIL_USER # 用户名
				 	,password=setting.MAIL_PASSWRD # 授权码
				 	)
	m.send(to=setting.TO,# 接收用户，可以多个
		   subject=title,# 邮件主题
		   contents=content, # 邮件内容
		   attachments=attrs # 附件，多个附件则传入一个['1.txt','2.txt']
		   )
	atp_log.info('发送邮件完成') # 记录日志，打印log

