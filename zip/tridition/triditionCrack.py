# -*- coding:utf-8 -*-  
import os
import subprocess
import zipfile
#假设6位纯数字密码,如果密码不确定可以使用字典跑包
def brutecrack():
	for a in range(1,10):
		for b in range(1,10):
			for c in range(1,10):
				for d in range(1,10):
					for e in range(1,10):
						for f in range(1,10):
							passwd=str(a)+str(b)+str(c)+str(d)+str(e)+str(f)
							command='unzip -P '+ passwd +' -d E:/zip/ F:/Data/github/brutecrack/zip/tridition/tridition.zip' #unzip只能解压 传统模式的加密方式，使用范围窄;当用户使用默认方式压缩 设置密码时,不能使用unzip命令循环爆破,所以有局限
							print(passwd)
							child=subprocess.call(command)
							#os.popen(command)#这个也可以用,但是不好监控解压状态
							print(child)
							if child==0:
								print("密码为："+passwd)
								return
if __name__ == '__main__':
	brutecrack()