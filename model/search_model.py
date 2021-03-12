
def stepwise(input_data, model, evaluation_func, mode=None):
        '''
            MD法の計算するためのメソッド。

            Args:
                input_data(pandas.DataFrame): MD法を計算するための各項目データのリスト

            Returns:
                md(float): MD法を計算結果
        '''
	best_cols = []
	best_score = 0
	best_param = {}

	train_x, train_y, test_x, test_y = input_data

	cols = train_x.columns().values

	while True:

		for col in cols:

			if col in best_cols:
				continue

			tmp_cols = best_cols.copy()
			tmp_cols.append(col)

			train_x = train_x[tmp_cols]
			test_x = test_x[tmp_cols]

			if mode == "lbm":
				return

			else:
				model.fit(train_x, train_y)
				pred_y = model.predict(test_x)

				score = evaluation_func(				)



		





