import urllib3

url = 'http://www.oldbaileyonline.org/browse.jsp?id=t17800628-33&div=t17800628-33'

response = urllib2.urlopen(url)
webContent = response.read()

f = open('obo-t17800628-33.html', 'w')
f.write(webContent)
f.close
#
# import urllib2
# import html2text
# url=''
# page = urllib2.urlopen(url)
# html_content = page.read()
# rendered_content = html2text.html2text(html_content)
# file = open('file_text.txt', 'w')
# file.write(rendered_content)
# file.close()

#
# import html2text
# html = open("foobar.html").read()
# print html2text.html2text(html)