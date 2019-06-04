"""
   Example of multi-label classification
   Apply on the medical data set
"""

from scipy.io.arff import loadarff

train = loadarff("./medical/medical-train.arff")
test  = loadarff("./medical/medical-test.arff")