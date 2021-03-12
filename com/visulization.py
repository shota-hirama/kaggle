import matplotlib.pyplot as plt
import seaborn as sns
import numpy as np

import file_handle

#グラフのスタイルをseabornに変更
sns.set(font='Meiryo')

class data_visulization():
    '''
        構造化データを可視化するためのクラス。
    '''

	def join_name(f_name, plot_name):
		'''
            可視化ファイル名取得のためのメソッド。

            Args:
                f_name(str): 解析名
                plot_name(str): 出力グラフ名
        '''
		name = plot_name
		if f_name != "":
			name = f_name + "_" + plot_name
		return name


    def output_fig(self, plt, dst_path, f_name):
        '''
            可視化結果を出力するためのメソッド。

            Args:
                plt(module): 可視化結果
                dst_path(str): 可視化結果出力先フォルダ
                f_name(str): 可視化結果出力ファイル名
        '''
        if dst_path != "":
            dst = file_handle.join_path([dst_path, f_name])
            plt.savefig(dst)
        else:
            plt.show()
        plt.close('all')

    def heatmap(self, input_data, f_name="", dst_path=""):
        '''
            ヒートマップを出力するためのメソッド。

            Args:
                input_data(pandas.DataFrame): グラフ描写のためのデータ
				f_name(str): 解析名
                dst_path(str): 可視化結果出力先フォルダ
        '''
        plt.figure(figsize=(15, 15))
        sns.heatmap(input_data, annot=True, fmt="1.2f", cmap="coolwarm", square=True, vmax=1, vmin=-1)
		name = join_name(f_name, "heatmap.jpg")
        self.output_fig(plt, dst_path, name)

    def pairplot(self, input_data, f_name="", dst_path=""):
        '''
            ペアープロット(単相関/分布)を出力するためのメソッド。

            Args:
                input_data(pandas.DataFrame): グラフ描写のためのデータ
				f_name(str): 解析名
                dst_path(str): 可視化結果出力先フォルダ
        '''
        sns.pairplot(input_data)
		name = join_name(f_name, "pairplot.jpg")
        self.output_fig(plt, dst_path, name)

    def plot(self, input_data, x_col_nm="", f_name="", dst_path=""):
        '''
            線グラフを出力するためのメソッド。

            Args:
                input_data(pandas.DataFrame): グラフ描写のためのデータ
                x_col_nm(str): X軸に設定する列名称
				f_name(str): 解析名
                dst_path(str): 可視化結果出力先フォルダ
        '''
        rows, cols = input_data.shape
        if x_col_nm == "":
            x = range(rows)
            input_data_ = input_data
        else:
            x = input_data[x_col_nm].values
            cols = cols - 1
            input_data_ = input_data.drop(x_col_nm, axis=1)


        fig = plt.figure(figsize=(20, 3 * cols))

        for i, col_nm in enumerate(input_data_.columns):
            ax = fig.add_subplot(cols, 1, i + 1)
            y = input_data[col_nm].values
            ax.plot(x, y, label=col_nm, marker=".")
            plt.legend()
		name = join_name(f_name, "plot.jpg")
        self.output_fig(plt, dst_path, name)

    def distplot(self, input_data, f_name="", dst_path=""):
        '''
            ヒスト(分布)を出力するためのメソッド。

            Args:
                input_data(pandas.DataFrame): グラフ描写のためのデータ
				f_name(str): 解析名
                dst_path(str): 可視化結果出力先フォルダ
        '''
        rows, cols = input_data.shape

        if cols >= 3:
            # 切り上げにするための計算
            ax_row = -(-1 * cols // 3)
            ax_col = 3
        else:
            ax_row = 1
            ax_col = cols
        fig = plt.figure(figsize=(5 * ax_col, 4 * ax_row))

        for i, col_nm in enumerate(input_data.columns):
            ax = fig.add_subplot(ax_row, ax_col, i + 1)
            x = input_data[col_nm].values

            std = np.std(x)
            if std == 0.0:
                kde = False
            else:
                kde = True

            sns.distplot(x, label=col_nm, ax=ax, kde=kde)
            plt.legend()
		name = join_name(f_name, "distplot.jpg")
        self.output_fig(plt, dst_path, name)

    def scatter(self, input_data, x_col_nm="", y_col_nm="", f_name="", dst_path=""):
        '''
            散布図を出力するためのメソッド。

            Args:
                input_data(pandas.DataFrame): グラフ描写のためのデータ
                x_col_nm(str): X軸に設定する列名称
                y_col_nm(str): Y軸に設定する列名称
				f_name(str): 解析名
                dst_path(str): 可視化結果出力先フォルダ
        '''
        plt.figure(figsize=(15, 15))
        x = input_data[x_col_nm].values
        y = input_data[y_col_nm].values
        plt.scatter(x, y)
        plt.grid(True)
        plt.xlabel(x_col_nm)
        plt.ylabel(y_col_nm)
		name = join_name(f_name, "scatter.jpg")
        self.output_fig(plt, dst_path, name)