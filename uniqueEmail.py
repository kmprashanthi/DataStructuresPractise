def numUniqueEmails(emails):
    result = []
    for email in emails:
        localName, domainName= email.split('@')
        localName = localName.replace('.','')
        try : 
            localName = localName[:localName.index('+')]
        except:
            localName = localName
        result.append(localName+'@'+domainName)
    
    return list(set(result))
        

print (numUniqueEmails(['test.e.mail+bob.cathy@leetcode.com']))