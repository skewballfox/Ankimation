import pandas as pd 

file=("./test_data/basic_cards.xlsx")

xl=pd.ExcelFile(file)

print(xl.parse('Sheet1'))

deck_name="Test"

for column, row in xl.parse('Sheet1').iterrows():
    print((str(column)+"{}").format(row))