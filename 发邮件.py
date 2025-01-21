#import smtplib

#server = smtplib.SMTP()
#server.connect(host, port)
#server.login(username, password) 
#server.sendmail(from_addr, to_addr, msg.as_string()) 
#server.quit() 



#初级版本：
# smtplib 用于邮件的发信动作
import smtplib
from email.mime.text import MIMEText
# email 用于构建邮件内容

# 发信方的信息：发信邮箱，QQ 邮箱授权码
from_addr = 'xxx@qq.com'
password = '你的授权码数字'

# 收信方邮箱
to_addr = 'xxx@qq.com'

# 发信服务器
smtp_server = 'smtp.qq.com'

# 邮箱正文内容，第一个参数为内容，第二个参数为格式(plain 为纯文本)，第三个参数为编码
msg = MIMEText('send by python','plain','utf-8')

# 开启发信服务，这里使用的是加密传输
server = smtplib.SMTP_SSL()
server.connect(smtp_server,465)
# 登录发信邮箱
server.login(from_addr, password)
# 发送邮件
server.sendmail(from_addr, to_addr, msg.as_string())
# 关闭服务器
server.quit()




#中级版本
# smtplib 用于邮件的发信动作
import smtplib
from email.mime.text import MIMEText
# email 用于构建邮件内容
from email.header import Header
# 用于构建邮件头

# 发信方的信息：发信邮箱，QQ 邮箱授权码
from_addr = 'xxx@qq.com'
password = '你的授权码数字'

# 收信方邮箱
to_addr = 'xxx@qq.com'

# 发信服务器
smtp_server = 'smtp.qq.com'

# 邮箱正文内容，第一个参数为内容，第二个参数为格式(plain 为纯文本)，第三个参数为编码
msg = MIMEText('send by python','plain','utf-8')

# 邮件头信息
msg['From'] = Header(from_addr)
msg['To'] = Header(to_addr)
msg['Subject'] = Header('python test')

# 开启发信服务，这里使用的是加密传输
server = smtplib.SMTP_SSL()
server.connect(smtp_server,465)
# 登录发信邮箱
server.login(from_addr, password)
# 发送邮件
server.sendmail(from_addr, to_addr, msg.as_string())
# 关闭服务器
server.quit()





#次终极版本
# smtplib 用于邮件的发信动作
import smtplib
from email.mime.text import MIMEText
# email 用于构建邮件内容
from email.header import Header
# 用于构建邮件头

# 发信方的信息：发信邮箱，QQ邮箱授权码）
from_addr = 'xxx@qq.com'
password = '你的授权码数字'

# 收信方邮箱
to_addr = 'xxx@qq.com'

# 发信服务器
smtp_server = 'smtp.qq.com'

# 邮箱正文内容，第一个参数为内容，第二个参数为格式(plain 为纯文本)，第三个参数为编码
text = '''亲爱的学员，你好！
​    我是吴枫老师，能遇见你很开心。
​    希望学习Python对你不是一件困难的事情！

人生苦短，我用Python
'''
msg = MIMEText(text,'plain','utf-8')

# 邮件头信息
msg['From'] = Header(from_addr)
msg['To'] = Header(to_addr)
msg['Subject'] = Header('python test')

# 开启发信服务，这里使用的是加密传输
server = smtplib.SMTP_SSL()
server.connect(smtp_server,465)
# 登录发信邮箱
server.login(from_addr, password)
# 发送邮件
server.sendmail(from_addr, to_addr, msg.as_string())
# 关闭服务器
server.quit()






#终极版本----群发1:设置一个列表形成的变量
# smtplib 用于邮件的发信动作
import smtplib
from email.mime.text import MIMEText
# email 用于构建邮件内容
from email.header import Header
# 用于构建邮件头

# 发信方的信息：发信邮箱，QQ邮箱授权码）
from_addr = 'xxx@qq.com'
password = '你的授权码数字'

# 收信方邮箱
to_addrs = ['wufeng@qq.com','kaxi@qq.com']

# 发信服务器
smtp_server = 'smtp.qq.com'

# 邮箱正文内容，第一个参数为内容，第二个参数为格式(plain 为纯文本)，第三个参数为编码
text='''亲爱的学员，你好！
​    我是吴枫老师，能遇见你很开心。
​    希望学习Python对你不是一件困难的事情！

人生苦短，我用Python
'''
msg = MIMEText(text,'plain','utf-8')

# 邮件头信息
msg['From'] = Header(from_addr)
msg['To'] = Header(",".join(to_addrs)) 
msg['Subject'] = Header('python test')

# 开启发信服务，这里使用的是加密传输
server = smtplib.SMTP_SSL()
server.connect(smtp_server,465)
# 登录发信邮箱
server.login(from_addr, password)
# 发送邮件
server.sendmail(from_addr, to_addr, msg.as_string())
# 关闭服务器
server.quit()





#终极版本----群发2:用while循环
# smtplib 用于邮件的发信动作
import smtplib
from email.mime.text import MIMEText
# email 用于构建邮件内容
from email.header import Header
# 用于构建邮件头

