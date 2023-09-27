import os
import pandas as pd
#file_path ='django_excel.xlsx'

#file_path = os.path.join(os.path.dirname(os.path.dirname(os.path.abspath(__file__))), 'myproject', 'django_excel.xlsx')
file_path = os.path.join(os.path.dirname(os.path.abspath(__file__)), 'django_excel.xlsx')


df = pd.read_excel(file_path)
if os.path.exists(file_path):
    df = pd.read_excel(file_path)
    print("File exist")
    # Continue processing the file
else:
    print("The file does not exist.")
df = pd.read_excel(file_path)
#print("The data: ", df.head())

#reading the field_names 
field_names = df.columns.tolist()
lower_field_names=[x.lower() for x in field_names]
print(lower_field_names)
print("The fields are: ", field_names)



