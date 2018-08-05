# -*- coding:utf-8 -*-  
import os
import subprocess
import zipfile
def brutecrack():
	for a in range(1,10):
		for b in range(1,10):
			for c in range(1,10):
				for d in range(1,10):
					for e in range(1,10):
						for f in range(1,10):
							passwd=str(a)+str(b)+str(c)+str(d)+str(e)+str(f)
							command='7z -p'+passwd+' t F:/Data/github/brutecrack/zip/ordinary/ord.zip'  #t 表示test，不进行实际解压，只测试密码
							print(passwd)
							child=subprocess.call(command)
							#os.popen(command)#这个也可以用,但是不好监控解压状态
							print(child)
							if child==0:
								print("密码为："+passwd)
								return
if __name__ == '__main__':
	brutecrack()