import numpy as np
from sklearn.metrics import mean_squared_error, r2_score, mean_squared_log_error, log_loss

# 2値予測（確率）向け評価指標
def cal_logloss(y_true, y_pred, param_cnt=0):
	'''
		LOG_LOSSの計算するためのメソッド。

		Args:
			y_true(numpy.array): 正解データリスト
			y_pred(numpy.array): 予測データリスト
			param_cnt(int): 予測時のパラメータ数［不要］

		Returns:
			logloss_val(float): LOG_LOSSの計算値
	'''
	logloss_val = log_loss(y_true, y_pred)

	return logloss_val

# 回帰分析向け評価指標
def cal_rmsle(y_true, y_pred, param_cnt=0):
	'''
		RMSLEの計算するためのメソッド。

		Args:
			y_true(numpy.array): 正解データリスト
			y_pred(numpy.array): 予測データリスト
			param_cnt(int): 予測時のパラメータ数［不要］

		Returns:
			rmsle_val(float): RMSLEの計算値
	'''
	rmels_val = np.sqrt(mean_squared_log_error(y_true, y_pred))

	return rmsle_val

def cal_rmse(y_true, y_pred, param_cnt=0):
	'''
		RMSEの計算するためのメソッド。

		Args:
			y_true(numpy.array): 正解データリスト
			y_pred(numpy.array): 予測データリスト
			param_cnt(int): 予測時のパラメータ数［不要］

		Returns:
			rmse_val(float): RMSEの計算値
	'''
	rmes_val = np.sqrt(mean_squared_error(y_true, y_pred))

	return rmse_val

def cal_r2_score(y_true, y_pred, param_cnt=0):
	'''
		R2値の計算するためのメソッド。

		Args:
			y_true(numpy.array): 正解データリスト
			y_pred(numpy.array): 予測データリスト
			param_cnt(int): 予測時のパラメータ数［不要］

		Returns:
			r2_val(float): R2値の計算値
	'''
	r2_val = r2_score(y_true, y_pred) 

	return r2_val

def cal_aic(y_true, y_pred, param_cnt):
	'''
		AICの計算するためのメソッド。

		Args:
			y_true(numpy.array): 正解データリスト
			y_pred(numpy.array): 予測データリスト
			param_cnt(int): 予測時のパラメータ数

		Returns:
			aic_val(float): AICの計算値
	'''
	res = y_true - y_pred
	rss = np.dot(res.T, res)
	aic_val = len(y_pred) * (np.log(2 * np.pi * rss / len(y_pred)) + 1) + 2 * param_cnt

	return aic_val

def cal_bic(y_true, y_pred, param_cnt):
	'''
		BICの計算するためのメソッド。

		Args:
			y_true(numpy.array): 正解データリスト
			y_pred(numpy.array): 予測データリスト
			param_cnt(int): 予測時のパラメータ数

		Returns:
			bic_val(float): BICの計算値
	'''
	res = y_true - y_pred
	rss = np.dot(res.T, res)
	bic_val = len(y_pred) * (np.log(2 * np.pi * rss / len(y_pred)) + 1) + np.log(len(y_pred)) * param_cnt

	return bic_val




