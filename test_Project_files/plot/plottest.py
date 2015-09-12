import numpy as np
import toCart
import plot as pt
import Outlier as oo
import iqd 
import Sparser as SS
import RANSAC as rr
import time
x = np.array([[  15.,109.],[  20. , 109.], [  25. , 105.],[  30. , 107.], [  35. , 105.], [  40. , 106.], [  45. , 102.], [  50. , 104.], [  55. , 102.], [  60.  ,101.] ,[  65.  ,100.],[  70.  ,114.],[  75. ,  99.],[  80.,   98.],[  85.  , 96.],[  90. ,  97.],[  95. ,  94.],[ 100.,  110.],[ 105.  , 91.],[ 110. ,  94.],[ 115.  , 94.],[ 120.  , 91.],[ 125.  , 93.],[ 130. ,  91.],[ 135.  , 89.],[ 140.  , 89.],[ 145. , 111.],[ 150.,  101.],[ 155.,   90.],[ 160.,   95.],[ 165. , 110.] ,[ 170.   ,92.],[ 165. ,  91.] ,[ 160.   ,90.], [ 155. ,  90.], [ 150. ,  91.], [ 145. , 110.], [ 140. ,  89.], [ 135. ,  92.], [ 130.,  109.], [ 125.  , 90.],[ 120.,   91.] ,[ 115.,   90.],[ 110.   ,91.],[ 105. , 112.],[ 100. ,  96.],[  95.  , 91.],[  90. , 110.] ,[  85.   ,93.],[  80.  , 93.] ,[  75. ,  93.],[  70. ,  94.], [  65. , 115.], [  60.  , 95.], [  55. ,  96.], [  50. ,  97.], [  45. ,  97.], [  40. ,  99.], [  35. , 100.], [  30. , 101.], [  25. , 118.], [  20. , 102.]],dtype = float)
toCart.toCartesian(x)
#k = rr.nice(x)
#x = SS.sparse(x,20)
#oo.clearOutlier(x,1,2,4)
k = iqd.outlierRemoval(x,1)
pt.plotArray(k)
#pt.plotArray(x)
