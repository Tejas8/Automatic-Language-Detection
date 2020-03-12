
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
li=[]
with os.scandir('/home/tejas/Desktop/Sanjanasharmapun')as values:
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
            #l1.insert(m,k)
            
            sheet3.write(2+q,m,k)
        sheet3.write(2+q,0,value.name)   

wb.save('xlwt2 example.xls')             
        print(l1)
#y = multivariate_normal.pdf(mfcc_feat[:,0], mean=1.679289181802354136e+01, cov=5.549530598306957607e+00)

    #for j in range(0,13):
    
    #np.savetxt('/home/tejas/Desktop/X',X,delimiter=',')
    
    #print(weight[i,]*s)
      #      l=z.shape
  
                 

