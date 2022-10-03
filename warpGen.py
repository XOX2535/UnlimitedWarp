# Import Modules
import json
import datetime
import time , requests , random , string
import urllib
from sys import argv

# Generate a random number
def rand_number():
    return str(random.randint(1,999))

# Generate a random string
def rand_string(number):
    text = string.ascii_letters + string.digits
    result= ''.join(random.choice(text) for ch in range(number))
    return result

# Generate a random session with Cloudflare API
session = requests.Session()
url = "https://api.cloudflareclient.com/v0a%s/reg" % rand_number()

# Generate WARP+ references
def warp_unlimited(id_code):
    inst = rand_string(22)
    body = {"key": "{}=".format(rand_string(43)),
        "install_id": inst,
        "fcm_token": "{}:APA91b{}".format(inst, rand_string(134)),
        "referrer": id_code,
        "warp_enabled": False,
        "locale": "es_US"}
    data = json.dumps(body).encode('utf8')
    header = {'Content-Type': 'application/json; charset=UTF-8',
        'User-Agent': 'okhttp/3.12.1'
        }
    try:
        req = urllib.request.Request(url , data , header)
        resp = urllib.request.urlopen(req)
    except urllib.error.HTTPError:
        time.sleep(5)

# CLI
if len(argv) == 1:
    from pyfiglet import Figlet
    from rainbowtext import text
    from colorama import Fore

    print (text(Figlet(font="whimsy").renderText("Warp Fox")))
    print (Fore.RED + "[$] Created By Maximum Radikali")
    print (Fore.GREEN + "[$] Channel : @BlackFoxSecurityTeam")
    print (Fore.LIGHTMAGENTA_EX + "[&] Warp Plus Unlimited Script ! ")
    print (Fore.YELLOW + "=====================================") ; code_id = input(Fore.CYAN + "[+] Please Enter Your Client ID : ")

    while True:
        try:
            warp_unlimited(code_id)
            print ( Fore.GREEN + "Success ! You Got 1GB Warp + \n" + Fore.MAGENTA + "Please Wait 17 Second !")        
            time.sleep(17)

        except KeyboardInterrupt:
            print (Fore.Red + "Stopped ! ")
            break

else:
    print ("Warp Plus Unlimited Script ! ")
    print ("Created By Maximum Radikali")
    print ("Channel : @BlackFoxSecurityTeam")
    
    if argv[1] == "ext":
        import warpID
        while True:
            warp_unlimited(warpID.WARP)
            print ("Success ! You Got 1GB Warp + \n" + "Please Wait 17 Second !")        
            time.sleep(17)
    else:
        while True:
            warp_unlimited(argv[1])
            print ("Success ! You Got 1GB Warp + \n" + "Please Wait 17 Second !")        
            time.sleep(17)