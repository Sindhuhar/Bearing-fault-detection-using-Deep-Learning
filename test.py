



import scipy.io 
#import scipy
import numpy as np
from sklearn.model_selection import train_test_split, KFold
from sklearn.metrics import confusion_matrix
import tensorflow as tf
from tensorflow.keras import layers, models
import matplotlib.pyplot as plt
import seaborn as sns 
import pandas as pd




def ImportData():
  X99_normal = scipy.io.loadmat('./BearingData_CaseWestern/99.mat')['X099_DE_time']              





print( ImportData() )


