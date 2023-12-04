
from sklearn.datasets_selection import fetch_openmL
from sklearn.datasets_selection import train_test_split


df_boston = fetch_openml(name="boston", as_frame=True)['frame']

print(df_boston)