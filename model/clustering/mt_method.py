import sys
sys.path.append('../../com')
import os
import numpy as np
from visualization import data_visulization as dv
from data_check import DataCheck as DC
from file_handle import FileHandle

class MtMethod():
    '''
        MT法を実行するためのクラス。
    '''

    def chk_standard_space(self, input_data, dst_path="", x_col_plot=""):
        '''
            MT法の標準空間に使用するデータを確認するためのメソッド。

            Args:
                input_data(pandas.DataFrame): 標準空間を作るためのデータ(項目数以上のサンプルデータが必要)
                dst_path(str): 可視化結果出力先フォルダ
                x_col_plot(str): 可視化結果出力先フォルダ
        '''
        dst_path_ = FileHandle.join_file(dst_path, "mt_check")

        #トレンドグラフの可視化
        dv.plot(input_data, x_col_plot, dst_path_)
        #分布の可視化
        dv.distplot(input_data, dst_path_)
        #データの統計情報を取得
        DC.check_main(input_data, dst_path_)

    def cal_standard_space(self, input_data):
        '''
            MT法の標準空間の平均/相関行列/項目数を計算するためのメソッド。

            Args:
                input_data(pandas.DataFrame): 標準空間を作るためのデータ(項目数以上のサンプルデータが必要)
        '''
        self.mean = np.mean(input_data, axis=0)
        self.cov_i = np.linalg.pinv(np.cov(input_data.T))
        self.col_cnt = len(self.mean)

    def setup_standard_space(self, mean, cov_i, col_cnt):
        '''
            MT法の標準空間の平均/相関行列/項目数を設定するためのメソッド。

            Args:
                mean(np.array): 標準空間を作成した際の各項目ごとの平均値
                cov_i(np.array): 標準空間を作成した際の相関行列
                col_cnt(int): 標準空間を作成した際の項目数
        '''
        self.mean = mean
        self.cov_i = cov_i
        self.col_cnt = col_cnt

    def cal_mt(self, input_data):
        '''
            MD法の計算するためのメソッド。

            Args:
                input_data(pandas.DataFrame): MD法を計算するための各項目データのリスト

            Returns:
                md(float): MD法を計算結果
        '''
        stan_data = input_data - self.mean
        md = np.sqrt(np.dot(np.dot(stan_data, self.cov_i), stan_data.T) / self.col_cnt)
        return  md