# 发信方的信息：发信邮箱，QQ 邮箱授权码
from_addr = input('请输入登录邮箱：')
password = input('请输入邮箱授权码：')

# 收信方邮箱
to_addrs = []
while True:
    a=input('请输入收件人邮箱：')
    to_addrs.append(a)
    b=input('是否继续输入，n退出，任意键继续：')
    if b == 'n':
        break

# 发信服务器
smtp_server = 'smtp.qq.com'

# 邮箱正文内容，第一个参数为内容，第二个参数为格式(plain 为纯文本)，第三个参数为编码
text='''亲爱的学员，你好！
我是吴枫老师，能遇见你很开心。
希望学习Python对你不是一件困难的事情！

人生苦短，我用Python
'''
msg = MIMEText(text,'plain','utf-8')

# 邮件头信息
msg['From'] = Header(from_addr)
msg['To'] = Header(",".join(to_addrs)) 
msg['Subject'] = Header('python test')

# 开启发信服务，这里使用的是加密传输
server = smtplib.SMTP_SSL(smtp_server)
server.connect(smtp_server,465)
# 登录发信邮箱
server.login(from_addr, password)
# 发送邮件
server.sendmail(from_addr, to_addrs, msg.as_string())
# 关闭服务器
server.quit()





#终极版本----群发3:用csv文档
import smtplib
# smtplib 用于邮件的发信动作
from email.mime.text import MIMEText
# email 用于构建邮件内容
from email.header import Header
# 用于构建邮件头
import csv
# 引用csv模块，用于读取邮箱信息

# 发信方的信息：发信邮箱，QQ邮箱授权码
# 方便起见，你也可以直接赋值
from_addr = input('请输入登录邮箱：')
password = input('请输入邮箱授权码：')

# 发信服务器
smtp_server = 'smtp.qq.com'

# 邮件内容
text='''亲爱的学员，你好！
我是吴枫老师，能遇见你很开心。
希望学习python对你不是一件困难的事情！

人生苦短，我用Python
'''

# 待写入csv文件的收件人数据：人名+邮箱
# 记得替换成你要发送的名字和邮箱
data = [['wufeng ', 'wufeng@qq.com'],['kaxi', 'kaxi@qq.com']]

# 写入收件人数据
with open('to_addrs.csv', 'w', newline='') as f:
    writer = csv.writer(f)
    for row in data:
        writer.writerow(row)

# 读取收件人数据，并启动写信和发信流程
with open('to_addrs.csv', 'r') as f:
    reader = csv.reader(f)
    for row in reader: 
        to_addrs=row[1]
        msg = MIMEText(text,'plain','utf-8')
        msg['From'] = Header(from_addr)
        msg['To'] = Header(to_addrs)
        msg['Subject'] = Header('python test')
        server = smtplib.SMTP_SSL()
        server.connect(smtp_server,465)
        server.login(from_addr, password)
        server.sendmail(from_addr, to_addrs, msg.as_string())
try:
    server.sendmail(from_addr, to_addrs, msg.as_string())
    print('恭喜，发送成功')
except:
    print('发送失败，请重试')
# 关闭服务器
server.quit()



#自己写的成功版本：
import smtplib
from email.mime.text import MIMEText
from email.header import Header


#server = smtplib.SMTP()
host = "smtp.qq.com"
port = 25
#server.connect(host,port)

username = input("please enter the username:\n")
#username = "1933262583@qq.com"
password = input("please enter the password:\n")
#password = "fmcydcjcioiifjii"
#server.login(username,password)

from_addr = username
#from_addr = "1933262583@qq.com"
to_addrs = []
while True:
    addr = input("please enter a receive email address:\n")
    to_addrs.append(addr)
    again = input("enter anything to keep enter, enter 'Q' to finish entering email:\n")
    if again == "Q":
        break
#to_addr = "158994970@qq.com"
#to_addr = "1933262583@qq.com"
#to_addr = "ZXC979@student.bham.ac.uk"
#to_addrs = ["1933262583@qq.com","ZXC979@student.bham.ac.uk"]   #群发邮件（缺点：每个人可以看到其他人的账号）


content = "mai mi dang ka"
#content = "自动化办公第一步成功！！！！"
my_type = "plain"
code = "utf-8"
msg = MIMEText(content,my_type,code)
#msg = MIMEText("hi this email is automatically sent by python!!!","plain","utf-8")
#server.sendmail(from_addr,to_addr,msg.as_string())

msg["From"] = Header(from_addr)
#msg["To"] = Header(to_addr)
msg["To"] = Header(",".join(to_addrs))
msg["Subject"] = Header("how are you today!!!")

server = smtplib.SMTP()
server.connect(host,port)
server.login(username,password)
#server.sendmail(from_addr,to_addrs,msg.as_string())
#server.quit()
try:
    server.sendmail(from_addr, to_addr, mag.as_string())
    print("successed!!!")
except:
    print("mission fail!!!")
server.quit()
'''
try:
    qqmail.sendmail(account, receiver, message.as_string())
    print ('邮件发送成功')
except:
    print ('邮件发送失败')
qqmail.quit()
'''