import sys, time, requests

"""
Task: 0002-PG
Priority: Medium
Deadline: 2023-10-15
Task Given To: @Altorx @Morpheus 
Task Given By: @I2rys 
Programming Language (s) Scope: Python, NodeJS
Task (s): Make a tool to find all params, API endpoints on a website including external ones (Recursive. If you can).

Date of make: 20/10/2023 (DD/MM/YY) late by: 5 days
I will be using python for this.

- Fuck Morpheus
"""

class color:
    end = '\033[0m'
    bold = '\033[1m'
    Spartan = '\033[38;5;196m'
    quotecolor = '\033[38;5;226m'
    blue = '\033[38;5;33m'
    green = '\033[38;5;40m'


banner = color.bold + color.Spartan + """
                                           ..^!?Y5PGGBGGGP5~ .:..                                   
                                      .  P&@@@@@@@@@@@@@@@@~J@@@@&B57^.                             
                                   .7B@#.&@@@@@@@@@@@@@@@@&&@@@@@@@@@@@#Y:                          
                                 ^G@@@@@G#@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@&J                        
                               ~#@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@&P7:                        
                             ^#@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@B7.                            
                            P@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@#7.                               
                          .&@@@@@@@@@@@@@@@@&#BBBBB###BBBBBBB&@@5:                                  
                         :@@@@@@@@@@@@@@@&#&&@@@@@@@@@@@@@@@&&7                                     
                        .&@@@@@@@@@@@@@&&@@@@@@@@@@@@@@@@@@@@&                                      
                        P@@@@@@@@@@@@@@@@@@@&#GPPGGGGPPPPG#&&.                                      
                       .&@@@@@@@@@@@@@@@@&GPG#&@@@@@@@@@&#P?:                                       
                       .Y#@@@@@@@@@@@@@&G#@@@@@@@@@@@@@@@@@@@#!.7B                                  
                       J@@@@@@@@@@@@@@B&@@@@@@@@@@@@@@@@@@@@@@@@@@.                                 
                       J@@@@@@@@@@@@@B@@@@@@@@@@@@@@@@@@@@@@@@@@@@~                                 
                       ~@@@@@@@@@@@@#@@@@@@@@@@@@@@@@@@@&@@@@@@@@@J                                 
                       .@@@@@@@@@@@@&@@@@@@@@@@@@@@@&&@@@@@@@@@@@@B                                 
                        JG&@@@@@&?!~G@@@@@@@@@@&&&@@@@@@@@@@@@@@@@&                                 
                        .&@@@@@?    ~@@@@&&&&&@@@@@@@@@@@@@@@@@@@@@:                                
                        .@@@@#.     ?@@@@@@@@@@@@@@@@@@@@@5B#B&@@@@7                                
                         ^@@G        G@@@@@@@@@@@@@@@@@@@?P@&7^^~Y@G                                
                          ^#         .@@@@@@&&&&@@@@@@@@@&#GPGPPP~7&                                
                                      ^@@@@@@@7J@@@@@@@@@@@@@@&#G^7@.                               
                                      .@@@@@@?  &@@@@@@@@@@@@@@@@5?@^                               
                                     .B@@@@@!   Y@@@@@@@@@@@@@@@@B~@7                               
                                   .J@@@@@5.    B@@@@@@@@@@@@@@@@&7#:                               
                                   .J55J^      .#@@@@@@@@@@@@@@@@&?@~                               
                                                 .7B@@@@@@@@@@@@@@!@P                               
                                                    .!G@@@@@@@@@@@7&@                               
                                                       .~G&@@@@@@@BJ@P                              
                                                           ^Y#@@@@@5G@P                             
                                                              .7B&@@BG&5                            
                                                                  :7P?                              
""" + color.end

for char in banner:
    sys.stdout.write(char)
    sys.stdout.flush()
    time.sleep(0.000001)

print(f"{color.quotecolor}Discovering secrets with Hercules.{color.end}".center(125))

def log(i, msg):
    if i == "*":
        print(f"{color.blue}[*]{color.end} {msg}")
    elif i == "+":
        print(f"{color.green}[+]{color.end} {msg}")
    elif i == "-":
        print(f"{color.Spartan}[-]{color.end} {msg}")
    elif i == "!":
        print(f"{color.bold}[!]{color.end} {msg}")

url = input(f"\n{color.bold}Enter the URL of the website you want to scan: {color.end}")

if not url.startswith("http://") and not url.startswith("https://"):
    url = "http://" + url

try:
    requests.get(url)
except:
    log("-", "Invalid URL")
    exit()

log("*", "URL is valid")

log("*", "Starting to scan for endpoints\n")

endpoints = open("endpoints.txt", "r").read().splitlines()

foundendpoints = []
notfoundendpoints = []

for endpoint in endpoints:
    try:
        r = requests.get(url + endpoint)
        if "404" or "Not Found" in r.text:
            log("-", f"Endpoint {url + endpoint} not found")
            notfoundendpoints.append(url + endpoint)
        else:
            log("+", f"Found endpoint {url + endpoint}")
            foundendpoints.append(url + endpoint)
    except KeyboardInterrupt:
        log("+", "Exiting")
        exit()
    except:
        log("-", f"Endpoint {url + endpoint} not found")
        notfoundendpoints.append(url + endpoint)

log("*", "Starting to scan for params\n")

params = open("params.txt", "r").read().splitlines()

foundparams = []
notfoundparams = []

for param in params:
    try:
        r = requests.get(url + "?" + param)
        if "404" or "Not Found" in r.text:
            log("-", f"Param {param} not found")
            notfoundparams.append(param)
        else:
            log("+", f"Found param {param}")
            foundparams.append(param)
    except KeyboardInterrupt:
        log("+", "Exiting")
        exit()
    except:
        log("-", f"Param {param} not found")
        notfoundparams.append(param)

log("*", "Done scanning\n")

print(f"{color.bold}Found endpoints:{color.end}")
for endpoint in foundendpoints:
    print(f"{color.green}[+]{color.end} {endpoint}")

print(f"{color.bold}\nNot found endpoints:{color.end}")
for endpoint in notfoundendpoints:
    print(f"{color.Spartan}[-]{color.end} {endpoint}")

print(f"{color.bold}\nFound params:{color.end}")
for param in foundparams:
    print(f"{color.green}[+]{color.end} {param}")

print(f"{color.bold}\nNot found params:{color.end}")
for param in notfoundparams:
    print(f"{color.Spartan}[-]{color.end} {param}")

asktosave = input(f"{color.bold}\nDo you want to save the results? (y/n): {color.end}")
if asktosave == "y":
    foldername = url
    with open(foldername + "/Found Endpoints.txt", "w") as f:
        for endpoint in foundendpoints:
            f.write(endpoint + "\n")

    with open(foldername + "/Not Found Endpoints.txt", "w") as f:
        for endpoint in notfoundendpoints:
            f.write(endpoint + "\n")

    with open(foldername + "/Found Params.txt", "w") as f:
        for param in foundparams:
            f.write(param + "\n")

    with open(foldername + "/Not Found Params.txt", "w") as f:
        for param in notfoundparams:
            f.write(param + "\n")

    log("+", "Saved results")

log("+", "Exiting")
exit()

# Made by Altorx
# Fuck you Morpheus