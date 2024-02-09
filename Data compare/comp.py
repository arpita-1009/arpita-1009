import pandas as pd
import pypyodbc
connection = pypyodbc.connect('Driver={ODBC Driver 17 for SQL Server};Server=mssql.esmsys.in,14251;Database=proplegit-adani;uid=esmsysqadb;pwd=Yvf#eo-2X*Ff(Dd')
cur2 = connection.cursor()
# Step 1: Read data from the source Excel file
source_file = "Data compare/LOCATIONS_DATA_01112023.xlsx"  # Replace with the path to your source Excel file
df_source = pd.read_excel(source_file)
data_list = df_source.values.tolist()

# print(data_list)
database = []
try:
    for i in range(0 , len(data_list)):
        state = data_list[i][1]
        Dist = data_list[i][2]
        tal = data_list[i][3]
        vill = data_list[i][4]
        cur2.execute("SELECT * from tblState s , tbldistrict d, tbltaluka t, tblvillage v where s.StateName = '"+state+"' and d.DistrictName = '"+Dist+"' and t.TalukaName = '"+tal+"'   and v.VillageName = '"+vill+"'")
        fetch_userid = cur2.fetchall()
        print(fetch_userid)
        if len(fetch_userid) == 0:
            summary = 'False'
        else:
            summary = 'True'
        # if state == 'UTTAR PRADESH':
        #     break

        print(state , Dist ,tal,vill , summary)
        database.append(str(i)+'%'+str(state)+'%'+str(Dist)+'%'+ str(tal) +'%'+str(vill) +'%'+str(summary))


    # # Create DataFrame and DataStore in Excel 
    a = [i.split('%') for i in  database]
    df = pd.DataFrame(a,columns=['No','State','District','Taluka','Village','Summary'])
    df.to_excel('Diifgetlocation.xlsx',index=True,  engine='xlsxwriter')

except:
    a = [i.split('%') for i in  database]
    df = pd.DataFrame(a,columns=['No','State','District','Taluka','Village','Summary'])
    df.to_excel('Diifgetlocation.xlsx',index=True,  engine='xlsxwriter')
