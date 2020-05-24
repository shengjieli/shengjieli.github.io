
标准库：urllib
```python
from urllib import request

import httpx


url = "http://httpbin.org/get"


def main():
    resp = request.urlopen(url)
    print(resp.status)
    print(resp.url)
    print(resp.headers)
    print(resp.read())


if __name__ == "__main__":
    main()
```



requests：HTTP for Humans
中文文档推荐：https://cn.python-requests.org/zh_CN/latest/
项目github地址：https://github.com/psf/requests
官方文档：https://requests.readthedocs.io/en/master/
```python
import json

import requests


def main():
    url = "https://httpbin.org/get"
    resp = requests.get(url)
    print(resp.status_code)
    print(resp.url)
    print(resp.history)
    print(resp.headers)
    print(resp.content)
    print(resp.text)
    print(resp.json())
    requests.put('https://httpbin.org/put', data = {'key':'value'})
    requests.delete('https://httpbin.org/delete')
    requests.head('https://httpbin.org/get')
    requests.options('https://httpbin.org/get')
    resp = requests.get(url="https://httpbin.org/get", params={"query": "test"})
    print(resp.json())
    resp = requests.post(url="https://httpbin.org/post", params={"query": "test"}, data={"key": "value"})
    print(resp.json())
    resp = requests.post(url="https://httpbin.org/post", json={"key": "value"})
    print(resp.json())
    files = {'file': open('test.txt', 'rb')}
    resp = requests.post(url="https://httpbin.org/post", files=files)
    print(resp.json())
    session = requests.Session()
    session.headers.update({"User-Agent": "I am spider man"})
    # proxies, cookies
    resp = session.get("https://httpbin.org/get")
    print(resp.json())


if __name__ == "__main__":
    main()

```


httpx：HTTPX is a fully featured HTTP client for Python 3, which provides sync and async APIs, and support for both HTTP/1.1 and HTTP/2.
github：https://github.com/encode/httpx
官方文档：https://www.python-httpx.org/


```python
import asyncio

import httpx


async def main():
    async with httpx.AsyncClient() as client:
        resp = await client.get("https://httpbin.org/get")
        print(resp.status_code)
        print(resp.url)
        print(resp.headers)
        print(resp.text)
        print(resp.content)
        print(resp.json())


if __name__ == "__main__":
    asyncio.run(main())


```

```python
import asyncio

import httpx


# url = "https://httpbin.org/get"?
url = "https://nghttp2.org/"


async def main():
    async with httpx.AsyncClient() as client:
        resp = await client.get(url)
        print(resp.http_version)
    async with httpx.AsyncClient(http2=True) as client:
        resp = await client.get(url)
        print(resp.http_version)


if __name__ == "__main__":
    asyncio.run(main())

```

aiohttp：Asynchronous HTTP Client/Server for asyncio and Python.
github：https://github.com/aio-libs/aiohttp
官方文档：https://docs.aiohttp.org/

lxml：

```python
import requests
from lxml.etree import HTML


def main():
    resp = requests.get("xxxx")
    html = HTML(resp.text)
    # html.cssselect('div#head .mnav > p')
    ele = html.xpath('//div[@id="head"]/p')
    print(ele.text)
    print(ele.tag)
    print(ele.attrib)


if __name__ == "__main__":
    main()
```

xpath：https://cuiqingcai.com/5545.html
lxml and xpath：https://cuiqingcai.com/2621.html


控制浏览器：效率较低，占用资源高，不需要破解js加密参数，浏览器检测，cookie等
selenium

chrome headless


https://github.com/kennethreitz/requests-html
爬虫全家桶：
requests：HTTP 客户端
pyquery：可以使用jQuery的语法解析HTML
fake-useragent：User-Agent
bs4：解析HTML

https://httpbin.org/
https://cuiqingcai.com/

