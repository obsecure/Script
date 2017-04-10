#!/usr/bin/env python

import json
import urllib2
from urllib2 import HTTPError, URLError
import requests
import urllib3
urllib3.disable_warnings()

def alarm(bot_id, chat_id, text, https_proxy):
    proxies = {'https':https_proxy}
    payload = {
        'chat_id' : chat_id,
        'text' : text
    }
    headers = {'content-type':'application/json'}
    url = 'https://api.telegram.org/bot%s/sendMessage' % (bot_id)

    response = requests.post(url, data = json.dumps(payload), headers = headers, proxies = proxies)


url = 'http://namenode-host:50070/jmx?qry=Hadoop:service=NameNode,name=NameNodeStatus'

msg = "Name Node Failed Over!!!"
bot_id = "XXXXXXXXXXX"
chat_id = -XXXXXXXXXX
proxy = "https://proxy_host:8080"

try:

    response = urllib2.urlopen(url)

except HTTPError as e:
    #print "The server couldn\'t fulfill the request."
    #print "Error code: %s" % (e.code)
    msg = 'Error code: %s' % (e.code)
    alarm(bot_id, chat_id, msg, proxy)

except URLError as e:
    #print "We failed to reach a server"
    #print "Reason: %s" % (e.reason)
    msg = 'Reason: %s' % (e.reason)
    alarm(bot_id, chat_id, msg, proxy)

else:

    data = json.load(response)

    hastatus = data['beans'][0]['State']

    if hastatus == "active" :
        hastatus = "A"
    elif hastatus == "standby" :
        hastatus ="S"


    # touch state_file if it does not exits

    file = open("/media/RamDisk/nn_status.txt", "a").close()
    file = open("/media/RamDisk/nn_status.txt", "r")

    prev_state = file.read()
    file.close()

    next_state=""

    if len(prev_state) < 3 :
        next_state = prev_state + hastatus
    else :
        next_state = prev_state[1:] + hastatus

    file = open("/media/RamDisk/nn_status.txt", "w")

    file.write(next_state)

    file.close()

    #print "Cluster status: %s" % (hastatus)
    #print "Cluster previous status: %s" % (prev_state)
    #print "Cluster next status: %s" % (next_state)

    if next_state[-3:] == "AAS":
        print msg
        alarm(bot_id, chat_id, msg, proxy)

    if next_state[-3:] == "SSA":
        print msg
        alarm(bot_id, chat_id, msg, proxy)
