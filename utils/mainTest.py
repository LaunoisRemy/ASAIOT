
with open('user.csv','r') as file :
        lignes=file.read().splitlines()
        dataColum=lignes[0].split(',')
        
        lignes.remove(lignes[0])
        for l in lignes :
                dataLigne=l.split(',')
                i=0
                personnes={}
                for c in dataColum:
                       personnes[c] = dataLigne[i]
                       i+=1
                print(personnes)
file.closed
                
                
        
        


