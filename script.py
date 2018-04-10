import pandas as pd
import numpy as np
from SubCMediansLib.pySubCMedians import SubCMedians
from SubCMediansLib.EvaluationUtil.evaluationfunctions import accuracy,ce
import pickle
import random
import time
import sys
seed=1
np.random.seed(seed)

def generate_evaluation(clusters_found, clusters_hidden):
	accuracy_local = accuracy(cluster_hidden=clusters_hidden,cluster_found=clusters_found)
	ce_local = ce(cluster_hidden=clusters_hidden,cluster_found=clusters_found)
	nb_clusters = np.unique(clusters_found).size
	return [accuracy_local, ce_local,nb_clusters]

def get_evaluation_string(evaluations, evaluation_names):
	txt = ""
	for i,evalu in enumerate(evaluations):
		txt += evaluation_names[i]+"="+"{0:.2f}".format(evalu)+" "
	return txt

# Read the dataset
base_name = 'Datasets/pendigits'
file_name = base_name+".csv"
df = pd.read_csv(file_name, index_col=0, comment = "#")
y = df[df.columns[-1]]
df.drop(df.columns[-1],axis=1, inplace=True)
df = df.astype(float)

# Easy default parameter setting
D = df.shape[1]
NbExpClust = 30
SDmax = int(D * NbExpClust)
N = 25 * NbExpClust
NbIter = 10 * SDmax * NbExpClust

# Create SubCMedians Instance
scm = SubCMedians(D = D,
				  SDmax = SDmax,
				  N = N,
				  NbIter = NbIter)

print "====== Execution of SubCMedians version 1.1.0 (single threaded version) ======"
print "====== Parameters ======\n"
print "Random seed: "+str(seed)
print "Maximal model size SDmax="+str(scm.SDmax)
print "Sample size N="+str(scm.N)
print "Number of iterations NbIter="+str(scm.NbIter)
sys.stdout.write("====== Creating Subspace Clustering Model ======")
time0 = time.time()
scm.fit(df)
evaluation_names = ["Acc.", "CE", "NbClust."]
df_evaluation = pd.DataFrame()
df_evaluation["clusters_found"] = list(scm.predict(df.values))
df_evaluation["clusters_hidden"] = list(y)
clusters_found = df_evaluation["clusters_found"]
clusters_hidden = df_evaluation["clusters_hidden"]
runtime = str(time.time()-time0)
evaluation_temp = generate_evaluation(clusters_found, clusters_hidden)
txt = get_evaluation_string(evaluation_temp, evaluation_names)+" Runtime="+runtime
print txt

