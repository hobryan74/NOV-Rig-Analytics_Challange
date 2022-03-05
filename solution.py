import json

customersData = open('dmv-appointment-scheduler\data-set\CustomerData.json')
tellerData = open('dmv-appointment-scheduler\data-set\TellerData.json')

customers = json.load(customersData)
tellers = json.load(tellerData)

customerD = customers
tellerD = tellers
'''
for x in customers['Customer']:
    print(x['type'])


for x in tellers['Teller']:
    print(x['SpecialtyType'])'''

#tellerD['Teller'][0]['time'] = 20
#print(tellerD['Teller'][0]['time'])

customersData.close()
tellerData.close()