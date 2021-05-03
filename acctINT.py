from termcolor import colored, cprint
import argparse
import requests
import json
import time
import sys


# ----------------------------------------
# INTRO TEXT
# ----------------------------------------

cprint(" ________  ________  ________ _________     ___  ________   _________", 'cyan')
cprint("|\   __  \|\   ____\|\   ____\\\\___   ___\  \ \\  \|\   ___  \|\___   ___\ ", 'cyan')
cprint("\ \  \|\  \ \  \___|\ \  \___\|___ \  \_    \ \  \ \  \\\ \  \|___ \  \_| ", 'cyan')
cprint(" \ \   __  \ \  \    \ \  \       \ \  \     \ \  \ \  \\\ \  \   \ \  \  ", 'cyan')
cprint("  \ \  \ \  \ \  \____\ \  \____   \ \  \     \ \  \ \  \\\ \  \   \ \  \ ", 'cyan')
cprint("   \ \__\ \__\ \_______\ \_______\  \ \__\ .   \ \__\ \__\\  \__\   \ \__\\", 'cyan')
cprint("                                                                     ", 'cyan')


parser = argparse.ArgumentParser()
parser.add_argument("-d", "--domain", help="Specify the parent domain", required=True)
parser.add_argument("--pwnedapi", help="API key for HIBP", required=True)
parser.add_argument("--huntapi", help="API key for hunter.io", required=True)
args = parser.parse_args()


if args.domain:

    # -------------------- ARG ASSIGNMENTS ---------------------------------------------
    domain = args.domain
    hunterapi = args.huntapi
    pwnedapi = args.pwnedapi
    acct_count = 0

    # -------------------- GREETING ---------------------------------------------
    cprint("----------------------------------------------------------------------------------------------------",'cyan')
    cprint("Finding accounts associated with "+domain+"",'cyan')
    cprint("----------------------------------------------------------------------------------------------------\n",'cyan')


    # -------------------- Hunter.io API PARAMETERS ---------------------------------------------

    request1 = "domain"
    hunterapi = args.huntapi

    headershunter = {
        'apikey': hunterapi,
        'accept': 'application/json'
    }

    headerspwned = {
        'hibp-api-key': pwnedapi,
        'accept': 'application/json'
    }


    # extract values
    def extract_values(obj, key):
        """Pull all values of specified key from nested JSON."""
        arr = []

        def extract(obj, arr, key):
            """Recursively search for values of key in JSON tree."""
            if isinstance(obj, dict):
                for k, v in obj.items():
                    if isinstance(v, (dict, list)):
                        extract(v, arr, key)
                    elif k == key:
                        arr.append(v)
            elif isinstance(obj, list):
                for item in obj:
                    extract(item, arr, key)
            return arr

        results = extract(obj, arr, key)
        return results


    #Account Count
    response = requests.get('https://api.hunter.io/v2/email-count?domain={domain}'.format(domain=domain), headers=headershunter)
    total = extract_values(response.json(), 'total')
    cprint(""+str(total)+" total accounts found:", 'blue')

    #Account Request
    responseHunter = requests.get('https://api.hunter.io/v2/domain-search?domain={domain}&api_key={hunterapi}&limit=1000000'.format(domain=domain, hunterapi=hunterapi), headers=headershunter)
    names = extract_values(responseHunter.json(), 'value')

    for i in names:
        cprint('    - '+i, 'magenta')

    cprint("\n----------------------------------------------------------------------------------------------------",'cyan')
    cprint("Starting footprint for "+domain+" accounts ",'cyan')
    cprint("----------------------------------------------------------------------------------------------------\n",'cyan')

    for i in names:
        
        cprint(""+i+" footprint:",'cyan')
        
        #----------------------SOURCE CHECKS----------------------
        cprint("     Sources:",'blue')
        responsejson = json.dumps(responseHunter.json())
        huntresponse = json.loads(responsejson)
        sources = huntresponse['data']['emails'][acct_count]['sources']
        source_count=0
        for x in sources:
            cprint("         - "+huntresponse['data']['emails'][acct_count]['sources'][source_count]['uri'], 'green')
            cprint("                   initially seen on: "+huntresponse['data']['emails'][acct_count]['sources'][source_count]['extracted_on'], 'green')
            cprint("                   last seen on: "+huntresponse['data']['emails'][acct_count]['sources'][source_count]['last_seen_on'], 'green')
            source_count = source_count+1
        acct_count = acct_count+1


        #----------------------BREACH CHECKS----------------------
        cprint("     Breaches:",'blue')
        response = requests.get('https://haveibeenpwned.com/api/v3/breachedaccount/{account}'.format(account=i), headers=headerspwned)
        

        if response.status_code == 404:
                cprint("         - None", 'green')
        else:
            breach_count=0
            responsejson = json.dumps(response.json())
            hibpresponse = json.loads(responsejson)
            breachinfo = hibpresponse
            for y in breachinfo:
                response = requests.get('https://haveibeenpwned.com/api/v3/breach/{name}'.format(name=hibpresponse[breach_count]['Name']))
                responsejson = json.dumps(response.json())
                breachinforesponse = json.loads(responsejson)

                cprint("         - "+breachinforesponse['Name'], 'green')
                cprint("                   Breach Date: "+breachinforesponse['BreachDate'], 'green')
                cprint("                   Data Compromised: "+str(breachinforesponse['DataClasses']), 'green')
                breach_count=breach_count+1
        time.sleep(2)


        #----------------------PASTE CHECKS----------------------
        cprint("     Pastes:",'blue')
        response = requests.get('https://haveibeenpwned.com/api/v3/pasteaccount/{account}'.format(account=i), headers=headerspwned)
     
        if response.status_code == 404:
                cprint("         - None", 'green')
        else:
            paste_count=0
            responsejson = json.dumps(response.json())
            hibpresponse = json.loads(responsejson)
            pasteinfo = hibpresponse
            for y in pasteinfo:
                cprint("         - Title: "+str(hibpresponse[paste_count]['Title']), 'green')
                cprint("                   Source: "+str(hibpresponse[paste_count]['Source']), 'green')
                cprint("                   Location: "+str(hibpresponse[paste_count]['Id']), 'green')
                paste_count=paste_count+1
        time.sleep(2)


