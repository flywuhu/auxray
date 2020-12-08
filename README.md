# auxray
一键实现xray批量扫描+被动扫描

~~~python
print(
    '''
    Usage: python3 auxray.py -h    #查看帮助
           python3 auxray.py -r <filepath> -a    #开启主动模式进行批量扫描
           python3 auxray.py -p    #开启xray的被动扫描模式
    '''
  )

一、auxray.py需要和xray放在同一文件夹，如xray的名称不同，可以进入源码修改（或者直接将xray加入环境变量）。

二、Xray被动扫描配置，推荐使用BurpSuite的passive-scan-client插件来进行转发。
https://github.com/c0ny1/passive-scan-client/releases/tag/0.1












