import pandas as pd
import csv
import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt
 
 
df1 = pd.read_csv("MortalityData.csv")
df2 = pd.read_csv("DataSci.csv")
 
df_2019 = df2[df2['year'] == 2019]
df_2020 = df2[df2['year'] == 2020]
df_19_20 = pd.concat([df_2019, df_2020]) #combined data frame of 2019 and 2020 to use on bar graph that compares the life ladder between those 2 years
 
# print(df_19_20.head())
 
print(df_2019["Life Ladder"].mean())
print(df_2020["Life Ladder"].mean())
 
#Code for comparing the life ladder between 2019 and 2020
# fig, axes = plt.subplots(nrows=1, ncols=1,constrained_layout=True,figsize=(10,4))
# sns.barplot(x='year' ,y='Life Ladder',data=df_19_20,palette='Wistia')
# plt.show()
 
#Played around with variables and axes in the code below to get the various bar graphs.
 
# fig, axes = plt.subplots(nrows=1, ncols=1,constrained_layout=True,figsize=(10,4))
# sns.barplot(x='Life Ladder' ,y='Country name',data=df_2020.nlargest(10,'Life Ladder'),palette='Wistia')
# plt.xlabel('Happiest Countries 2020')
# plt.ylabel('Country Name')
# plt.show()
 
# fig, axes = plt.subplots(nrows=2, ncols=2,constrained_layout=True,figsize=(12,8))
# sns.barplot(x='Log GDP per capita',y='Country name',data=df_2020.nsmallest(10,'Log GDP per capita'),ax=axes[0,0],palette="Blues_d")
# sns.barplot(x='Social support' ,y='Country name',data=df_2020.nsmallest(10,'Social support'),ax=axes[0,1],palette="YlGn")
# sns.barplot(x='Healthy life expectancy at birth' ,y='Country name',data=df_2020.nsmallest(10,'Healthy life expectancy at birth'),ax=axes[1,0],palette='OrRd')
# sns.barplot(x='Freedom to make life choices' ,y='Country name',data=df_2020.nsmallest(10,'Freedom to make life choices'),ax=axes[1,1],palette='YlOrBr')
# plt.show()

# df1 = pd.read_csv("MortalityData.csv")
# df2 = pd.read_csv("DataSci.csv")

###Individual Countries###
# filter by a country
country_df = df2.loc[df2['Country name'] == 'Kenya']

# print(final_df)
country_df.plot('year', 'Healthy life expectancy at birth', color="Red")
plt.xlabel('Year')
plt.ylabel("Healthy Life Expectancy at Birth")
plt.title("Kenya Healthy Life Expectancy at Birth")
plt.savefig("Kenya Healthy Life Expectancy at Birth")



###Comparing covid deaths to various factors###

df_2019 = df2[df2['year']==2019]
df_2020 = df2[df2['year']==2020]

# which should be x and which should be y?
sns.lmplot(x ="Index of institutional trust", y ="COVID-19 deaths per 100,000 population in 2020", data = df1, order = 1, ci = None)

plt.savefig("COVIDindex_graph.png")

# merged dfs
# to compare covid data to 2020 happiness
df3 = pd.merge(df1, df_2020, how = 'inner')

sns.lmplot(x ="COVID-19 deaths per 100,000 population in 2020", y = "Index of institutional trust", data = df3, order = 1, ci = 95)

plt.savefig("COVIDindex_graph.png")

sns.lmplot(x ="COVID-19 deaths per 100,000 population in 2020", y = "Social support", data = df3, order = 1, ci = 95)

plt.savefig("COVIDvs_social.png")

sns.lmplot(x ="COVID-19 deaths per 100,000 population in 2020", y = "Log GDP per capita", data = df3, order = 1, ci = 95)

plt.savefig("COVIDvs_gdp.png")

sns.lmplot(x ="COVID-19 deaths per 100,000 population in 2020", y = "Freedom to make life choices", data = df3, order = 1, ci = 95)

plt.savefig("COVIDvs_free.png")

sns.lmplot(x ="COVID-19 deaths per 100,000 population in 2020", y = "Freedom to make life choices", data = df3, order = 1, ci = 95)

plt.savefig("COVIDvs_free.png")

plt.savefig("COVIDindex_graph.png")

plt.savefig("COVIDvs_free.png")




