import pandas as pd
from pathlib import Path
BRENT_DAILY_FILEPATH = Path(__file__).parent.joinpath( 'data','brent-daily.csv')
GAS_DAILY_FILEPATH = Path(__file__).parent.joinpath('data','gas-daily.csv')
BRENT_MONTH_FILEPATH = Path(__file__).parent.joinpath('data','brent-month.csv')
GAS_MONTHLY_FILEPATH = Path(__file__).parent.joinpath( 'data','gas-monthly.csv')
WTI_DAILY_FILEPATH = Path(__file__).parent.joinpath( 'data','wti-daily.csv')
WTI_MONTHLY_FILEPATH = Path(__file__).parent.joinpath( 'data','wti-month.csv')


cols = ['Date', 'Price']
df_brent_daily = pd.read_csv(BRENT_DAILY_FILEPATH, usecols=cols)
df_wti_daily = pd.read_csv(WTI_DAILY_FILEPATH, usecols=cols)
df_gas_daily = pd.read_csv(GAS_DAILY_FILEPATH, usecols=cols)
df_gas_monthly = pd.read_csv(GAS_MONTHLY_FILEPATH, usecols=cols)
df_wti_monthly = pd.read_csv(WTI_MONTHLY_FILEPATH, usecols=cols)
df_brent_monthly = pd.read_csv(BRENT_MONTH_FILEPATH, usecols=cols)

df_brent_daily.insert(0, 'type', 'brent')

df_brent_daily.to_csv(BRENT_DAILY_FILEPATH, index=False)



df_gas_daily.insert(0, 'type', 'gas')

df_gas_daily.to_csv(GAS_DAILY_FILEPATH, index=False)



df_wti_daily.insert(0, 'type', 'wti')

df_wti_daily.to_csv(WTI_DAILY_FILEPATH, index=False)



df_list_d = [df_brent_daily, df_gas_daily, df_wti_daily]

df_merged_d = pd.concat(df_list_d, axis=0)

df_merged_d.to_csv('daily_file.csv', index=False)



df_brent_monthly.insert(0, 'type', 'brent')

df_brent_monthly.to_csv(BRENT_MONTH_FILEPATH, index=False)



df_gas_monthly.insert(0, 'type', 'gas')

df_gas_monthly.to_csv(GAS_MONTHLY_FILEPATH, index=False)



df_wti_monthly.insert(0, 'type', 'wti')

df_wti_monthly.to_csv(WTI_MONTHLY_FILEPATH, index=False)


df_list_m = [df_brent_monthly, df_gas_monthly, df_wti_monthly]

df_merged_m = pd.concat(df_list_m, axis=0)

df_merged_m.to_csv('monthly_file.csv', index=False)