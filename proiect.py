import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

# --- 1. CITIRE SI PREGATIRE DATE ---
file_name = 'P_Data_Extract_From_World_Development_Indicators (4).xlsx'

# Citim fisierul (convertim automat '..' in lipsa de date)
df = pd.read_excel(file_name, na_values='..')

# Selectam coloanele exacte (cele 5 variabile + Numele Tarii)
cols = ['Health_Exp_GDP', 'Physicians', 'Life_Expectancy', 'Infant_Mortality', 'Pop_65_Plus']
tari = df['Country_Name'].values

# Umplem datele lipsa cu media coloanei
X_df = df[cols].fillna(df[cols].mean())
X = X_df.values

# --- 2. CALCULE MATEMATICE PCA ---

# Standardizare (Z-score)
X_std = (X - np.mean(X, axis=0)) / np.std(X, axis=0)

# Matricea de covarianta si Vectorii proprii
cov_mat = np.cov(X_std.T)
valori, vectori = np.linalg.eig(cov_mat)

# Sortare de la mare la mic
idx = np.argsort(valori)[::-1]
valori = valori[idx]
vectori = vectori[:, idx]

# Varianta explicata (procente)
procente = (valori / np.sum(valori)) * 100
cumulat = np.cumsum(procente)

# Proiectia datelor (Coordonatele pentru grafic)
pca_coords = X_std.dot(vectori[:, :2])

# --- 3. AFISARE REZULTATE IN CONSOLA (TABELE) ---
print("\n--- TABEL 1: VALORI PROPRII ---")
df_valori = pd.DataFrame({
    'Componenta': ['PC1', 'PC2', 'PC3', 'PC4', 'PC5'],
    'Valoare Proprie': valori,
    'Varianta (%)': procente,
    'Cumulat (%)': cumulat
})
print(df_valori.round(4).to_string(index=False))

print("\n--- TABEL 2: MATRICEA COMPONENTELOR ---")
df_vectori = pd.DataFrame(vectori, index=cols, columns=['PC1', 'PC2', 'PC3', 'PC4', 'PC5'])
print(df_vectori[['PC1', 'PC2']].round(4))

# --- 4. GRAFIC 1: SCREE PLOT ---
plt.figure(figsize=(8, 5))
plt.bar(['PC1', 'PC2', 'PC3', 'PC4', 'PC5'], procente, color='blue')
plt.plot(['PC1', 'PC2', 'PC3', 'PC4', 'PC5'], procente,color='red',marker='o',linestyle='-',linewidth=2)
plt.title('Scree Plot')
plt.ylabel('Procent Varianta (%)')
plt.grid(axis='y', alpha=0.3)


# --- 5. GRAFIC 2: HARTA TARILOR ---
plt.figure(figsize=(14, 9))
plt.scatter(pca_coords[:, 0], pca_coords[:, 1], c='gray', alpha=0.6)

# Punem numele tarilor
for i in range(len(tari)):
    nume = str(tari[i]).strip()
    plt.annotate(nume, (pca_coords[i, 0] + 0.1, pca_coords[i, 1]), fontsize=8)



# Desenam sagetile (Vectorii)
scale = 3.5
for i in range(len(cols)):
    x = vectori[i, 0] * scale
    y = vectori[i, 1] * scale
    plt.arrow(0, 0, x, y, color='green', head_width=0.1)
    plt.text(x * 1.1, y * 1.1, cols[i], color='green', weight='bold')

plt.xlabel(f'PC1 - Nivel Dezvoltare ({procente[0]:.1f}%)')
plt.ylabel(f'PC2 - Structura Demografica ({procente[1]:.1f}%)')
plt.title('Harta PCA a Sistemelor de Sanatate')
plt.axhline(0, color='black', linewidth=0.8)
plt.axvline(0, color='black', linewidth=0.8)
plt.grid(alpha=0.3)


plt.show()