import matplotlib.pyplot as plt
import math
import csv
f=open('news.csv','r')
reader=csv.reader(f)
data=[]
label=[]

for r in reader:
    temp=[]    
    for i in range(len(r)-1):
        temp.append(float(r[i]))
    data.append(temp)
    label.append(int(r[-1]))
    
d=len(data[0])

def norm(x):
    n=0.0
    for i in range(len(x)):
        n=n+x[i]**2
    return math.sqrt(n)
        

def perceptron():
    t1=0
    w=[0 for i in range(len(data[0]))]
    w_t=[]
    dist=[] 
    w_t.append(w)
    
    for t in range(len(data)):
        x_t=data[t]
        s=0
        for i in range(len(w)):
            s=s+(x_t[i]*w[i])
        if(s>=0):
            p_t=1
        else:
            p_t=-1
        #print p_t,label[t]
        if(p_t!=label[t]):
            z=w[:]
            w=[]
            for i in range(len(x_t)):
                w.append(z[i]+(label[t]*x_t[i]))          
                
            w_t.append(w)    
        else :
            w_t.append(w)
        
        
#        if(t>50800):
#            print "w",w
        #w_t.append(w)
        #print w
        
        d1=w_t[t+1][:]
        d2=w_t[t][:]
#        print "d1",d1
#        print "d2",d2
        norm_d1=norm(d1)
        norm_d2=norm(d2)
        if(norm_d1==0 or norm_d2==0):
            dist=[]
            t1=t
        else:
            distance=[0 for i in range(len(w))]
            for i in range(len(w)):
                
                d1[i]=float(d1[i])/norm_d1
                d2[i]=float(d2[i])/norm_d2    
                distance[i]=d1[i]-d2[i]
            z=norm(distance)
                #print z
            dist.append(z)
    
    
    num=[i for i in range(t1+1,len(data))]
    plt.scatter(num,dist,label='perceptron')
    plt.legend()
    plt.xlabel("Time Epochs")
    plt.ylabel("Distances between consecutive w")
    plt.title("Plot of Distances of consecutive w against Time Epochs")
    
        
def winnow():
    eta=0.25
    w=[1.0/d for i in range(len(data[0]))]
    t1=0
    w_t=[]
    dist=[] 
    w_t.append(w)
    for t in range(len(data)):
        x_t=data[t]
        s=0
        for i in range(len(w)):
            s=s+(x_t[i]*w[i])
        if(s>=0):
            p_t=1
        else:
            p_t=-1
        #print p_t,label[t]
        if(p_t!=label[t]):
            z=w[:]
            w=[]
            ss=0.0
            for i in range(len(z)):
                ss=ss+(z[i]*math.exp(eta*label[t]*data[t][i]))
                
    
            for i in range(len(x_t)):
                w.append(z[i]*math.exp(eta*label[t]*data[t][i])/ss)
            w_t.append(w)   
        else : 
            w_t.append(w)
#        if(t>50800):
#            print "w",w
        #w_t.append(w)
        
        
        d1=w_t[t+1][:]
        d2=w_t[t][:]
        norm_d1=norm(d1)
        norm_d2=norm(d2)
        if(norm_d1==0 or norm_d2==0):
            dist=[]
            t1=t
        else:
            distance=[0 for i in range(len(w))]
            for i in range(len(w)):
                
                d1[i]=float(d1[i])/norm_d1
                d2[i]=float(d2[i])/norm_d2    
                distance[i]=d1[i]-d2[i]
            z=norm(distance)
                #print z
            dist.append(z)
    

    num=[i for i in range(t1,len(data))]
    plt.scatter(num,dist,color='r',label='winnow')
    plt.legend()
    plt.xlabel("Time Epochs")
    plt.ylabel("Distances between consecutive w")
    plt.title("Plot of Distances of consecutive w against Time Epochs")
        



perceptron()
winnow()
        
        