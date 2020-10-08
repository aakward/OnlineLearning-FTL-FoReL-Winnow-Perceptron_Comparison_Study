import matplotlib.pyplot as plt
import scipy.stats as ss
import math
import numpy as np
from random import randint


T=int(input("Enter the value of T : "))      #time horizon
npath=input("Enter the no. of sample paths : ")
    
def ftl():
    
    d=10       #the no. of experts
    eta=0           #learning rate
    loss1_param=[0.5,0.5,0.5,0.5,0.5,0.5,0.5,0.5,0.4,0.6]
    loss2_param=[0.5,0.5,0.5,0.5,0.5,0.5,0.5,0.5,0.4,0.3]
    Cum_Regret_over_paths=[]  
    cum_regret_t=[[0 for j in range(npath)]for i in range(T)]
    for path in range(npath):
        temp1=[]
        #print "s",path
        Cum_Regret=[0 for i in range(T)]
        loss=[]  
        lo=[]
        minl_tillt=[0 for i in range(d)]
        armnround=0
        for t in range(T):
            #print "t",t
            temp=[]
            for j in range(d):
                    
                    if(t<T/2):
                        l=np.random.binomial(1,loss1_param[j])
                        temp.append(l)
                    else:
                        l=np.random.binomial(1,loss2_param[j])
                        temp.append(l)
                      
            loss.append(temp)
            if(t==0):
                r=randint(0,d-1)
                lo.append(temp[r]) 
                Cum_Regret[t]=Cum_Regret[t]+loss[t][r]
                minlv_tillt=[temp[i] for i in range(d)]
                minl_tillt=min(minlv_tillt)
                armnround=minlv_tillt.index(minl_tillt)
                Cum_Regret[t]=Cum_Regret[t]-minl_tillt
                #print "r",r
                cum_regret_t[t][path]=Cum_Regret[t]
            else:
                lo.append(temp[armnround]+lo[-1]) 
                Cum_Regret[t]=Cum_Regret[t-1]+loss[t][armnround]
                #print "CR", Cum_Regret
                minlv_tillt=[minlv_tillt[i]+loss[t][i] for i in range(d)]
                minl_tillt=min(minlv_tillt)
                armnround=minlv_tillt.index(minl_tillt)
                Cum_Regret[t]=lo[-1]-minl_tillt
                temp1.append(Cum_Regret[t])
                cum_regret_t[t][path]=Cum_Regret[t]
#            print "Loss incurred",lo    
#            print "Arm chosen in round",t+1, "is:",armnround+1
#            
#            print "Losses",temp
#            
#            print "CL", minlv_tillt
#            print "CR", Cum_Regret
            
        Cum_Regret_over_paths.append(Cum_Regret)
    Avg_Cum_Regret=[0 for i in range(T)]
    for t in range(T):
        for path in range(npath):
            Avg_Cum_Regret[t]=Avg_Cum_Regret[t]+Cum_Regret_over_paths[path][t]
    for t in range(T):
        Avg_Cum_Regret[t]=Avg_Cum_Regret[t]/npath
    num=[i for i in range(T)]
    #print num
    ######################
    regret_mean = []
    regret_err = []
    time_epoch=[i for i in range(T)]
    freedom_degree = len(cum_regret_t[0]) - 2
    for regret in cum_regret_t:
        regret_mean.append(np.mean(regret))
        regret_err.append(ss.t.ppf(0.95, freedom_degree) *ss.sem(regret))
    colors = list("rgbcmyk")
    shape = ['--^', '--d', '--v']
    plt.errorbar(time_epoch, regret_mean, regret_err, color=colors[0])
    plt.plot(time_epoch, regret_mean, colors[0] + shape[0], label='Follow the Leader (FTL)')
########################################3
    
    
    
    plt.plot(Avg_Cum_Regret)
    plt.xlabel("T")
    plt.ylabel("Cumulative Regret")
    plt.title("Plot for pseudo Cumulative regret against T")

#def forel():
#    
#    d=10       #the no. of experts
#    eta=0           #learning rate
#    c=1
#    loss1_param=[0.5,0.5,0.5,0.5,0.5,0.5,0.5,0.5,0.4,0.6]
#    loss2_param=[0.5,0.5,0.5,0.5,0.5,0.5,0.5,0.5,0.4,0.3]
#    R_eta=[]
#    wm_regret=[]
#    cum_regret_t=[[0 for j in range(npath)]for i in range(T)]
#    if(c==1):
#    
#        eta=c*math.sqrt(2.0*math.log(d)/T)
#        b=[]
#        b.append(eta)
#        R=[]
#        for path in range(npath):
#            w=[]
#            w.append([1.0,1.0,1.0,1.0,1.0,1.0,1.0,1.0,1.0,1.0])
#            regret=0
#            minm=[0 for i in range(d)]
#            for t in range(T):
#                a=[]
#                loss=[]
#                expected_loss=0
#                for j in range(d):
#                    a.append(w[t][j]/sum(w[t]))
#                    if(t<T/2):
#                        l=np.random.binomial(1,loss1_param[j])
#                    else:
#                        l=np.random.binomial(1,loss2_param[j])
#                    loss.append(l)
#                    minm[j]=minm[j]+l
#                    expected_loss=expected_loss+(a[j]*loss[j])
#                a=[]
#                regret=regret+expected_loss
#                for j in range(d):
#                    a.append(w[t][j]*math.exp(-1*eta*loss[j]))
#                w.append(a)
#                if(t<T/2.0):
#                    regret=regret-(T*0.4)
#                else:
#                    regret=regret-min(0.4*(t+1),0.3*((T/2.0)+(t+1)))
#                cum_regret_t[t][path]=regret
##            R.append(regret)
##            b.append(regret)
##            wm_regret.append(b)
#        #R_eta.append(sum(R)/20)
#   # print R_eta
#    eta = []
#    regret_mean = []
#    regret_err = []
#    freedom_degree = len(cum_regret_t) - 2
#    time_epoch=[i for i in range(T)]
#    for regret in wm_regret:
#        regret_mean.append(np.mean(regret))
#        regret_err.append(ss.t.ppf(0.95, freedom_degree) * ss.sem(regret))
#    
#    colors = list("rgbcmyk")
#    shape = ['--^', '--d', '--v']
#    plt.errorbar(time_epoch, regret_mean, regret_err, color=colors[1])
#    plt.plot(time_epoch, regret_mean, colors[1] + shape[1], label='FoReL')
#    plt.legend()
#    
#
##    plt.title("Pseudo Regret vs Learning Rate for T = 10^5 and 20 Sample paths")
##    plt.xlabel("Learning Rate")
##    plt.ylabel("Pseudo Regret")
##    plt.close()




ftl()
#forel()
                