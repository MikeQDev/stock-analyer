import pandas as pd
import sys


# TODO:
# not only df_year, but df_5year, etc.
# % difference between mean and latest
# look at latest period - is it peak or valley?

if len(sys.argv) != 2:
  print 'Invalid parameters. Usage: '+str(sys.argv[0])+' dataframe.csv'
  sys.exit(1)

df=pd.read_csv(sys.argv[1]).filter(regex='_Close|Unnamed')
df_year=df[2320:2583]

mean=df_year.mean()
latest=df_year.tail(1).T.drop(['Unnamed: 0']).T.mean()

mean_latest=pd.concat([latest,mean],axis=1)
mean_latest.columns=['year_avg','latest']
mean_latest['cheaper_than_year_avg']=mean<latest

print mean_latest.loc[mean_latest['cheaper_than_year_avg']]
