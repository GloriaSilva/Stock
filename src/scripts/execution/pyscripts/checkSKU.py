
import pandas as pd
from pandas import ExcelWriter
from datetime import date, datetime
import os
from dotenv import load_dotenv
from openpyxl import load_workbook 
import numpy as np
import xlsxwriter




load_dotenv()

dateY=str(date.today())
path=os.getenv('PROJECT_PATH')




reportES=path+'file/'+'report_es_'+dateY+'.xlsx'


#Leer archivos reporte excel de España de la carpeta "file"
df=pd.read_excel(reportES)
#Cambiar el nombre de la columna 'Text availability'
df.rename({'Text Availability':'CTA'}, axis=1, inplace=True )
#Rellenar con 0 los espacios vacíos
df['CTA']=df['CTA'].fillna(0)
#Cresr un DF con las columnas necesarias
df_exc=pd.DataFrame(df, columns=['SKU', 'EAN', 'Title', 'Availability', 'CTA'])
#Reescribir el excel existente
writer=ExcelWriter(reportES)
df_exc.to_excel(writer, 'Sheet0', index=False)
writer.save()


#indexar el archivo de "noStock"
x=pd.read_excel(reportES)

indx=[]

#Extraer productos de "in stock" y "pre order" que no permitan añadir al carrito. Es decir, no tengan los CTAs:
# "comprar", "añadir al carrito" o "precomprar" o extraer los que no tienen stock
for i in range(len(x.SKU)):
    if x.Availability[i] == 'pre order' and (x.CTA[i] == 'recibir alertas de stock' or x.CTA[i] == 'producto no disponible.' or x.CTA[i] == 'dónde comprar' or x.CTA[i] == 0 or x.CTA[i] =='agotado'):

            indx.append(i)
    elif x.Availability[i]== 'in stock' and (x.CTA[i] == 'recibir alertas de stock' or x.CTA[i] == 'producto no disponible.' or x.CTA[i] == 'dónde comprar' or x.CTA[i] == 0 or x.CTA[i] =='agotado'):

            indx.append(i)
    elif x.Availability[i]=='out of stock' and (x.CTA[i] == 'comprar' or x.CTA[i] == 'añadir al carrito') :

        indx.append(i)


stockReview=x.iloc[indx]
dataframe1=pd.DataFrame(stockReview)





#Empieza revision de PT---------------

reportPT=path+'file/'+'report_pt_'+dateY+'.xlsx'

#Leer archivos reporte excel de España de la carpeta "file"
df1=pd.read_excel(reportPT)
#Cambiar el nombre de la columna 'Text availability'
df1.rename({'Text Availability':'CTA'}, axis=1, inplace=True )
#Rellenar con 0 los espacios vacíos
df1['CTA']=df1['CTA'].fillna(0)
#Cresr un DF con las columnas necesarias
df_exc2=pd.DataFrame(df1, columns=['SKU', 'EAN', 'Title', 'Availability', 'CTA'])
#Reescribir el excel existente
writer2=ExcelWriter(reportPT)
df_exc2.to_excel(writer2, 'Sheet0', index=False)
writer2.save()


#indexar el archivo de "noStock"
y=pd.read_excel(reportPT)


indx2=[]

#Extraer productos de "in stock" y "pre order" que no permitan añadir al carrito. Es decir, no tengan los CTAs:
# "comprar", "añadir al carrito" o "precomprar" o extraer los que no tienen stock
for i in range(len(y.SKU)):
    if y.Availability[i] == 'pre order' and (y.CTA[i] == 'recibir alertas de stock' or y.CTA[i] == 'producto no disponible.' or y.CTA[i] == 'dónde comprar' or y.CTA[i] == 0 or y.CTA[i] =='agotado'):

            indx2.append(i)
    elif y.Availability[i]== 'in stock' and (y.CTA[i] == 'recibir alertas de stock' or y.CTA[i] == 'producto no disponible.' or y.CTA[i] == 'dónde comprar' or y.CTA[i] == 0 or y.CTA[i] =='agotado'):

            indx2.append(i)
    elif y.Availability[i]=='out of stock' and (y.CTA[i] == 'comprar' or y.CTA[i] == 'añadir al carrito') :

        indx2.append(i)


stockReviewPT=y.iloc[indx2]
dataframe2=pd.DataFrame(stockReviewPT)


with pd.ExcelWriter('stockReview.xlsx', engine='xlsxwriter') as writer:
    dataframe1.to_excel(writer, sheet_name='ES')
    dataframe2.to_excel(writer, sheet_name='PT')




print('done')