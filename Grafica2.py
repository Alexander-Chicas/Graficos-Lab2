import pandas as pd
import matplotlib.pyplot as plt

# Cargamos el dataset que usaremos en este ejercicio
Spotify = pd.read_csv(r"C:\Users\salex\Downloads\archive (1)\Spotify Most Streamed Songs.csv")
print(Spotify.head())
# Agrupamos por 'track_name' y 'artist(s)_name' y contar las ocurrencias
spotifymost_count = Spotify.groupby(['track_name', 'artist(s)_name']).size().sort_values(ascending=False).head(10)

# Aqui configuramos la gráfica de pastel
plt.figure(figsize=(8, 8))
plt.pie(spotifymost_count, labels=[f"{name[0]} - {name[1]}" for name in spotifymost_count.index], autopct='%1.1f%%', startangle=140,
        colors=['blue', 'Purple', 'Green', 'Gray', 'Pink'])
plt.title('Distribución de las canciones más escuchadas')
plt.tight_layout()
plt.show()
