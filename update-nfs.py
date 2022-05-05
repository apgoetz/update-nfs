#! /usr/bin/env python3
import requests
import sys
import os
from auth import NfsnAuth

import re
from time import strftime, localtime

try:
    user = os.environ['NFS_DNS_USER']
    key  = os.environ['NFS_DNS_APIKEY']
    domain  = os.environ['NFS_DNS_DOMAIN']
    subdomain  = os.environ['NFS_DNS_SUBDOMAIN']
except KeyError as e:
    print("missing critical env variable: {}".format(e.args[0]), file=sys.stderr)
    sys.exit(1)

apiurl = 'https://api.nearlyfreespeech.net'



currentip = re.findall(r"[0-9]+(?:\.[0-9]+){3}", requests.get('https://ipinfo.io/ip').text)[0]

s = requests.Session()
s.auth = NfsnAuth(user, key)

# get dns records of website
r = s.post(apiurl+'/dns/'+domain+'/listRRs', data = {'name' : subdomain})
if r.status_code != requests.codes.ok:
    print("ERROR: {} could not list dns entries!".format(r.status_code), file=sys.stderr)
    sys.exit(1)


try:
    listedip = r.json()[0]['data']
except IndexError:
    print("could not index dns entries!", file=sys.stderr)
    sys.exit(1)

    
logtime = strftime("%Y-%m-%d %H%M", localtime())
print ("current: {} listed: {}".format(currentip, listedip))
if currentip != listedip: # check to see if the ip has changed; if so:
    if listedip is not None:
        data = {'name' : subdomain, 'type' : 'A', 'data' : currentip}
        r = s.post(apiurl+'/dns/'+domain+'/replaceRR', data)
        if r.status_code != requests.codes.ok:
            print("could not update dns entries!", file=sys.stderr)
            sys.exit(1)
        print (logtime + " DNS record updated from " + listedip + " to " + currentip)
else:
    print (logtime + " No update required.")


