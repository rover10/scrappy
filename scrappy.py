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
    
#print compList
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
            mobUri = line[ mobPage.end() +1 : re.search(r'>',line[mobPage.end():]).start() + mobPage.end() -1]    
            mobUriList.append(mobUri)
        if found and re.search(r"</div>", line):
            break
        
            
print mobUriList
            
print compList

#reads all 
# Urls of each brand and there pages 
#mobUriList.extend(compList)
for x in compList:
    mobUriList.append(x[1:len(x)-1])


#Make list individual pages of mobile phone.
mobDescPages = []
for uri in mobUriList:
    print "Reading url : " + "http://www.gsmarena.com/" + uri
    try:
        response =  urllib2.urlopen("http://www.gsmarena.com/" + uri)
    except urllib2.HTTPError, err:
        print "badUrl found"
        #response =  urllib2.urlopen("http://www.gsmarena.com/" + uri + "h")
    #print(response)
    found = False
    for line in response:
        if re.search(r"review-body", line) is not None:
            found=True
        mobPage = re.search(r"href=", line)
        if found and mobPage is not None:
            mobUri = line[ mobPage.end(): re.search(r'>',line[mobPage.end():]).start() + mobPage.end()]    
            mobDescPages.append(mobUri)
        if found and re.search(r"</div>", line):
            break


print "************"
print mobDescPages


print "***********"
        



