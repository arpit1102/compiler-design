#follow of a grammar
def fir(f):
    p=f.read().split("\n")
    first={}
    for i in p:
        print(i)
        first[i[0]]=[]
    for i in p:
        t=i[3:]
        x=t.split("|")
        for j in x:
            if j[0].islower():
                first[i[0]].append(j[0])
    
    for i in p:
        t=i[3:]
        x=t.split("|")
        for j in x:
            k=0
            if j[k].isupper():
                l=first[j[k]]
                if 'e' not in l:
                    first[i[0]]+=(l)
                    for t in p:
                        if t[0]==j[k]:
                            if t[3].isupper():
                                first[i[0]]+=first[t[3]]
  
                            
                            
                        
            k=0   
            while j[k].isupper() and 'e' in first[j[k]]:
                try:
                    k+=1
                    if j[k].islower():
                        first[i[0]].append(j[k])
                    else:
                        first[i[0]]+=(first[j[k]])
                except IndexError:
                    break
                
                
    return(first)
def follow(f,fi):
    
    p=f.read().split("\n")
    follow={}
    
    for i in p:
        #print(i)
        follow[i[0]]=[]
    follow[p[0][0]]+=['$']
    for s in p:
        m=s[3:]
        x=m.split("|")
        for i in x:
            for j in range(len(i)-1):
                if i[j].isupper() and i[j+1].islower():
                    follow[i[j]]+=i[j+1]
                elif i[j].isupper() and i[j+1].isupper():
                    t=[k for k in fi[i[j+1]] if k!='e']
                    follow[i[j]]+=t
    for s in p:
        m=s[3:]
        x=m.split("|")
        for i in x:     
            for k in range(len(i)):
                if i[k].isupper():
                    if (k!=len(i)-1 and i[k+1].isupper() and 'e' in fi[i[k+1]]) or (k==(len(i)-1) and not i[k].islower()):
                        follow[i[k]]+=follow[s[0]]

    for i in follow:
        follow[i]=(list(set(follow[i])))
                    
    print(follow)
   

f=open("C:/Users/Arpit/Desktop/grammar.txt","r")
fi=fir(f)
f.close()
f=open("C:/Users/Arpit/Desktop/grammar.txt","r")
follow(f,fi)
