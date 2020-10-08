import random
import numpy as np
import matplotlib.pyplot as plt

np.random.seed(4995)

data1=[]
label1=[]
data2=[]
label2=[]

for i in range(1000):
    temp=[]    
    for j in range(2):
        r=np.random.normal(loc=-2,scale=math.sqrt(0.5))
        temp.append(r)
    temp.append(-1)
    data1.append(temp)
    

for i in range(1000):
    temp=[]    
    for j in range(2):
        r=np.random.normal(loc=-10,scale=math.sqrt(0.25))
        temp.append(r)
    temp.append(1)
    data2.append(temp)
    

data=data1+data2

w_star=[]

np.random.shuffle(data)

label=[]
for i in range(len(data)):
    label.append(data[i][2])
    
def norm(x):
    n=0.0
    for i in range(len(x)):
        n=n+x[i]**2
    return math.sqrt(n)


def perceptron():
    R_max=-1
    t1=0
    w=[0,0]
    w_t=[]
    dist=[] 
    w_t.append(w)
    b_t=[]
    b_t.append(0)
    mistakes=0
    for t in range(len(data)):
            x_t=[]
            for i in range(len(data[0])-1):
                x_t.append(data[t][i])
            if max(x_t)>R_max:
                R_max=max(x_t)
            s=0
            for i in range(len(w)-1):
                s=s+(data[t][i]*w[i])
            s=s+b_t[t]
            if(s>=0):
                p_t=1
            else:
                p_t=-1
            #print p_t,label[t]
            if(p_t!=label[t]):
                mistakes=mistakes+1
                z=w[:]
                w=[]
                for i in range(len(x_t)):
                    w.append(z[i]+(label[t]*x_t[i]))
                w_t.append(w)
                
                b_t.append(b_t[t]+data[t][2])
            else :
                w_t.append(w)
                b_t.append(b_t[t])
    #        if(t>50800):
    #            print "w",w
            #w_t.append(w)
            #print w
            w_star=w[:]
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
    b_star=b_t[-1]
    print "No. of mistakes for Perceptron is:",mistakes
    Mistake_Bound=0.0
    
    gamma=margin_estimate(w_star,b_star)
    Mistake_Bound=R_max**2*norm(w_star)/gamma**2
    print "Mistake Bound for perceptron is: ",Mistake_Bound

#    num=[i for i in range(t1+1,len(data))]
#    plt.scatter(num,dist,color='r',label='perceptron')
#    plt.legend()
#    plt.xlabel("Time Epochs")
#    plt.ylabel("Distances between consecutive w")
#    plt.title("Plot of Distances of consecutive w against Time Epochs")
    
def margin_estimate(w_star,b_star):
    #print "w*",w_star
    gamma=99999999999
    
    for t in range(len(data)):
        x_t=[]
        for i in range(len(data[0])-1):
            x_t.append(data[t][i])
        s=0
        for i in range(len(data[0])-1):
            s=s+(w_star[i]*x_t[i])
        
        s=(s+b_star)*data[t][2]
        if abs(s)<=gamma:
            gamma=abs(s) 
    print "Estimate of gamma is: ",gamma
    return gamma




def winnow():
    eta=0.25
    d=len(data[0])-1
    w=[1.0/d for i in range(len(data[0]))]
    t1=0
    w_t=[]
    dist=[] 
    w_t.append(w)
    b_t=[]
    b_t.append(0)
    eta_s=[0.05,0.1,0.15,0.20,0.25,0.30,0.35,0.40,0.45,0.50]
    for eta in eta_s:
        mistakes=0
        for t in range(len(data)):
            x_t=[]
            for i in range(len(data[0])-1):
                x_t.append(data[t][i])
            s=0
            for i in range(len(w)-1):
                s=s+(x_t[i]*w[i])
            if(s>=0):
                p_t=1
            else:
                p_t=-1
            #print p_t,label[t]
            if(p_t!=label[t]):
                mistakes=mistakes+1
                z=w[:]
                w=[]
                ss=0.0
                for i in range(len(z)):
                    ss=ss+(z[i]*math.exp(eta*label[t]*data[t][i]))
                    
        
                for i in range(len(x_t)):
                    w.append(z[i]*math.exp(eta*label[t]*data[t][i])/ss)
                w_t.append(w)   
                b_t.append(b_t[t]+data[t][2])
            else : 
                w_t.append(w)
                b_t.append(b_t[t])
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
        
        print "No. of Mistakes for Winnow is: ", mistakes,"when value of eta is: ",eta
#    num=[i for i in range(t1,len(data))]
#    plt.scatter(num,dist,color='r',label='winnow')
#    plt.legend()
#    plt.xlabel("Time Epochs")
#    plt.ylabel("Distances between consecutive w")
#    plt.title("Plot of Distances of consecutive w against Time Epochs")
#    
    

perceptron()
winnow()
