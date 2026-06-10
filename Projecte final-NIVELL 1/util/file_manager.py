"""
Mòdul file_manager.py
Conté la classe CSVFileManager per llegir i escriure fitxers CSV.
"""

from pathlib import Path
import pandas as pd

# dataFrame és una taula de pandas. Per exemple, imaginem aquest CSV de caixers:
# dni,nom,edat,horari,sou
# Quan pandas el llegeix, obgens una DataFrame, que seria com una taula amb les columnes dni, nom, edat, horari i sou, i cada fila corresponent a un caixer diferent.
class CSVFileManager:
    """Gestiona la lectura i escriptura de fitxers CSV."""

    def __init__(self, path: str):
        self.path = Path(path)

    def read(self) -> pd.DataFrame:
        """Llegeix un fitxer CSV i retorna el contingut com a DataFrame."""
        if not self.path.exists():
            raise FileNotFoundError(f"No s'ha trobat el fitxer: {self.path}")
        # Funció de pandas per llegir un fitxer CSV i retornar un DataFrame. 
        # El paràmetre dtype=str indica que pandas ha de llegir totes les columnes com a text (str)
        # evitant problemes de tipus de dades. 
        return pd.read_csv(self.path, dtype=str)

    def write(self, dataFrame: pd.DataFrame) -> None: #indica que aquesta funció no retorna res (None). La seva feina és escriure un fitxer, no retornar dade
        """Escriu un DataFrame en un fitxer CSV."""
        # Aquesta línia crea la carpeta on es guardarà el fitxer, si encara no existeix
        # self.path.parent et porta directament on és el fitxer que es vol lleguir o escriure.
        # mkdir(parents=True, exist_ok=True) crea la carpeta i totes les seves subcarpetes si no existeixen. Si ja existeix, no fa res gràcies a exist_ok=True.
        # parents=True permet crear totes les carpetes necessàries en la ruta, no només la carpeta immediata.
        # exist_ok=True evita que es llanci una excepció si la carpeta ja existeix, permetent que el programa continuï sense problemes.
        self.path.parent.mkdir(parents=True, exist_ok=True) 
        # Funció de pandas per escriure un DataFrame en un fitxer CSV. 
        # El paràmetre index=False indica que no s'ha d'escriure l'índex del DataFrame com una columna extra al fitxer CSV.
        # Per defecte, pandas escriu l'índex del DataFrame com una columna addicional al fitxer CSV. 
        # En establir index=False, s'evita aquesta columna extra i només es guarden les dades reals del DataFrame.
        dataFrame.to_csv(self.path, index=False)
