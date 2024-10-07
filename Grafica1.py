import pandas as pd
import matplotlib.pyplot as ptl

# Asegúrate de usar la ruta correcta
dcu = pd.read_csv(r'C://Users//salex//Downloads//archive//Marvel Vs DC NEW.csv')

# Filtramos las diez películas con las puntuaciones más altas
MarvelvsDC = dcu[['Movie', 'IMDB_Score', 'Description']].sort_values('IMDB_Score', ascending=False).head(10)

# Configuración de la figura
ptl.figure(figsize=(8, 6))

# Gráfica de barras
ptl.plot(MarvelvsDC['Movie'], MarvelvsDC['IMDB_Score'], color='blue')

# Ajustamos las etiquetas en el eje X
ptl.xticks(rotation=45, ha='right')
ptl.xlabel('Movies')
ptl.ylabel('IMDB Score')
ptl.title('Películas de Marvel vs DC')
ptl.tight_layout()
ptl.show()
