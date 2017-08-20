import numpy as np
import matplotlib.pyplot as plt
from time import time

from scipy.spatial import KDTree


def eucl (a,b):
    return np.sqrt(np.sum((a-b)**2))

def create_data(n_rows, n_cols, range=1):
    return (np.random.random((n_rows, n_cols))-0.5)*range

def dratio (a,b,ref):
    return eucl(a,b)/ref

def plot_lsh_performance_for_datasizes (row_list, col_list, k_neighbours, bin_width, projs):

    fig = plt.figure(figsize=(10,10))
    ax1 = fig.add_subplot(221)
    ax2 = fig.add_subplot(222)
    ax3 = fig.add_subplot(223)
    ax4 = fig.add_subplot(224)

    total,c = len(row_list)*len(col_list),1

    for col in col_list:
        bOR, bAND, tOR, tAND = [], [], [], []
        for row in row_list:
            
            if c%(total/10)==0:
                print "%d"%(c*100./total)+"%",
            c+=1

            brOR, brAND, trOR, trAND = [], [], [], []
            for i in range(10):
                d = create_data(row, col)
                q = create_data(1, col)[0]
                kt    = KDTree(d)
                ktr   = kt.query(q,k_neighbours)
                drref = np.max(ktr[0])
                lsh = DiscretizedLSH(d,projs,bin_width)
                ts = time(); lshrAND = lsh.search_AND(q,k_neighbours); teAND = time()-ts
                ts = time(); lshrOR = lsh.search_OR(q,k_neighbours); teOR = time()-ts
                brAND.append(np.mean([dratio(d[i],q,drref) for i in lshrAND]))
                brOR.append(np.mean([dratio(d[i],q,drref) for i in lshrOR]))
                trAND.append(teAND)
                trOR.append(teOR)
            bOR.append(np.mean(brOR))
            bAND.append(np.mean(brAND))
            tOR.append(np.mean(trOR))
            tAND.append(np.mean(trAND))
            
        ax1.plot(row_list, bOR, label="cols "+str(col))
        ax2.plot(row_list, bAND, label="cols "+str(col))
        ax3.plot(row_list, tOR, label="cols "+str(col))
        ax4.plot(row_list, tAND, label="cols "+str(col))
    ax1.set_xlabel("rows")
    ax1.set_ylabel("distance ratio")
    ax1.set_title("lsh OR bin_w=%.3f, projs=%d, k=%d"%(bin_width, projs, k_neighbours))
    ax1.legend()

    ax2.set_xlabel("rows")
    ax2.set_ylabel("distance ratio")
    ax2.set_title("lsh AND bin_w=%.3f, projs=%d, k=%d"%(bin_width, projs, k_neighbours))
    ax2.legend()
    
    ax3.set_xlabel("rows")
    ax3.set_ylabel("query time")
    ax3.set_title("lsh OR bin_w=%.3f, projs=%d, k=%d"%(bin_width, projs, k_neighbours))
    ax3.legend()

    ax4.set_xlabel("rows")
    ax4.set_ylabel("query time")
    ax4.set_title("lsh AND bin_w=%.3f, projs=%d, k=%d"%(bin_width, projs, k_neighbours))
    ax4.legend()


def plot_lsh_performance_for_bins_projs(n_samples, len_x, k_neighbours, bins_list, projs_list):

    d = create_data(n_samples, len_x)
    q = create_data(1, len_x)[0]

    fig = plt.figure(figsize=(10,10))
    ax1 = fig.add_subplot(221)
    ax2 = fig.add_subplot(222)
    ax3 = fig.add_subplot(223)
    ax4 = fig.add_subplot(224)

    total,c = len(bins_list)*len(projs_list),1
    for p in projs_list:
        bOR, bAND, tOR, tAND = [], [], [], []
        for b in bins_list:
            if c%(total/10)==0:
                print "%d"%(c*100./total)+"%",
            c+=1

            brOR, brAND, trOR, trAND = [], [], [], []
            for i in range(10):
                q = (np.random.random(size=(len_x))-0.5)*.7
                kt    = KDTree(d)
                ktr   = kt.query(q,k_neighbours)
                drref = np.max(ktr[0])
                lsh = DiscretizedLSH(d,p,b)
                ts = time(); lshrAND = lsh.search_AND(q,k_neighbours); teAND = time()-ts
                ts = time(); lshrOR = lsh.search_OR(q,k_neighbours); teOR = time()-ts
                brAND.append(np.mean([dratio(d[i],q,drref) for i in lshrAND]))
                brOR.append(np.mean([dratio(d[i],q,drref) for i in lshrOR]))
                trAND.append(teAND)
                trOR.append(teOR)
            bOR.append(np.mean(brOR))
            bAND.append(np.mean(brAND))
            tOR.append(np.mean(trOR))
            tAND.append(np.mean(trAND))
            
        ax1.plot(bins_list, bOR, label="np "+str(p))
        ax2.plot(bins_list, bAND, label="np "+str(p))
        ax3.plot(bins_list, tOR, label="np "+str(p))
        ax4.plot(bins_list, tAND, label="np "+str(p))
    ax1.set_xlabel("bin width")
    ax1.set_ylabel("distance ratio")
    ax1.set_title("lsh OR (%d,%d) k=%d"%(n_samples, len_x, k_neighbours))
    ax1.legend()

    ax2.set_xlabel("bin width")
    ax2.set_ylabel("distance ratio")
    ax2.set_title("lsh AND (%d,%d) k=%d"%(n_samples, len_x, k_neighbours))
    ax2.legend()
    
    ax3.set_xlabel("bin width")
    ax3.set_ylabel("query time")
    ax3.set_title("lsh OR (%d,%d) k=%d"%(n_samples, len_x, k_neighbours))
    ax3.legend()

    ax4.set_xlabel("bin width")
    ax4.set_ylabel("query time")
    ax4.set_title("lsh AND (%d,%d) k=%d"%(n_samples, len_x, k_neighbours))
    ax4.legend()

