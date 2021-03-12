import os
import configparser
import pandas as pd

def read_ini(ini_path):
	'''
		.iniを読み込むためのメソッド。

		Args:
			ini_path(str): .iniファイルのパス
	'''
	ini = configparser.ConfigParser()
	ini.read(ini_path)

	return ini

def make_dir(path):
	'''
		フォルダ作成のメソッド。

		Args:
			path(str): 作成フォルダのパス
	'''
	os.makedirs(path, exist_ok=True)

def output_pandas(path, pd_data):
	'''
		pandas出力メソッド。

		Args:
			path(str): 作成ファイルのパス
			pd_data(pandas.DataFrame): pandasデータフレーム
	'''
	dirname = os.path.dirname(path)
	make_dir(dirname)

	root, ext = os.path.splitext(path)

	if str.upper(ext) == ".CSV":
		data.to_csv(path, index=False)
	elif  str.upper(ext) == ".XLSX" or str.upper(ext) == ".XLS":
		data.to_excel(path, index=False)

def join_path(path_list):
	return os.path.join(path_list)

