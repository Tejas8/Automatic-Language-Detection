#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Sep 28 02:05:21 2019

@author: tejas
"""
#from sklearn. import GMM
from python_speech_features import mfcc
from python_speech_features import logfbank
import matplotlib.pyplot as plt
import scipy.io.wavfile as wav
import os
import numpy as np
#X=np.array([1.235662999131026218e+01,5.135665522398781269e-01,-9.069041267513476612e+00,-5.107590607860569065e+00,-1.870763869260885226e+00,1.182421954875965042e+01,-1.634106476514922024e+00,-6.143084894512931271e+00,-1.499750174967341865e+00,8.644761014813246547e+00,4.310536133255357782e+00,-5.331662382708723058e+00,-7.853376757771147965e+00])
#Y=np.array([1.235662999131026218e+01,5.135665522398781269e-01,-9.069041267513476612e+00,-5.107590607860569065e+00,-1.870763869260885226e+00,1.182421954875965042e+01,-1.634106476514922024e+00,-6.143084894512931271e+00,-1.499750174967341865e+00,8.644761014813246547e+00,4.310536133255357782e+00,-5.331662382708723058e+00,-7.853376757771147965e+00])
x=0
X=None
with os.scandir('/home/tejas/Desktop/lang6/4:1/train data/')as values:
    for value in values:
        print(value.name)
        with os.scandir(value) as entries:
            for entry in entries:
                (rate,sig) = wav.read(entry)
                mfcc_feat=mfcc(sig,rate)
                if X is None:
                    X=mfcc_feat
                else:
                    X=np.row_stack((X,mfcc_feat))
        
            #np.savetxt('/home/tejas/Desktop/lang6/4:1/mfcc_each_lang1/'"{0}{1}".format("L", value.name),X,delimiter=',')
            #x=x+1
            #X=None
    np.savetxt('test1.out', X, delimiter=',')
                
                