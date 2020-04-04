import os,sys

'''
    配置项目环境变量,用于各个模块之间的调用,系统可用找到对应的模块位置
'''
curPath = os.path.abspath(os.path.dirname(__file__))
rootPath = os.path.split(curPath)[0]
sys.path.append(rootPath)

from lib.common import OpCase
from lib.send_mail import sendmail
from conf import setting


# 运行测试的主类
class CaseRun(object):

	def find_cases(self):
		# 实例化OpCase类
		op = OpCase()
		# 循环遍历测试用来目录下的每一个excel
		for f in os.listdir(setting.CASE_PATH):
			# 拼接获取文件的绝对路径
			abs_path = os.path.join(setting.CASE_PATH,f)
			# 调用op对象的get_case方法获取当前excel用例截取的接口信息数据
			case_list = op.get_case(abs_path)
			# 定义一个存储返回值列表
			res_list = []
			# 初始化定义成功和失败的用例个数
			pass_count,fail_count = 0,0
			# 循环当前excel所有行信息
			for case in case_list:
				# 将当前行数据提取出来赋值给相应的变量
				url,method,req_data,check = case
				# 调用op对象的my_request方法，请求接口并拿到响应数据
				res = op.my_request(url,method,req_data)
				# 调用op对象的check_res方法，验证接口返回数据和预期是否一致
				status = op.check_res(res,check)
				# 将接口响应数据和验证结果添加到测试结果列表中
				res_list.append([res,status])
				# 根据验证结果计算成功与失败的用例个数
				if status=='通过':
					pass_count+=1
				else:
					fail_count+=1
			# 调用op的write_excel方法，将响应结果和验证结果写入excel
			op.write_excel(res_list)
			# 定义测试报告内容
			msg = '''
					xx你好：
						本次共运行%s条用例，通过%s条，失败%s条。
					'''%(len(res_list),pass_count,fail_count)
			# 发送测试报告，并附件测试用例，该测试用例为执行接口测试之后，包含测试结果和验证结果的excel文件
			sendmail('测试用例运行结果',content=msg,attrs=abs_path)

# 执行该python文件，默认就实例化CaseRun对象，并调用find_cases方法
CaseRun().find_cases()
