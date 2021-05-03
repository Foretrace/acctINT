``` 
 ________  ________  ________ _________     ___  ________   _________
|\   __  \|\   ____\|\   ____\\___   ___\  \ \  \|\   ___  \|\___   ___\ 
\ \  \|\  \ \  \___|\ \  \___\|___ \  \_    \ \  \ \  \\ \  \|___ \  \_| 
 \ \   __  \ \  \    \ \  \       \ \  \     \ \  \ \  \\ \  \   \ \  \  
  \ \  \ \  \ \  \____\ \  \____   \ \  \     \ \  \ \  \\ \  \   \ \  \ 
   \ \__\ \__\ \_______\ \_______\  \ \__\ .   \ \__\ \__\  \__\   \ \__\
```                                                                   


# acctINT
acctINT is designed to footprint the public email accounts associated with a domain. This will help users identify publicly exposed accounts, places the accounts appears online, known breaches where passwords may be located, and paste sites (pastebin, pastie, etc.) which contain mentions of the accounts in a paste entry.


To run this script yourself:
1. Aquire necessary API keys (hunter.io [[free tier]](https://hunter.io/pricing) and haveibeenpwned.com [[$3.50/mo]](https://haveibeenpwned.com/API/Key))
2. Install pyton3 and pip3
3. Clone the repository: ```git clone https://github.com/Foretrace/acctint```
4. Install requirements: ```pip3 install -r requirements.txt```
5. Run a test ```run python3 acctINT.py -d example.com --pwnedapi <hibp api key> --huntapi <huner.io api key>```



# How it works
1. Requests accounts associated with a domain from the hunter.io Domain Search API
2. Iterates through each account and displays the accounts source urls provided by hunter, and requests latest breach and paste information over the haveibeenpwned api


# Args
```
usage: acctINT.py [-h] -d DOMAIN --pwnedapi PWNEDAPI --huntapi HUNTAPI

optional arguments:
  -h, --help            show this help message and exit
  -d DOMAIN, --domain DOMAIN
                        Specify the parent domain
  --pwnedapi PWNEDAPI   API key for HIBP
  --huntapi HUNTAPI     API key for hunter.io
```

# Example

Execution:
```
python3 acctINT.py -d bar.com --pwnedapi <haveibeenpwned api key> --huntapi <hunter.io api key>
```
(truncated) Output:
```
 ________  ________  ________ _________     ___  ________   _________
|\   __  \|\   ____\|\   ____\\___   ___\  \ \  \|\   ___  \|\___   ___\ 
\ \  \|\  \ \  \___|\ \  \___\|___ \  \_    \ \  \ \  \\ \  \|___ \  \_| 
 \ \   __  \ \  \    \ \  \       \ \  \     \ \  \ \  \\ \  \   \ \  \  
  \ \  \ \  \ \  \____\ \  \____   \ \  \     \ \  \ \  \\ \  \   \ \  \ 
   \ \__\ \__\ \_______\ \_______\  \ \__\ .   \ \__\ \__\  \__\   \ \__\
                                                                     
----------------------------------------------------------------------------------------------------
Finding accounts associated with bar.com
----------------------------------------------------------------------------------------------------

[220] total accounts found:
    - leigh@bar.com
    - john@bar.com
    - fred@bar.com
    - david@bar.com
    - joe@bar.com
    - john.doe@bar.com
    - mike@bar.com
    - bruno@bar.com
    [...]

----------------------------------------------------------------------------------------------------
Starting footprint for bar.com accounts
----------------------------------------------------------------------------------------------------
joe@bar.com footprint:
     Sources:
         - http://freron.lighthouseapp.com/projects/58672-mailmate/tickets
                   initially seen on: 2021-02-15
                   last seen on: 2021-02-15
         - http://nixref.markweastwood.co.uk/site/display/articles_for/mail/topic_is/sendmail
                   initially seen on: 2020-07-18
                   last seen on: 2020-07-18
         - http://unixsystem.net.ua/print:page,1,193-dopolnitelnye-primitivy-konfiguracii-programmy.html
                   initially seen on: 2019-02-26
                   last seen on: 2019-08-26
     Breaches:
         - Collection1
                   Breach Date: 2019-01-07
                   Data Compromised: ['Email addresses', 'Passwords']
         - PDL
                   Breach Date: 2019-10-16
                   Data Compromised: ['Email addresses', 'Employers', 'Geographic locations', 'Job titles', 'Names', 'Phone numbers', 'Social media profiles']
         - MyHeritage
                   Breach Date: 2017-10-26
                   Data Compromised: ['Email addresses', 'Passwords']
         - Nihonomaru
                   Breach Date: 2015-12-01
                   Data Compromised: ['Email addresses', 'IP addresses', 'Passwords', 'Usernames']
     Pastes:
         - Title: email and password hacked by anonymous sadek
                   Source: Pastebin
                   Location: 1pbNnkVB
         - Title: None
                   Source: Pastebin
                   Location: BVY9QMLw
john@bar.com footprint:
     Sources:
         - http://openldap.org/lists/openldap-software/200403/msg00920.html
                   initially seen on: 2015-05-06
                   last seen on: 2021-01-30
         - http://anandprakash.net
                   initially seen on: 2017-07-06
                   last seen on: 2020-04-04
         - http://anandprakash.net/2016/11
                   initially seen on: 2017-07-06
                   last seen on: 2020-04-04
         - http://anandprakash.net/2016/11/15/how-to-build-a-business-kiss-keep-it-simple-and-sweet
                   initially seen on: 2017-07-06
                   last seen on: 2020-04-04
         - http://gist.github.com/tdrozdowski/056744d6ecf6707b29c3
                   initially seen on: 2015-04-27
                   last seen on: 2018-03-20
     Breaches:
         - PDL
                   Breach Date: 2019-10-16
                   Data Compromised: ['Email addresses', 'Employers', 'Geographic locations', 'Job titles', 'Names', 'Phone numbers', 'Social media profiles']
         - RiverCityMedia
                   Breach Date: 2017-01-01
                   Data Compromised: ['Email addresses', 'IP addresses', 'Names', 'Physical addresses']
         - VerificationsIO
                   Breach Date: 2019-02-25
                   Data Compromised: ['Dates of birth', 'Email addresses', 'Employers', 'Genders', 'Geographic locations', 'IP addresses', 'Job titles', 'Names', 'Phone numbers', 'Physical addresses']
     Pastes:
         - None
david@bar.com footprint:
     Sources:
         - http://patentsencyclopedia.com/app/20090030919
                   initially seen on: 2019-02-15
                   last seen on: 2021-02-15
         - http://google.com/patents/us20090030919
                   initially seen on: 2016-03-25
                   last seen on: 2018-07-18
         - http://faqs.org/patents/app/20110087969
                   initially seen on: 2015-02-02
                   last seen on: 2019-02-26
     Breaches:
         - None
     Pastes:
         - None
```

