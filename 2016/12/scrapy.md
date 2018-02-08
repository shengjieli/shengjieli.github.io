# scrapy爬虫一定会用到的小技巧

处处是坑，且用且珍惜

入坑Python爬虫已经一周多了，哦，不对，这篇文章本打算上周末写的，然而周末总是过的很快（相信都深有体会，哈哈），结果写了个框架，内容一点也没填，所以，到现在应该是已经两周多了。踩了很多坑，谨以此文纪念我一周多的Python的Scrapy爬虫

## scrapy入门

文档（0.24中文）：http://scrapy-chs.readthedocs.io/zh_CN/0.24/index.html
文档（1.2英文）：https://doc.scrapy.org/en/1.2/index.html

写了好多了，感觉停不下来了，还是另写一篇入门文章吧，写好后链接更新到这里
今天还是先把上周挖好的坑填了吧


## scrapy的meta
scrapy的meta的作用就是在执行`scrapy.Request()`函数时把一些回掉函数中需要的数据传进去，meta必须是一个字典，在下一个函数中可以使用`response.meta`防问
如：

```python
def parse(self, response):
  yield scrapy.Request(url='baidu.com', callback=detailpage, meta={website:'百度'})
def detailpage(self, response):
  website = response.meta['website']
```

## Python中的json解析：

爬虫离不了json的解析，很多传统网站中可能并不需要，但是目前很多新网站中都使用json进行数据传输，动态展现，所以json的解析对于爬虫是很重要的

python解析json的包是json，使用时需要先引入json包
`import json`
常用的三个函数load(),loads(),dumps()
json.loads()：传入一个json字符串，返回一个字符串解析出来的list或dict
json.load()：这货长的和json.loads()很像，但是绝对不一样，这个函数的作用是从文件中读取json并解析成dict或list
json.dumps()：把一个dict或list转换成字符串，相当于json.loads()的逆向过程
还有一个json.dump()：与文件操作结合的，实际中用的不多，不再介绍
例：

```python
import json
dict = {'name':'qitiandasheng','age':18}
str = json.dumps(dict)
data = json.loads(str)
with open('test.json','w') as f:
  data = json.load(f)
```

## 字符串函数：

常见的字符串处理函数：
replace()：字符串类型才有这个函数，传入两个参数，第一个是需要替换的字符串，第二个是替换成什么，会循环替换所有匹配到的字符串
strip()：去除左右两边的空字符

##正则表达式：

对于字符串处理，还有更强大的正则表达式，python中要使用正则表达式，需要先引入re模块
`import re`
Python中正则表达式有两种使用方式，一种是通过re模块的`compile()`函数先生成一个正则表达式对象，然后用这个正则表达式对象去匹配字符串，这种方式调用函数时不需要传入正则表达式，当一个正则表达式需要重复多次使用时建议使用此方式，他会先编译正则表达式，然后再去匹配，速度想对较快；还有一种方式是直接使用re模块的各个函数，第一个参数需要传入正则表达式

常用的四个函数：
re.compile()：传入正则表达式字符串，推荐使用r''的这种原始字符串，不需要对一些特定字符转义，此函数返回一个正则表达式对象
re.match()：**从字符串的开始处匹配**，匹配到返回match对象
re.search()：从任意字符处开始匹配，匹配到就返回一个match对象
re.findall()：从任意字符处开始匹配，匹配到所有的结果，返回一个list

`match()`和`search()`返回的是一个match对象，有`group()`和`groups()`两个方法：
group()：不传参数时相当于group(0)返回所有匹配的结果，当传入数字时，如group(1)，返回第1组括号匹配到的结果
groups()：以tuple形式返回所有匹配到的结果


`re.findall()`的返回结果：
list中每个元素的值的类型，取决于正则表达式的写法
当list中元素是字符串时：你的正则表达式中没有捕获的组（不分组，或非捕获分组）
字符串的值就是你的正则表达式所匹配到的单个完整的字符串
当list中元素是tuple时：你的正则表达式中有（带捕获的）分组（简单可理解为有括号）
tuple的值，是各个group的值所组合出来的


https://m.baidu.com/feed/data/landingpage?nid=2740700877946007370&n_type=1&p_from=2&type=share


## 换行符^M

一大坑，windows和linux换行符不同，在windows上编辑的文件上传到linux上就会多一个^M符号

## 爬过的页面不会再爬

scrpay有个机制，在一个spider中，当一个向一个url发送请求之后，如果再次请求该url，scrapy不在处理

## allowed domains

生成spider时，会在allowed domains中加入允许访问的域名，如果在此spider中访问改域名外的url，scrapy不会请求

## fiddler的https配置

首先要配置fiddler抓取https的包：

![Paste_Image.png](http://upload-images.jianshu.io/upload_images/2795025-76c0438b8cea83e1.png?imageMogr2/auto-orient/strip%7CimageView2/2/w/1240)

然后，在手机上输入，代理ip和端口，如192.168.1.5:8888，点击FiddlerRootcertificate安装证书，就可以抓取https的数据包了

python新手常见错误：https://www.oschina.net/question/89964_62779


做过两年多公众号的我写东西尽然毫无排版，哈哈哈哈
终于写完了，睡觉zzz

2016.12.04 01:26
北京

