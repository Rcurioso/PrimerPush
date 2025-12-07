# Script para analizar abandono de clientes
# Todo por desarroyar

df['segmento_valor'] = pd.qcut(df['valor'], 3, labels=['bajo', 'medio', 'alto'])