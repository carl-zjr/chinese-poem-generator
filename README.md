# chinese-poem-generator
Chinese poetry generator based on LSTM and Seq2Seq
![avatar](/graph/net.png)

# 计算机网络
## OSI参考模型与TCP/IP四层模型
- 每层对应的常见协议
![image.png](/uploads/B2CFD55D535049E88434C4D18E25B1A1/image.png)
<br/>
## TCP3次握手、4次挥手
- 画图并简述过程
&emsp;&emsp;参考链接：https://hit-alibaba.github.io/interview/basic/network/TCP.html
- 为什么是3次握手？
&emsp;&emsp;1、防止已失效的链接请求报文段又到达服务端，发生错误
&emsp;&emsp;2、TCP连接支持全双工通信，若没有第3次握手，服务端无法确认客户端已知服务端就绪
- 连接3次，断开连接4次？
&emsp;&emsp;客户端发送断开连接请求，服务端应答后，需要完成未发送的数据传输才能断开连接
- TIME_WAIT的作用
&emsp;&emsp;当服务端未能接收到客户端的ACK包，可重传FIN包，之后客户端再次应答。这一过程需要收发报文段，因此TIME_WAIT的时间为2MSL
## TCP与UDP的区别
![image.png](/uploads/3C0B1CACF9C44E8FA7C82F10DFE62901/image.png)
<br/>
- TCP如何保证可靠传输
&emsp;&emsp;确认和重传：接收端收到数据后会确认，发送端超过某一时间未收到确认则重传
&emsp;&emsp;校验和：TCP报文头有校验和，用于校验数据是否损坏
&emsp;&emsp;数据合理分片和排序：按MTU合理分片
&emsp;&emsp;流量控制：让发送方的发送速率不要太快，接收方来得及接收
&emsp;&emsp;拥塞控制：慢开始、拥塞避免、快重传、快恢复
- 如何使不可靠的UDP可靠
&emsp;&emsp;1、添加SYN/ACK机制，确保数据发送到对端
&emsp;&emsp;2、添加超时重传机制
## 浏览器访问某一URL的流程
&emsp;&emsp;1、依次在浏览器DNS缓存、本地DNS缓存、Hosts文件中查找域名对应的ip，若无则调用DNS服务完成域名解析
&emsp;&emsp;2、建立TCP连接
&emsp;&emsp;3、客户端向服务端发送HTTP请求
&emsp;&emsp;4、服务端收到请求后发送HTTP响应
&emsp;&emsp;5、客户端浏览器解析并渲染出HTML页面
&emsp;&emsp;6、断开TCP连接
## HTTP与HTTPS的区别
&emsp;&emsp;1、HTTP是明文传输，HTTPS是密文传输
&emsp;&emsp;2、前者端口号是80，后者则是443
&emsp;&emsp;3、HTTP的响应速度比HTTPS快，更节省服务器资源
## HTTPS连接过程
&emsp;&emsp;1、客户端发送HTTPS请求
&emsp;&emsp;2、服务端返回证书，含公钥
&emsp;&emsp;3、客户端用公钥加密随机值并发送到服务端
&emsp;&emsp;4、服务端用私钥解密得到随机值，并用这一随机值加密信息后发送到客户端
&emsp;&emsp;5、客户端用随机值解密
## GET与POST的区别
&emsp;&emsp;1、GET方法显式提交数据，在URL中可见，POST方法则是放在请求体中
&emsp;&emsp;2、GET方法是安全且幂等的，POST方法则可能修改服务器状态
&emsp;&emsp;3、GET方法只有application/x-www-urlencoded编码类型，POST方法还有form/multipart-data
## 常见的状态码
- 10x：服务器正在处理请求
- 20x：请求正确处理完毕
- 30x：重定向以正确处理请求
- 40x：客户端错误
- 50x：服务器错误
## 常见的端口及对应的服务
- 21：FTP
- 22：SSH
- 23：TELNET
- 25：SMTP
- 53：DNS
- 80：HTTP
- 110：POP3
- 443：HTTPS
- 3306：MYSQL
## 私有（保留）地址
10.0.0.0 - 10.255.255.255
162.16.0.0 - 162.31.255.255
192.168.0.0 - 192.168.255.255
