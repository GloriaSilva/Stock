
import pandas as pd
from pandas import ExcelWriter
from datetime import date, datetime
import os
from dotenv import load_dotenv
import workbook as wb
from StyleFrame import StyleFrame, Styler, utils

load_dotenv()

dateY=str(date.today())
path=os.getenv('PROJECT_PATH')

report=path+'file/'+'report_es_'+dateY+'.xlsx'

#Leer archivos reporte excel de la carpeta "file"
df=pd.read_excel(report)
df.rename({'Text Availability':'CTA'}, axis=1, inplace=True )
df['CTA']=df['CTA'].fillna(0)
df_exc=pd.DataFrame(df, columns=['SKU', 'EAN', 'Title', 'Availability', 'CTA'])
writer=ExcelWriter(report)
df_exc.to_excel(writer, 'Sheet0', index=False)
writer.save()


#indexar el archivo de "noStock"
x=pd.read_excel(report)

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

cell_format = wb.add_format()

#Generar archivo para enviar
stockReview.to_excel('stockReview.xlsx')
