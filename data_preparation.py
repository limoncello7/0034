import pandas as pd


df_brent = pd.read_csv('brent-daily.csv')

df_brent.insert(0, 'type', 'brent')

df_brent.to_csv('brent-daily.csv', index=False)



df_gas = pd.read_csv('gas-daily.csv')

df_gas.insert(0, 'type', 'gas')

df_gas.to_csv('gas-daily.csv', index=False)



df_wti = pd.read_csv('wti-daily.csv')

df_wti.insert(0, 'type', 'wti')

df_wti.to_csv('wti-daily.csv', index=False)



df_list = [pd.read_csv('brent-daily.csv'), pd.read_csv('gas-daily.csv'), pd.read_csv('wti-daily.csv')]

df_merged = pd.concat(df_list, axis=0)

df_merged.to_csv('merged_file.csv', index=False)