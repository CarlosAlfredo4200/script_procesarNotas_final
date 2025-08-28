import pandas as pd

def procesarNotas_1_9(periodo, archivo):
    """
    Procesa el archivo de notas:
    - Quita filas y columnas innecesarias
    - Renombra columnas
    - Filtra por periodo
    - Ajusta tipos de datos
    - Reemplaza nombres de grados
    Retorna un DataFrame limpio
    """

    # --- Cargar archivo ---
    data_PI = pd.read_excel(archivo)

    # --- Elimina las primeras 8 filas ---
    data_sin_cabecera = data_PI.iloc[8:].reset_index(drop=True)
    
    # --- Adicionar las columnas faltantes ---
    cols_numericas = ["fisica", "quimica", "ciencias_politicas_economicas", "filosofia"]

    for col in cols_numericas:
        if col in data_sin_cabecera.columns:  # 🔑 si la columna ya existe
            data_sin_cabecera[col] = (
                data_sin_cabecera[col]
                .astype(str)  # convertir a string
                .str.replace(",", ".", regex=False)  # reemplazar comas por puntos
                .astype(float)  # convertir a float
            )
        else:
            # Si la columna no existe, la creamos con valor entero 0
            data_sin_cabecera[col] = 0

    # Convertir explícitamente las nuevas columnas a enteros
    data_sin_cabecera[cols_numericas] = data_sin_cabecera[cols_numericas].astype(int)
    

   
     
    # # --- Eliminar columnas innecesarias ---
    data_sin_cabecera = data_sin_cabecera.drop(columns=[
        'Unnamed: 0',
        'Unnamed: 7',
        'Unnamed: 8', 
        'Unnamed: 10',
        'Unnamed: 12',
        'Unnamed: 14',
        'Unnamed: 16',
        'Unnamed: 18',
        'Unnamed: 20',
        'Unnamed: 22',
        'Unnamed: 23',
        'Unnamed: 27',
        'Unnamed: 29',
        'Unnamed: 30',
        
    ])
    
    
    

    # # # # --- Renombrar columnas ---
    data_sin_cabecera = data_sin_cabecera.rename(columns={
        "Unnamed: 1": "grupo",
        "Unnamed: 2": "codigo",
        "Unnamed: 3": "nombre",
        "Unnamed: 4": "periodo",
        "Unnamed: 5": "puesto",
        "Unnamed: 6": "promedio",
        "Unnamed: 9": "ciencias_naturales",
        "Unnamed: 11": "ciencias_sociales",
        "Unnamed: 13": "civica_y_constitucion",
        "Unnamed: 15": "educacion_artistica",
        "Unnamed: 17": "educacion_cristiana",
        "Unnamed: 19": "educacion_etica",
        "Unnamed: 21": "educacion_fisica",
        "Unnamed: 24": "idioma_extranjero",
        "Unnamed: 25": "lengua_castellana",
        "Unnamed: 26": "matematicas",
        "Unnamed: 28": "tecnologia"
    })
   
   
     
    
    

    # --- Filtrar datos por periodo ---
    filtro_periodo = data_sin_cabecera[data_sin_cabecera["periodo"] == periodo].copy()
    
    # --- Cambio de tipo de datos ---
    filtro_periodo[["grupo", "codigo", "nombre", "periodo"]] = (
        filtro_periodo[["grupo", "codigo", "nombre", "periodo"]].astype(str)
    )

    filtro_periodo["puesto"] = pd.to_numeric(filtro_periodo["puesto"], errors="coerce").astype("Int64")

    cols_numericas = [
        "promedio",
        "ciencias_naturales",
        "fisica",
        "quimica",
        "ciencias_politicas_economicas",
        "ciencias_sociales",
        "civica_y_constitucion",
        "educacion_artistica",
        "educacion_cristiana",
        "educacion_etica",
        "educacion_fisica",
        "filosofia",
        "idioma_extranjero",
        "lengua_castellana",
        "matematicas",
        "tecnologia"
    ]

    for col in cols_numericas:
        filtro_periodo[col] = (
            filtro_periodo[col]
            .astype(str)
            .str.replace(",", ".", regex=False)
            .astype(float)
        )

    # --- Diccionario de reemplazos ---
    reemplazos = {
        "ONCE": "11.",
        "DECIMO": "10.",
        "NOVENO": "9.",
        "OCTAVO": "8.",
        "SEPTIMO": "7.",
        "SEXTO": "6.",
        "QUINTO": "5.",
        "CUARTO": "4.",
        "TERCERO": "3.",
        "SEGUNDO": "2.",
        "PRIMERO": "1."
    }

    for palabra, numero in reemplazos.items(): 
        filtro_periodo['grupo'] = filtro_periodo['grupo'].str.replace(palabra, numero, regex=False)

    # --- Reorganizar columnas ---
    orden_columnas = [
        "grupo", "codigo", "nombre", "periodo", "puesto", "promedio",
        "ciencias_naturales", "fisica", "quimica", "ciencias_politicas_economicas",
        "ciencias_sociales", "civica_y_constitucion", "educacion_artistica",
        "educacion_cristiana", "educacion_etica", "educacion_fisica", "filosofia",
        "idioma_extranjero", "lengua_castellana", "matematicas", "tecnologia"
    ]
    filtro_periodo = filtro_periodo[orden_columnas]
    
 
    
     # --- Adicionar columnas vacías (observaciones, metas, rep_eva) ---
    columnas_adicionales = [
        "observaciones_ciencias_naturales","observaciones_fisica","observaciones_quimica",
        "observaciones_ciencias_politicas_economicas","observaciones_ciencias_sociales",
        "observaciones_civica_y_constitucion","observaciones_educacion_artistica",
        "observaciones_educacion_cristiana","observaciones_educacion_etica",
        "observaciones_educacion_fisica","observaciones_filosofia","observaciones_idioma_extranjero",
        "observaciones_lengua_castellana","observaciones_matematicas","observaciones_tecnologia",
        "metas_ciencias_naturales","metas_fisica","metas_quimica","metas_ciencias_politicas_economicas",
        "metas_ciencias_sociales","metas_civica_y_constitucion","metas_educacion_artistica",
        "metas_educacion_cristiana","metas_educacion_etica","metas_educacion_fisica",
        "metas_filosofia","metas_idioma_extranjero","metas_lengua_castellana",
        "metas_matematicas","metas_tecnologia",
        "rep_eva_ciencias_naturales","rep_eva_fisica","rep_eva_quimica",
        "rep_eva_ciencias_politicas_economicas","rep_eva_ciencias_sociales",
        "rep_eva_civica_y_constitucion","rep_eva_educacion_artistica","rep_eva_educacion_cristiana",
        "rep_eva_educacion_etica","rep_eva_educacion_fisica","rep_eva_filosofia",
        "rep_eva_idioma_extranjero","rep_eva_lengua_castellana","rep_eva_matematicas","rep_eva_tecnologia"
    ]
    for col in columnas_adicionales:
        filtro_periodo[col] = "..."   
    
    
    return filtro_periodo.reset_index(drop=True)
    # print(filtro_periodo.info())
    # print(filtro_periodo.reset_index(drop=True))
