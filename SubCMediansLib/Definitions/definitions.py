NOT_ZERO_DIVISION_SECURITY = 0.0000000001
SEP_IN_FILE         = "\t"
END_OF_LINE_FILE    = "\n"
COMMENTS_IN_FILE    = '# '
STD_LAMBDA = 1
STD_ETA= 1

FIFO         = 1
FIRO         = 0
INSERT_ATOM_TO_CENTER_PROPORTIONAL_TO_COMPLEXITY = 0
INSERT_ATOM_TO_CENTER_PROPORTIONAL_TO_NUMBER_OF_OBJECTS = 1
INSERT_ATOM_TO_CENTER_PROPORTIONAL_TO_INVERSE_NUMBER_OF_OBJECTS = 2

DELETE_ATOM_PORTIONAL_TO_COMPLEXITY = 0
DELETE_ATOM_PROPORTIONAL_TO_NUMBER_OF_POINTS = 1
DELETE_ATOM_PROPORTIONAL_TO_INVERSE_NUMBER_OF_POINTS = 2

STD_SDmax      = 5000
STD_D = 1000
STD_N         = 1000
STD_THRESHOLD_CLUSTER_VALIDITY       = 0
STD_SEED      = 0       
STD_PRECISION = 1000
STD_OPT_DEL = 0
STD_OPT_INS = INSERT_ATOM_TO_CENTER_PROPORTIONAL_TO_COMPLEXITY
STD_FIFO = FIFO
STD_TRAIN_WITH_LATEST = 0
STD_LAZY_HILL_CLIMBING = 1

DIMID     = 0
DIMWEIGHT = 1
DIMPOS    = 2

POINTWEIGHT = 0
POINTINDEX  = 1
POINTGROUPID = 2
POINTCLASSID =3
POINTDISPERSION = 4
NBPOINTSINCLUSTER = 5
POINTDESCRIPTORS = 6

NBFEATURES = 11

PyDISPERSIONFEATURE = 0
PyKFEATURE = 1
PyNBCOREPOINTS = 2
PyNBCLUSTERS = 3
PyMEANDIMCOREPOINTS = 4
PyMEANDIMCLUSTERS = 5
PyMEANATOMCOREPOINTS = 6
PyMEANATOMCLUSTERS = 7
PyMEANATOMDIMCOREPOINTS = 8
PyMEANATOMDIMCLUSTERS = 9
PyCOVERAGE = 10
PyGENERATION = 11
STD_NbIter = 10000

AS_LIST = 0
AS_CAPSULE = 1
features_header = ["dispersion",
"K",
"NbCorePoints",
"NbClusters",
"AvgDimCorePoints",
"AvgDimClusters",
"AvgAtomCorePoints",
"AvgAtomClusters",
"AvgAtomDimCorePoints",
"AvgAtomDimClusters",
"Coverage",
"Generation"]

evaluation_header = ["SAE",
"entropy",
"accuracy",
"f1",
"ce",
"rnia",
"ce_ssc",
"nbNotNoiseClusters",
"AvgDimNotNoiseClusters",
"runTime"]