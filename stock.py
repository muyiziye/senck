#!/usr/bin/env python

from os import path,sep
from argparse import ArgumentParser
import urllib2
from urllib2 import Request
from urllib2 import urlopen
import re
import random
import time

user_agent = ["Mozilla/5.0 (Windows NT 10.0; WOW64)", 'Mozilla/5.0 (Windows NT 6.3; WOW64)',
              'Mozilla/5.0 (Windows NT 6.1) AppleWebKit/537.11 (KHTML, like Gecko) Chrome/23.0.1271.64 Safari/537.11',
              'Mozilla/5.0 (Windows NT 6.3; WOW64; Trident/7.0; rv:11.0) like Gecko',
              'Mozilla/5.0 (Windows NT 5.1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/28.0.1500.95 Safari/537.36',
              'Mozilla/5.0 (Windows NT 6.1; WOW64; Trident/7.0; SLCC2; .NET CLR 2.0.50727; .NET CLR 3.5.30729; .NET CLR 3.0.30729; Media Center PC 6.0; .NET4.0C; rv:11.0) like Gecko)',
              'Mozilla/5.0 (Windows; U; Windows NT 5.2) Gecko/2008070208 Firefox/3.0.1',
              'Mozilla/5.0 (Windows; U; Windows NT 5.1) Gecko/20070309 Firefox/2.0.0.3',
              'Mozilla/5.0 (Windows; U; Windows NT 5.1) Gecko/20070803 Firefox/1.5.0.12',
              'Opera/9.27 (Windows NT 5.2; U; zh-cn)',
              'Mozilla/5.0 (Macintosh; PPC Mac OS X; U; en) Opera 8.0',
              'Opera/8.0 (Macintosh; PPC Mac OS X; U; en)',
              'Mozilla/5.0 (Windows; U; Windows NT 5.1; en-US; rv:1.8.1.12) Gecko/20080219 Firefox/2.0.0.12 Navigator/9.0.0.6',
              'Mozilla/4.0 (compatible; MSIE 8.0; Windows NT 6.1; Win64; x64; Trident/4.0)',
              'Mozilla/4.0 (compatible; MSIE 8.0; Windows NT 6.1; Trident/4.0)',
              'Mozilla/5.0 (compatible; MSIE 10.0; Windows NT 6.1; WOW64; Trident/6.0; SLCC2; .NET CLR 2.0.50727; .NET CLR 3.5.30729; .NET CLR 3.0.30729; Media Center PC 6.0; InfoPath.2; .NET4.0C; .NET4.0E)',
              'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.1 (KHTML, like Gecko) Maxthon/4.0.6.2000 Chrome/26.0.1410.43 Safari/537.1 ',
              'Mozilla/5.0 (compatible; MSIE 10.0; Windows NT 6.1; WOW64; Trident/6.0; SLCC2; .NET CLR 2.0.50727; .NET CLR 3.5.30729; .NET CLR 3.0.30729; Media Center PC 6.0; InfoPath.2; .NET4.0C; .NET4.0E; QQBrowser/7.3.9825.400)',
              'Mozilla/5.0 (Windows NT 6.1; WOW64; rv:21.0) Gecko/20100101 Firefox/21.0 ',
              'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.1 (KHTML, like Gecko) Chrome/21.0.1180.92 Safari/537.1 LBBROWSER',
              'Mozilla/5.0 (compatible; MSIE 10.0; Windows NT 6.1; WOW64; Trident/6.0; BIDUBrowser 2.x)',
              'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/536.11 (KHTML, like Gecko) Chrome/20.0.1132.11 TaoBrowser/3.0 Safari/536.11']

def parse_argument():
	"""
	This function just deal with the argument
	"""
	parser = ArgumentParser()
	parser.add_argument(
		"-n", "--nopar", help="Just input -n without parameter", action="store_true")
	parser.add_argument(
                "-p", "--pagenum", help="page number of stock, num0:page0-page9; num1:page10-page19")
	arg = parser.parse_args()
	return arg

def get_stock_list(page_num):
    stock_total = []
    page_num = int(page_num)
    for i in (range(page_num*10, page_num*10+9)):
        url='http://quote.stockstar.com/stock/ranklist_a_3_1_'+str(i)+'.html'
        myrequest=Request(url=url,headers={"User-Agent":random.choice(user_agent)})
        try:       
            response=urlopen(myrequest, timeout=10)
        except:
            continue
        content=response.read()       
        print('get page',i)                  
        pattern=re.compile('<tbody[\s\S]*</tbody>') 
        #body=re.findall(pattern,str(content))
        body=pattern.findall(str(content))
        if not body:
            continue
        pattern=re.compile('>(.*?)<')
        stock_page=re.findall(pattern,body[0])      
        stock_total.extend(stock_page)
    stock_list=stock_total[:] 
    for data in stock_total:
        if '' == data:
            stock_list.remove(data)
    return stock_list


if __name__ == "__main__":
    dict_fvt = {}
    args = parse_argument()
    if args.nopar:
        print(args.nopar)
    if args.pagenum:
        print(get_stock_list(args.pagenum))
    else:
        print("pls input ./scotk -h to get help information")

