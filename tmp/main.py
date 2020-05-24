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