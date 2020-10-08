import matplotlib.pyplot as plt
import scipy.stats as ss
import math
import numpy as np
def main():
    T=int(input("Enter the value of T: "))      #time horizon
    d=10       #the no. of experts
    eta=0           #learning rate
    c=0.1
    loss1_param=[0.5,0.5,0.5,0.5,0.5,0.5,0.5,0.5,0.4,0.6]
    loss2_param=[0.5,0.5,0.5,0.5,0.5,0.5,0.5,0.5,0.4,0.3]
    R_eta=[]
    wm_regret=[]
    while(c<=2.1):
        c=c+0.2
        eta=c*math.sqrt(2.0*math.log(d)/T)
        b=[]
        b.append(eta)
        R=[]
        for i in range(20):
            w=[]
            w.append([1.0,1.0,1.0,1.0,1.0,1.0,1.0,1.0,1.0,1.0])
            regret=0
            minm=[0 for i in range(d)]
            for t in range(T):
                a=[]
                loss=[]
                expected_loss=0
                for j in range(d):
                    a.append(w[t][j]/sum(w[t]))
                    if(t<T/2):
                        l=np.random.binomial(1,loss1_param[j])
                    else:
                        l=np.random.binomial(1,loss2_param[j])
                    loss.append(l)
                    minm[j]=minm[j]+l
                    expected_loss=expected_loss+(a[j]*loss[j])
                a=[]
                regret=regret+expected_loss
                for j in range(d):
                    a.append(w[t][j]*math.exp(-1*eta*loss[j]))
                w.append(a)
            regret=regret-(T*0.4)
            R.append(regret) 
            b.append(regret)
            wm_regret.append(b)
        print "for c= ",c-0.2,", the regret is: ",sum(R)/20
        R_eta.append(sum(R)/20)
    print R_eta
    eta = []
    regret_mean = []
    regret_err = []
    freedom_degree = len(wm_regret[0]) - 2
    for regret in wm_regret:
        eta.append(regret[0])
        regret_mean.append(np.mean(regret[1:]))
        regret_err.append(ss.t.ppf(0.95, freedom_degree) * ss.sem(regret[1:]))

    colors = list("rgbcmyk")
    shape = ['--^', '--d', '--v']
    plt.errorbar(eta, regret_mean, regret_err, color=colors[0])
    plt.plot(eta, regret_mean, colors[0] + shape[0], label='FoReL')
    
    plt.legend(loc='upper right', numpoints=1)
    plt.title("Pseudo Regret of FoReL for T = 10^5 and 20 Sample paths")
    plt.xlabel("Learning Rate")
    plt.ylabel("Pseudo Regret")
    plt.close()

main()
                
                
                
                    
                
            
            
            