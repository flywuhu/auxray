import os
import sys
import time

def batch_xray(ip):
  name=ip.replace('https://', '').replace('http://', '').replace('/', '')
  exp=(("xray_windows_amd64.exe webscan --basic-crawler {0}/ --html-output {1}.html").format(ip,name))
  os.system(exp)

def active_scan(ipaddr):
  print("[-] 模式：主动扫描")
  print("[-] 开始扫描...")
  if ipaddr == 0:
    print("[-] 请使用 -r <filepath>指定待扫描IP！")
  elif os.path.exists(ipaddr):
    with open(ipaddr, 'r') as file:
      list = [www.strip() for www in file.readlines()]
    for ip in list:
      batch_xray(ip.rstrip('/'))
      print("[+] " + ip + "扫描完成！")
  else:
    print("[-] 指定文件不存在！")

def passive_scan(port):
  print("[-] 模式：被动扫描")
  print("[-] 开始监听...")
  date_name = time.strftime('%Y-%m-%d-%H%M', time.localtime(time.time()))
  exp = (("xray_windows_amd64.exe webscan --listen 127.0.0.1:{0}  --html-output {1}.html").format(port,date_name))
  print(exp)
  os.system(exp)


if __name__ == "__main__":

  print(
    '''                     
  _|_|                                                      
_|    _|  _|    _|  _|    _|  _|  _|_|    _|_|_|  _|    _|  
_|_|_|_|  _|    _|    _|_|    _|_|      _|    _|  _|    _|  
_|    _|  _|    _|  _|    _|  _|        _|    _|  _|    _|  
_|    _|    _|_|_|  _|    _|  _|          _|_|_|    _|_|_|  
                                                        _|  
                                                    _|_| 
                                                    
                                          ——Author:FlyWuhu

    '''
    )

if len(sys.argv) == 1:print("[-] 无参数项，输入-h查看帮助...")

argv = [a for a in sys.argv]
ipaddr = 0
if "-h" in argv:
  print(
    '''
    Usage: python3 auxray.py -h    #查看帮助
           python3 auxray.py -r <filepath> -a    #开启主动模式进行批量扫描
           python3 auxray.py -p    #开启xray的被动扫描模式
    '''
  )
if "-r" in argv:ipaddr=argv[argv.index("-r")+1]    #获取-r 后面的参数值
if "-a" in argv:active_scan(ipaddr)    #-a 主动扫描模式
if "-p" in argv:passive_scan(argv[argv.index("-p")+1])    #-p 被动扫描模式



"""
Xray被动扫描设置，推荐使用BurpSuite插件来进行转发
https://github.com/c0ny1/passive-scan-client/releases/tag/0.1
"""
