import pandas as pd
from procesarNotas_11_10 import procesarNotas
from procesarNotas_1_9 import procesarNotas_1_9
import json
from pymongo import MongoClient


# Ejecutar para distintos archivos
resultado11 = procesarNotas("PERIODO 2", "./periodos/Sabana_de_notas_descriptiva_11.xlsx")
resultado10 = procesarNotas("PERIODO 2", "./periodos/Sabana_de_notas_descriptiva_10.xlsx")
resultado9 = procesarNotas_1_9("PERIODO 2", "./periodos/Sabana_de_notas_descriptiva_9.xlsx")
resultado8 = procesarNotas_1_9("PERIODO 2", "./periodos/Sabana_de_notas_descriptiva_8.xlsx")
resultado7 = procesarNotas_1_9("PERIODO 2", "./periodos/Sabana_de_notas_descriptiva_7.xlsx")
resultado6 = procesarNotas_1_9("PERIODO 2", "./periodos/Sabana_de_notas_descriptiva_6.xlsx")
resultado5 = procesarNotas_1_9("PERIODO 2", "./periodos/Sabana_de_notas_descriptiva_5.xlsx")
resultado4 = procesarNotas_1_9("PERIODO 2", "./periodos/Sabana_de_notas_descriptiva_4.xlsx")
resultado3 = procesarNotas_1_9("PERIODO 2", "./periodos/Sabana_de_notas_descriptiva_3.xlsx")
resultado2 = procesarNotas_1_9("PERIODO 2", "./periodos/Sabana_de_notas_descriptiva_2.xlsx")
resultado1 = procesarNotas_1_9("PERIODO 2", "./periodos/Sabana_de_notas_descriptiva_1.xlsx")
 

# Concatenar resultados
df_data_concatenado = pd.concat([
    resultado11,resultado10,resultado9,resultado8,resultado7,resultado6,
    resultado5,resultado4,resultado3,resultado2,resultado1
    ])

# # Exportar a Excel
# ruta_salida = "./Notas_Periodo1.xlsx"
# df_data_concatenado.to_excel(ruta_salida, index=False)
# print(f"Archivo Excel creado en: {ruta_salida}")
 
# Convertir el DataFrame a JSON (sin secuencias de escape)
df_data_concatenado = df_data_concatenado.to_json(orient='records', lines=False, force_ascii=False)

# Guardar el archivo JSON en UTF-8
with open('consolidado.json', 'w', encoding='utf-8') as json_file:
    json.dump(json.loads(df_data_concatenado), json_file, ensure_ascii=False, indent=4)
    

# Conexión a MongoDB (ajusta el puerto y la URI si es necesario)
client = MongoClient("mongodb+srv://alfredomontoyacorreo2:dbcpcs2024@cluster0.wu0k7uf.mongodb.net/")

with open("consolidado.json", "r", encoding="utf-8") as file:
    data = json.load(file)

# Seleccionar la base de datos y colección
db = client["test"]
collection = db["studentnotes"]
 

# collection.delete_many({})  # limpiar todo antes
collection.insert_many(data)
total = collection.count_documents({})
print(f'Insertados en Mongo : {total} registros')


 
