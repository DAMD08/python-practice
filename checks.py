def contar_nulos(df):
	return df.isna().sum()

def contar_duplicados(df):
	return df.duplicated().sum()