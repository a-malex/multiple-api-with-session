#!/usr/bin/python

import requests
from csv import reader

def nidFormat (nid):
    nlen = len(nid)
    if (nlen != 10) :
        diflen = 10 - nlen
        nid = str(nid)
        nid = nid.zfill(10)
    return str(nid)

outFile = open('OUTPUT.txt', 'w')
with open('INPUT_CSV', 'r') as read_obj:
    csv_reader = reader(read_obj)
    for row in csv_reader:
        nid = nidFormat(row[0])
        bdate = str(row[1])
        print("nid: {}, birthday: {}".format(nid,bdate))
        session = requests.Session()
        outFile.write('nationalId : {}' .format(nid))
        session.headers.update({'Authorization': 'Basic BASE64_KEY'})
        response1 = session.get('http://SERVER_ADDRESS/API1?NID={0}&BIRTHDATE={1}&CIVIL_TYPE=1'.format(nid, bdate))
        outFile.write('\n\nAP1 : ' + str(response1.json()))
        response2 = session.get('http://SERVER_ADDRESS/API2?NID={0}'.format(nid))
        outFile.write('\n\nAP2 : ' + str(response2.json()))
        response3 = session.get('http://SERVER_ADDRESS/API3?NID={0}'.format(nid))
        outFile.write('\n\nAP3 : ' + str(response3.json()))
        query = {'NID': nid}
        response4 = session.get('http://SERVER_ADDRESS/API4', params=query)
        outFile.write('\n\nAP4 : ' + str(response4.json()) + '\n\n\n')
        print('{} done!'.format(nid))
outFile.close

