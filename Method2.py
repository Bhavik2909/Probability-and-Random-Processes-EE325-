from cmath import log
from re import U
import numpy as np
import matplotlib.pyplot as plt
import random
import math

p = [0.2, 0.4 , 0.7]
alpha_values = [0.1 , 0.05 , 0.01 ]
no_of_trials = 500

def toss(p):
    if p>=random.random():
        return 1
    else:
        return 0

def calc_ucb(n, k, alpha):
    x = 2*math.log(10)-math.log(alpha*100)
    return k/n + pow((x/(2*n)),0.5)

def simulation(N, alpha):
    n = [0,0,0]
    k = [0,0,0]
    ucb = [1.0,1.0,1.0]
    ka = [0 for x in range(5000)]
    kb = [0 for x in range(5000)]
    kc = [0 for x in range(5000)]

    for i in range(N):
        u = max(ucb[0], ucb[1], ucb[2])
        x, z= 0, 0
        y = []
        for j in range(3):
            if ucb[j]==u:
                x = x+1
                y.append(j)
        z = y[random.randint(0,x-1)]
        
        n[z]=n[z]+1
        k[z]=k[z]+toss(p[z])
        ucb[z] = calc_ucb(n[z],k[z],alpha)
        ka[i] = k[0]/(i+1)
        kb[i] = k[1]/(i+1)
        kc[i] = k[2]/(i+1)
    
    results = {"n": n , "k": k, "ka": ka, "kb" :kb, "kc" :kc}
    return results


def table_data():
    for alpha in alpha_values:
        print(" For alpha = ", alpha)
        for N in [20, 100, 1000, 5000]:
            heads_net = 0
            expected_reward = p[2]*N
        #ka_net = [0 for x in range(5000)]
        #kb_net = [0 for x in range(5000)]
        #kc_net = [0 for x in range(5000)]
            for i in range(no_of_trials):
                results = simulation(N, alpha)
                heads_net = heads_net + results["k"][0]+ results["k"][1]+ results["k"][2]
            #if N==5000:
                #for j in range(5000):
                    #ka_net[j] = ka_net[j] + results["ka"][j]
                    #kb_net[j] = kb_net[j] + results["kb"][j]
                    #kc_net[j] = kc_net[j] + results["kc"][j]

            avg_reward = heads_net/no_of_trials
        #ka_avg = [ x /no_of_trials for x in ka_net]
        #kb_avg = [ x /no_of_trials for x in kb_net]
        #kc_avg = [ x /no_of_trials for x in kc_net]
                
        #x_axis = [x for x in range(5000)]
        #plt.plot(x_axis,ka_avg,label = "K(A)/K")
        #plt.plot(x_axis,kb_avg,label = "K(B)/K")
        #plt.plot(x_axis,kc_avg,label = "K(C)/K")
        #plt.xlabel("Toss Number")
        #plt.ylabel("Sample Average for alpha = " + str(alpha))
        #plt.title("P(A) = 0.2, P(B) = 0.4, P(C) = 0.7")
        #plt.legend()
        #plt.show()

            print("  N = ",N, " -> Sample avg of Total Reward = ",avg_reward , ", Expected Reward = ", expected_reward)

print("For P(A,B,C) = ", p)
table_data()
p = [0.45,  0.5 , 0.58]
print("For P(A,B,C) = ", p)
table_data()