class DiscretizedLSH:
    def __init__ (self, data=None, nb_projections=None, bw=None):
        self.nb_projections = nb_projections
        self.bin_width      = bw
        if (data is not None and nb_projections is not None and bw is not None):
            self.build_buckets(data)
            
    def build_buckets (self, data):
        assert self.nb_projections != None and self.bin_width!=None
        self.projections = np.random.random(size=(self.nb_projections,data.shape[1]))-0.5
        self.data        = data
        self.buckets = build_buckets(self.projections, data, self.bin_width)

    def get_signature(self, point):
        return get_signature (self.projections, point, self.bin_width)
        
    def get_bin(self, p, d):
        return get_bin(p,d,self.bin_width)
                        
    
    def search_OR(self, q, k=None):
        return search_OR(q, self.data, self.buckets, self.projections, self.bin_width, k)

    def search_AND(self, q, k=None):
        return search_AND(q, self.data, self.buckets, self.projections, self.bin_width, k) 



def eucl (a,b):
    return np.sqrt(np.sum((a-b)**2))

def show_2D_discretized_lsh(discretized_lsh, q, k=5):
    d = discretized_lsh.data

    discretized_lsh.build_buckets(d)
    allOR   = discretized_lsh.search_OR(q)
    allAND  = discretized_lsh.search_AND(q)
    fig=plt.figure(figsize=(10,10))
    plt.scatter(d[:,0],d[:,1], s=2, marker=".", color="black", alpha=0.5)  

    if len(allOR)>0:
         plt.scatter(d[allOR,0], d[allOR,1], s=20, marker="o", color="yellow", alpha=.5)

    if len(allAND)>0:
        plt.scatter(d[allAND,0], d[allAND,1], s=20, marker="o", color="blue", alpha=.5)

    ts = time(); bestOR   = discretized_lsh.search_OR(q,k);  tOR  = time()-ts
    ts = time(); bestAND  = discretized_lsh.search_AND(q,k); tAND = time()-ts

    
    plt.scatter(d[bestOR,0], d[bestOR,1], s=20, marker="o", color="red", alpha=.8)

    plt.scatter(q[0],q[1], s=300, marker="+", color="green", alpha=1.) 
    plt.scatter(q[0],q[1], s=300, marker="o", color="green", alpha=.3) 
    plt.title("buckets: OR (yellow), AND (blue), return by OR (red), query (green cross)")
 
    bestk = np.argsort([eucl(q,i) for i in d])[:k]

    maxk  = np.max([eucl(q,i) for i in d[bestk]])
    if len(bestAND)!=0:
        drAND = np.mean([eucl(q,i)/maxk for i in d[bestAND]]) 
    if len(bestOR)!=0:
        drOR  = np.mean([eucl(q,i)/maxk for i in d[bestOR]]) 
    drk   = np.mean([eucl(q,i)/maxk for i in d[bestk]]) 
    print "searched for", k, "neighbors"
    print "best OR    ",  np.sort(bestOR)
    print "best AND   ", np.sort(bestAND)
    print "best       ", np.sort(bestk)
    print "--"
    if len(bestOR)!=0:
        print "mean distance ratio best OR     %.3f"%drOR 
    if len(bestAND)!=0:
        print "mean distance ratio best AND    %.3f"%drAND
    print "mean distance ratio best        %.3f"%drk
    print "---"
    print "time OR     %.5f"%tOR
    print "time AND    %.5f"%tAND
    print ""
 
