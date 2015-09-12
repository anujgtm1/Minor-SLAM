from sklearn import linear_model
def nice(a):
	x = a[:,0]
	y = a[:,1]
	clt_ransac = linear_model.RANSACRegressor(linear_model.LinearRegression())
	clt_ransac.fit(x, y)
	yhat = clt_ransac.predict(x)
	inlier_mask = clt_ransac.inlier_mask_
	
#	print(clt_ransac.estimator_.coef_)
#	print(clt_ransac.estimator_.intercept_)
	return np.transpose([x, yhat])
