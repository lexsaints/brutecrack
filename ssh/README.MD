使用KALI机器暴力破解ssh登录密码 及防范方法

服务器遭到暴力破解的防范措施：
  1.服务器日志文件：
    Redhat版本：cat /var/log/secure 
    debian ：cat /var/log/syslog
    例如:使用192.168.172.128机器 ssh连接 192.168.172.165
    在165机器上，查看日志cat /var/log/secure
      Mar 20 17:10:07 localhost sshd[24014]: Failed password for root from 192.168.172.128 port 42610 ssh2
      Mar 20 17:10:08 localhost sshd[24014]: Failed password for root from 192.168.172.128 port 42610 ssh2
      Mar 20 17:10:08 localhost sshd[24014]: Failed password for root from 192.168.172.128 port 42610 ssh2
      Mar 20 17:10:08 localhost sshd[24015]: Connection closed by 192.168.172.128
      Mar 20 17:10:12 localhost unix_chkpwd[24019]: password check failed for user (root)
      Mar 20 17:10:12 localhost sshd[24017]: pam_unix(sshd:auth): authentication failure; logname= uid=0 euid=0 tty=ssh ruser= rhost=192.168.172.128  user=root
      Mar 20 17:10:14 localhost sshd[24017]: Failed password for root from 192.168.172.128 port 42612 ssh2
      Mar 20 20:09:03 localhost sshd[24360]: Accepted password for root from 192.168.172.1 port 51258 ssh2
      Mar 20 20:09:03 localhost sshd[24360]: pam_unix(sshd:session): session opened for user root by (uid=0)
  如日志内容所示，登录失败的记录会被系统记录下来，所以经常看一下自己的日志，可以发现自己的服务器是否遭到过暴力破解，从而可以提前防范。
