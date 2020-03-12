#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Sep 28 02:05:21 2019

@author: tejas
"""
from sklearn.mixture import GaussianMixture
from python_speech_features import mfcc
import numpy as np
dataset = np.loadtxt(fname = "/home/tejas/Desktop/lang6/4:1/test1.out", delimiter=',')
gmm = GaussianMixture(n_components=16,covariance_type='diag').fit(dataset)
a=0.9
w=weighttot=(gmm.weights_)
m=meantot=(gmm.means_)
#(np.sum(gmm.weights_))
c=covatot=gmm.covariances_

index=0
for index in range (1,6):
    dataset1=np.loadtxt(fname = "/home/tejas/Desktop/lang6/4:1/mfcc_each_lang/""{0}{1}".format("L", index),delimiter=',')
    gmm1=GaussianMixture(n_components=16,covariance_type='diag').fit(dataset1)
    X=gmm2=a*gmm1.weights_+(1-a)*w
    np.savetxt('/home/tejas/Desktop/lang6/4:1/a_0.9/weight/'"{0}{1}".format("L", index),X,delimiter=',')
    X=None
    X=gmm3=a*gmm1.covariances_+(1-a)*c

    np.savetxt('/home/tejas/Desktop/lang6/4:1/a_0.9/covariance/'"{0}{1}".format("L", index),X,delimiter=',')
    X=None
    X=gmm4=a*gmm1.means_+(1-a)*m
    np.savetxt('/home/tejas/Desktop/lang6/4:1/a_0.9/mean/'"{0}{1}".format("L", index),X,delimiter=',')
    


