import xlrd
from xlutils import copy
from lib.log import atp_log
import requests


class OpCase(object):
	# 获取测试用例中接口相关信息
	def get_case(self,file_path):
		cases = [] # 存放所有的case
		if file_path.endswith('.xls') or file_path.endswith('.xlsx'):
			try:
				book = xlrd.open_workbook(file_path)        # 读取指定excel，获取book对象
				sheet = book.sheet_by_index(0)              # 获取第一页
				# 循环所有行，提取 4<= 列下标 <8 之间的列的数据
				for i in range(1,sheet.nrows):
					row_data = sheet.row_values(i)  # 获取当前行的所有数据
					cases.append(row_data[4:8])     # 截取指定部分的数据存入到列表
				atp_log.info('共读取%s条用例'%(len(cases)))
				self.file_path = file_path # 绑定文件地址到对象file_path属性上
			except Exception as e:
				atp_log.error('【%s】用例获取失败，错误信息：%s'%(file_path,e))
		else:
			atp_log.error('用例文件不合法的，%s'%file_path)
		return cases


	# 根据指定方式请求接口并获取响应数据
	def my_request(self,url,method,data):
		method = method.upper()         # 将请求类型转换成大写
		data = self.dataToDict(data)    # 数据拆分为map
		try :
			if method=='POST':
				res = requests.post(url,data).text          # 发送POST请求并获取文本信息
			elif method=='GET':
				res = requests.get(url,params=data).text    # 发送GET请求并获取文本信息
			else:
				atp_log.warning('该请求方式暂不支持。。')
				res = '该请求方式暂不支持。。'
		except Exception as e:
			msg = '【%s】接口调用失败，%s'%(url,e)
			atp_log.error(msg)
			res = msg
		return res

	# 响应数据与预期数据的验证方法
	def check_res(self,res,check):
		# 将响应数据中的  ": "  替换成  =
		res = res.replace('": "','=').replace('": ','=')
		for c in check.split(','): # 预期结果按照逗号拆分，并遍历，判断拆分之后的请求响应数据是否包含预期结果
			if c not in res:
				atp_log.info('结果校验失败，预期结果：【%s】，实际结果【%s】'%(c,res))
				return '失败'
		return '成功'

	# 根据结果将数据写入到excel
	def write_excel(self,cases_res):
		# [ ['dsfd',"通过"] ,['sdfsdf','失败'] ]
		book = xlrd.open_workbook(self.file_path)
		new_book = copy.copy(book)
		sheet = new_book.get_sheet(0)
		row = 1
		for case_case in cases_res:
			sheet.write(row,8,case_case[0]) #写第8列
			sheet.write(row,9,case_case[1]) #写第九列
			row+=1
		new_book.save(self.file_path.replace('xlsx','xls'))

	# 将数据拆分成map
	def dataToDict(self,data):
		#把数据转成字典
		res = {}
		data = data.split(',')
		for d in data:
			#a=
			k,v = d.split('=')
			res[k]=v
		return res

