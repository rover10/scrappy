import urllib2
import re
response = urllib2.urlopen('http://www.gsmarena.com/makers.php3')
#html = response.read()
found = False
compList = []
for line in response:
    #print line
    reMobCom = re.search(r"st-text", line)
    if reMobCom is not None:
        print line
        found = True
        
    brandPage = re.search(r"href=", line)
    if found is True and brandPage is not None:
        comUrl = line[ brandPage.end(): re.search(r'>',line[brandPage.end():]).start() + brandPage.end()]
        compList.append(comUrl)
    if found is True and re.search(r"</table>", line) is not None:
        print "OUT!"
        break
    
print compList
for uri in compList:
    response =  urllib2.urlopen("http://www.gsmarena.com/" + uri)
    print(response)
