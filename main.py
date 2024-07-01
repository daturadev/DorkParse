#!/usr/bin python3
# utf-8
try:
    import random
    import time
    import pyuser_agent
    # import json
    from os import system, name, getcwd
    import proxyscrape
    import requests
    from colorama import Fore
except:
    print('''
    [!] Error: Module(s) not found.
    [!] Please install the required modules via pip.
    [!] pip install -r requirements.txt
    ''')
    pass
    time.sleep(2.7)
    exit(1)
# Proxyscrape INIT
collector = proxyscrape.create_collector('collector-1', 'socks4')

# Global variables
urls = []
root = getcwd() + "/"


# UAs
UA = pyuser_agent.UA()
browsers = UA.list
browser = random.choice(browsers)
UA.browser = browser


# Clear Screen
def cls():
    if name == 'nt':
        _ = system('cls')
        pass
    else:
        _ = system('clear')
        pass


print(Fore.MAGENTA + '''

            ╔╦╗╔═╗╦═╗╦╔═╔═╗╔═╗╦═╗╔═╗╔═╗  
             ║║║ ║╠╦╝╠╩╗╠═╝╠═╣╠╦╝╚═╗║╣   
            ═╩╝╚═╝╩╚═╩ ╩╩  ╩ ╩╩╚═╚═╝╚═╝ 
            ''')
print(Fore.BLUE + '''
   -------------------------------------------------- 
    A proxyless parsing solution for your dork-lists
    
                Developer: @daturadev
 =========================================================
 ''')
print(Fore.RED + '''
PROVIDED FREE AND OPEN-SOURCE ON GITHUB, DO NOT GET SCAMMED!
''')
time.sleep(random.randint(1, 3))
cls()

# Grab dork file
path = input('''
[?] Input path to dork-list:
Example: lib/dorks.txt

''')
file = root + path
cls()



# Parse Dorks
with open(file, 'r') as dork_file:
    for dork in dork_file:
        # Rotate proxies
        proxy = collector.get_proxy()
        ip = str(proxy.host)
        port = str(proxy.port)
        protocol = str(proxy.type)

        proxies = {
            "http": private_proxy,
            protocol: f"{protocol}://{ip}:{port}"
        }

        # Capture response elements, normalize, and append to [urls]
        with open(f'{root}lib/results.txt', 'w+'):
            # Credit: https://jereze.com/code/image-search-api/
            r = requests.get("https://api.qwant.com/v3/search",
                             params={
                                 'count': 10,
                                 'q': 'kittens',
                                 't': 'web',
                                 'safesearch': 'on',
                                 'locale': 'en_US',
                                 'offset': 0,
                                 'device': 'desktop'
                             },
                             headers={
                                 'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 '
                                               '(KHTML, like Gecko) Chrome/56.0.2924.87 Safari/537.36'
                             })
            response = r.json()
            # urls.append(response)
            print(Fore.GREEN + f"{response}\n")
            pass

# Helpful Article Credits:
# Structure/Manipulation of HTTP Requests & Responses | https://mleue.com/posts/simple-python-http-request-parser/
