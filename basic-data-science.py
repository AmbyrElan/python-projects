def economicData():

    file = 'Economic_Data_2010.txt'

    region = input("Enter region : ")
    gdp = {}
    pop = {}
    pi = {}
    tPop = 0
    tPI = 0
    tGDP = 0
    states = []
    
    with open(file,'r') as f:
        line = f.readline()
        
        while(line!=''):
            line = line.split(',')
            
            if(line[1].lower()==region.lower()):
                state = line[0]
                states.append(state)
                pop[state] = line[2]
                tPop += float(line[2])
                gdp[state] = line[3]
                tGDP += float(line[3])
                pi[state] = line[4]
                tPI += float(line[4])
                
            line = f.readline()
            
    print("Economics statistics for the ",region," region")
    print("States in region :",', '.join(states))
    print("Total population : ",str(round(tPop,4)), " million")
    print("Average population : ",str(round(tPop/len(states),4))," million")
    print("Total GDP : ",str(round(tGDP,4))," billion")
    print("Average PI : ",str(round(tPI/len(states),4))," billion")

economicData()
