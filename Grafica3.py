import pandas as pd
import matplotlib.pyplot as plt

# Cargamos el archivo CSV
PS4gamesales = pd.read_csv(r'C:\Users\salex\Downloads\archive (2)\PS4_GamesSales.csv', encoding='ISO-8859-1')
print(PS4gamesales.head())

# Seleccionamos las columnas relevantes
ps4SALES = PS4gamesales[['Game', 'Genre', 'Publisher', 'Global']].head(10)

# Creamos la figura y el gráfico
plt.figure(figsize=(10, 6))
plt.plot(ps4SALES['Game'], ps4SALES['Global'], marker='s', linestyle='-', color='black')

# Ajustamos las etiquetas del gráfico
plt.xticks(rotation=45, ha='right')
plt.xlabel('Juego')  
plt.ylabel('Ventas Globales (in millions)') 
plt.title("Ventas Globales de Juegos de PS4")  
plt.tight_layout()
plt.show()
