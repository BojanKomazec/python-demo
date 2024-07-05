import pandas as pd

def init_demo():

	#
	# Convert a tuple into Pandas dataframe
	# 
	tuple1 = ('this', 'is', 'a', 'test')
	print(f'type(tuple1) = {type(tuple1)}')

	data_frame1 = pd.DataFrame({'word': tuple1})

	print(f'data_frame1 = \n{data_frame1}')
	# Output:
	# data_frame1 = 
	#    word
	# 0  this
	# 1    is
	# 2     a
	# 3  test

	list_of_tuples = [
		('Bojan', 35),
		('Anna', 33),
		('Bane', 27),
	]

	data_frame2 = pd.DataFrame.from_records(list_of_tuples, columns = ['Name', 'Age'] )
	print(f'data_frame2 = \n{data_frame2}')

def pandas_demo():
	init_demo()

pandas_demo()
