from datetime import date
import pandas as pd
import pyodbc

# Define the path to your Excel file
excel_file_path = r'C:\Users\smitl\Desktop\ESMSYS\MH_WS_Sep23.xlsx'

# Create a connection string
connection = pyodbc.connect('Driver={ODBC Driver 17 for SQL Server};Server=mssql.esmsys.in,14251;Database=jn-common-qa;uid=dotnet_dev;pwd=Esm@Dot%2023')
cursor = connection.cursor()

df = pd.read_excel(excel_file_path)
date_col = []
state_id = []
for i in range(len(df['District'])):
    date_col.append(str(date.today()))
    state_id.append('15')

df.insert(3, 'Date', date_col)
df.insert(4, 'state_id',state_id)

# Define the target table name
target_table = 'tblVTD_Master_Scrap'

# Iterate through the rows of the DataFrame and insert each row into the SQL Server table
for index, row in df.iterrows():
    print(index,row)
    cursor.execute(f"INSERT INTO {target_table} (District, Taluka, Village, Date, state_id) VALUES (?, ?, ?, ?, ?)", row['District'], row['Taluka'], row['Village'], row['Date'], row['state_id'])
    connection.commit()

# Commit the transaction
print(f'Data inserted successfully into {target_table}.')
