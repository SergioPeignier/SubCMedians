# SubCMedians
SubCMedians is a Subspace Clustering algorithm that extends the K-medians paradigm.
SubCMedians is a simple hill climbing algorithm based on stochastic weighted local exploration steps.
This median based algorithm exhibits satisfactory quality clusters when compared to well-established paradigms, while medians have still their own interests depending on the user application (robustness to noise/outliers and location optimality).

# Installation
Dependencies :

+ python 2.7 (anaconda distribution by continuum analytics contains every needed library, otherwise, you'll need to install numpy, pandas, seaborn and scikit-learn)
+ SubCMedians compilation : We provide binaries for OS X (should also work for Linux). If you need to compile it yourself for any purpose, sources are provided, and can be compiled via the command "python2.7 setup.py build_ext --inplace" in the SubCMediansLib/C/ folder. If you have any question please feel free to contact me.

# Usage

A simple example is provided in the `script.py` file. The basic steps are stated hereafter:
+ Load the SubCMedians library `from SubCMediansLib.pySubCMedians import SubCMedians`
+ Create a SubCMedians subspace clustering engine instance: `scm = SubCMedians(D = D, SDmax = SDmax, N = N, NbIter = NbIter)`
	+ `D` is the dataset dimensionality (number of features).
	+ `SDmax` is the maximal model weight.
	+ `N` is the data sample size
	+ `NbIter` is the number of iterations
+ A simple default parameter setting that has shown to be sufficient in many cases depends on a single parameter, the Number of Expected Clusters `NbExpClust`. Then the other parameters are set as follows:	
	+ `SDmax = int(D * NbExpClust)`
	+ `N = 25 * NbExpClust`
	+ `NbIter = 10 * SDmax * NbExpClust`
+ Compute the Subspace Clustering model `scm.fit(df)` of the dataset `df` (numpy array or pandas data frames supported)