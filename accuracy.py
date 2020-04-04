#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Mar 17 09:06:15 2020

@author: tejas
"""


from scipy.stats import multivariate_normal
from sklearn.mixture import GaussianMixture
from python_speech_features import mfcc
from python_speech_features import logfbank
import matplotlib.pyplot as plt
import scipy.io.wavfile as wav
import os
import sys
import numpy as np
import xlwt 
from xlwt import Workbook
wb=Workbook()
sheet3=wb.add_sheet('Sheet 3')
#sheet1.write(0,0,'Languages')
#sheet1.write(0,4,'L1')
#sheet1.write(0,5,'L2')
#sheet1.write(0,6,'L3')
#sheet1.write(0,7,'L4')
#sheet1.write(0,8,'L5')

#wb.save('xlwt example.xls') 
temp=-2**31-1
a=0
q=0;
p=[]
li=[]
c=-1;
import xlwt 
from xlwt import Workbook
wb=Workbook()
sheet1=wb.add_sheet('Sheet 1')
with os.scandir('/home/tejas/Desktop/cutted audio')as files:
#with os.scandir('/home/tejas/Desktop/cutted audio/5 english')as values:
    #sheet1.write(2,0,'5 english')  
    for file in files:
        #print (file.name)
        c=c+1
        with os.scandir(file)as values:
            for value in values:
                print (value.name)
                q=q+1
                (rate,sig)=wav.read(value)
                mfcc_feat=mfcc(sig,rate)
        #z=None
                l1=[]
                for m in range(1,6):
                    means=np.loadtxt(fname="/home/tejas/Desktop/lang6/4:1/a_0.9/mean/""{0}{1}".format("L",m),delimiter=',')
                    covar=np.loadtxt(fname="/home/tejas/Desktop/lang6/4:1/a_0.9/covariance/""{0}{1}".format("L",m),delimiter=',')
                    weight=np.loadtxt(fname="/home/tejas/Desktop/lang6/4:1/a_0.9/weight/""{0}{1}".format("L",m),delimiter=',')
                    k=None
                    z=None
                    for j in range(0,len(mfcc_feat)):
                         z=None
                         for i in range(0,16):
                             s=multivariate_normal.pdf(mfcc_feat[j,:],means[i,:],covar[i,:])
                             if z is None:
                                z=weight[i,]*s
                             else:
                                z=z+weight[i,]*s
                
                         if k is None:
                            k=np.log(z)
                         else:
                            k=k+np.log(z) 
                l1.insert(m,k)
                h=np.where(l1==np.amax(l1))
        #print(h[0][0])
                p.insert(0,h[0][0]+1)
                sheet1.write(c,2+q,str(h[0][0]+1))
        q=0        
        sheet1.write(c,0,file.name) 
        c=c+1

wb.save('l.xls')   
#print(p)        
#res = max(set(p), key = p.count)
#print(res)
#if res is 1:
#   print ('marathi')
#elif res is 2:
#    print('punjabi')
#elif res is 3:
#    print ('sanskrit')
#elif res is 4:
#    print('hindi') 
#elif res is 5:
#    print('english')       