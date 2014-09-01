# coding:utf-8

from selenium import webdriver
import time


wd = webdriver.Firefox()
wd.get("http://www.duokan.com/reader/www/app.html?id=51e4d3517ce44ca2a43a62d696891ad2")  # 换成书的在线阅读地址

pagecount = 381   # 换成书的总页数
content = ''
for i in range(1, pagecount / 2 + 1):
	wd.execute_script("$('.u-layer .j-close').trigger('click')")
	while wd.execute_script("return $('#book_page_%s text').length" % str(i * 2)) == 0 and wd.execute_script("return $('#book_page_%s .text').length" % str(i * 2)) == 0:
		time.sleep(0.2)
	content += wd.execute_script("var content = '';$('#book_page_%s text').each(function(){content += $(this).text()});return content;" % str(i * 2))
	if i * 2 + 1 > pagecount:
		break
	content += wd.execute_script("var content = '';$('#book_page_%s text').each(function(){content += $(this).text()});return content;" % str(i * 2 + 1))
	wd.execute_script("$('.j-pagedown').trigger('click')")
wd.close()
print content
with open('book', 'w') as f:
	f.write(content.encode('utf-8'))
