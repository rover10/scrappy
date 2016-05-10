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
    if found and brandPage is not None:
        comUrl = line[ brandPage.end(): re.search(r'>',line[brandPage.end():]).start() + brandPage.end()]
        compList.append(comUrl)
    if found and re.search(r"</table>", line) is not None:
        print "OUT!"
        break
    
print compList
mobUriList = []
for uri in compList:
    response =  urllib2.urlopen("http://www.gsmarena.com/" + uri)
    #print(response)
    found = False
    for line in response:
        if re.search(r"nav-pages", line) is not None:
            found=True
        mobPage = re.search(r"href=", line)
        if found and mobPage is not None:
            mobUri = line[ mobPage.end(): re.search(r'>',line[mobPage.end():]).start() + mobPage.end()]    
            mobUriList.append(mobUri)
        if found and re.search(r"</div>", line):
            break
        
            
print mobUriList
#reads all 
mobUrlList.extend(compList)

