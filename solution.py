import json

if __name__ == '__main__':
    customersData = open('dmv-appointment-scheduler\data-set\CustomerData.json')
    tellerData = open('dmv-appointment-scheduler\data-set\TellerData.json')

    customers = json.load(customersData)
    tellers = json.load(tellerData)

    customer1 = {}
    customer2 = {}
    customer3 = {}
    customer4 = {}

    count1 = 0
    count2 = 0
    count3 = 0
    count4 = 0
    
    #this section is to seperate each categories into seperate dictionaries (Lines)

    for x in customers['Customer']:

        if(x['type'] == '1'):
            customer1[count1] = x
            #print(customer1[count1])
            count1+=1

        elif(x['type'] == '2'):
            customer2[count2] = x
            #print(customer2[count2])
            count2+=1

        elif(x['type'] == '3'):
            customer3[count3] = x
            #print(customer3[count3])
            count3+=1

        elif(x['type'] == '4'):
            customer4[count4] = x
            #print(customer4[count4])
            count4+=1

        else:
            print("issue")

    teller1 = {}
    teller2 = {}
    teller3 = {}
    teller4 = {}

    count1 = 0
    count2 = 0
    count3 = 0
    count4 = 0

    for x in tellers['Teller']:

        if(x['SpecialtyType'] == '1'):
            teller1[count1] = x
            teller1[count1]['Time'] = 0
            #print(teller1[count1])
            count1+=1

        elif(x['SpecialtyType'] == '2'):
            teller2[count2] = x
            teller2[count2]['Time'] = 0
            #print(teller2[count2])
            count2+=1

        elif(x['SpecialtyType'] == '3'):
            teller3[count3] = x
            teller3[count3]['Time'] = 0
            #print(teller3[count3])
            count3+=1

        elif(x['SpecialtyType'] == '0'):
            teller4[count4] = x
            teller4[count4]['Time'] = 0
            #print(teller4[count4])
            count4+=1

        else:
            print("issue")

    line = 0
    count1 = 0
    count2 = 0
    count3 = 0
    count4 = 0

    #algorithm to assign customers to tellers

    while(line < len(customers['Customer'])):
        
        for a in teller1:
            if(line >= len(customers['Customer'])):
                break

            if(count1 < len(customer1)):
                time = int(customer1[count1]['duration']) * float(teller1[a]['Multiplier'])
                teller1[a]['Time'] += time
                count1+=1
                line+=1

            elif(count4 < len(customer4)):
                time = int(customer4[count4]['duration'])
                teller1[a]['Time'] += time
                count4+=1
                line+=1

            elif(count3 < len(customer3)):
                time = int(customer3[count3]['duration'])
                teller1[a]['Time'] += time
                count3+=1
                line+=1
            
            elif(count2 < len(customer2)):
                time = int(customer2[count2]['duration'])
                teller1[a]['Time'] += time
                count2+=1
                line+=1


            else:
                print(line , "teller1 issue")
            
        
        for b in teller2:
            if(line >= len(customers['Customer'])):
                break

            if(count2 < len(customer2)):
                time = int(customer2[count2]['duration']) * float(teller2[b]['Multiplier'])
                teller2[b]['Time'] += time
                count2+=1
                line+=1

            elif(count4 < len(customer4)):
                time = int(customer4[count4]['duration'])
                teller2[b]['Time'] += time
                count4+=1
                line+=1

            elif(count3 < len(customer3)):
                time = int(customer3[count3]['duration'])
                teller2[b]['Time'] += time
                count3+=1
                line+=1

            elif(count1 < len(customer1)):
                time = int(customer1[count1]['duration'])
                teller2[b]['Time'] += time
                count1+=1
                line+=1


            else:
                print(line , "teller2 issue")


        for c in teller3:
            if(line >= len(customers['Customer'])):
                break

            if(count3 < len(customer3)):
                time = int(customer3[count3]['duration']) * float(teller3[c]['Multiplier'])
                teller3[c]['Time'] += time
                count3+=1
                line+=1

            elif(count4 < len(customer4)):
                time = int(customer4[count4]['duration'])
                teller3[c]['Time'] += time
                count4+=1
                line+=1

            elif(count2 < len(customer2)):
                time = int(customer2[count2]['duration'])
                teller3[c]['Time'] += time
                count2+=1
                line+=1

            elif(count1 < len(customer1)):
                time = int(customer1[count1]['duration'])
                teller3[c]['Time'] += time
                count1+=1
                line+=1


            else:
                print(line , "teller3 issue")


        for d in teller4:
            if(line >= len(customers['Customer'])):
                break
            if(count4 < len(customer4)):
                time = int(customer4[count4]['duration']) * float(teller4[d]['Multiplier'])
                teller4[d]['Time'] += time
                count4+=1
                line+=1

            elif(count1 < len(customer1)):
                time = int(customer1[count1]['duration'])
                teller4[d]['Time'] += time
                count1+=1
                line+=1

            elif(count2 < len(customer2)):
                time = int(customer2[count2]['duration'])
                teller4[d]['Time'] += time
                count2+=1
                line+=1

            elif(count3 < len(customer3)):
                time = int(customer3[count3]['duration'])
                teller4[d]['Time'] += time
                count3+=1
                line+=1
            

            else:
                print(line , "teller4 issue")


    #displays the answers and total times for each teller

    tellernum=1
    for x in teller1:
        print("Teller", tellernum,": Total Time: ", teller1[x]["Time"])
        tellernum+=1
    for x in teller2:
        print("Teller", tellernum,": Total Time: ",teller2[x]["Time"])
        tellernum+=1
    for x in teller3:
        print("Teller", tellernum,": Total Time: ",teller3[x]["Time"])
        tellernum+=1
    for x in teller4:
        print("Teller", tellernum,": Total Time: ",teller4[x]["Time"])
        tellernum+=1



    customersData.close()
    tellerData.close()