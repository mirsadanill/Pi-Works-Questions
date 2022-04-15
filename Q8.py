def controller(url):
    
    alphanumeric = 'abcdefghijklmnopqrstuvwxyz'
    alphanumeric += alphanumeric.upper()
    alphanumeric += '123456789._'
    
    if url.startswith('<url>') and url.endswith('</url>'):
        url = url.strip('<url>').strip('</url>')
    else:
        return False
    
    if '://' in url:
        protocol, address = url.split('://')
        if not protocol.islower():
            return False
    else: return False
        
    for char in address:
        if not char in alphanumeric:
            return False
        
    return True
    
urls = ['<url>https://xcd32112.smart_meter.com</url>']
results = list()

for url in urls:
    result = controller(url)
    results.append(result)

print(list(zip(urls, results)))