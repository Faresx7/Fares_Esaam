
import pandas as pd 
import numpy as np
import matplotlib.pyplot as plt
import plotly.express as px
import seaborn as sns
from sklearn.preprocessing import MinMaxScaler
from plotly.subplots import make_subplots
import warnings
warnings.filterwarnings('ignore')

 
# ## Reading file
# take a small sample to work on to avoid any performance issues


# data=pd.read_csv('C:/Users/COMPUMARTS/Downloads/repo/Data Analysis project/TWO_CENTURIES_OF_UM_RACES.csv')
# # data.head()
# df = data.sample(frac=0.1, random_state=42)
# df.to_csv("small_file.csv", index=False)
data=pd.read_csv('data analysis project/small_file.csv')


# check null values


# replace spaces in columns with _
data.columns = data.columns.str.replace(' ', '_')
 
# ### Extracting age


# drop all nulls in athlete year of birth
data=data.dropna(subset=['Athlete_year_of_birth'])

 
# ## Problem
# some records have a year of birth bigger than the Year of event
# ### Actions 
# - remove all outliers (make the min age 12 and max 75)
# - if the -year of birth- bigger than -year of event- then replace it or remove it all


# to calculate the age in the race time not current time
data['Age'] = data['Year_of_event'] - data['Athlete_year_of_birth']


 #* fixing problem
condition=data['Athlete_year_of_birth']>data['Year_of_event']
data.loc[condition,['Athlete_year_of_birth','Year_of_event']]=data.loc[condition,['Year_of_event','Athlete_year_of_birth']].values


#calculating age after fixing the problem
data['Age'] = data['Year_of_event'] - data['Athlete_year_of_birth']


#take a look in the new data
data.loc[data['Age'].idxmin(), ['Age', 'Year_of_event', 'Athlete_year_of_birth']]

 
# now set a min and max age


data = data[(data['Age'] >= 12) & (data['Age'] <= 75)]



 
# ## Standardizing gender and distance


'''standardizing the gender
1 for male 0 for female '''
data=data.drop(data[data['Athlete_gender']=='X'].index)
data['Athlete_gender'] = data['Athlete_gender'].replace({'F': 0, 'M': 1})
data['Athlete_gender']=data['Athlete_gender'].astype('int')




 #* multiply mile(mi) distance in 1,6 to be accurate 
data['Event_distance/length'] = np.where(
    data['Event_distance/length'].str.contains('mi', na=False),               
    data['Event_distance/length'].str.extract(r'(\d+)').astype(float)[0] * 1.6, 
    data['Event_distance/length']                                               
)


 #* Reviewing all unique values in data to take the right action for best accuracy

 #* removed all rows contain units another km or mile
data = data[~data['Event_distance/length'].str.contains('h', na=False)]


#* extract only the numeric part from the distance/length column
data['Event_distance/length']=data['Event_distance/length'].str.split(r'[^0-9\.]').str.get(0)


#change data type to float
data['Event_distance/length']=data['Event_distance/length'].astype('float')


# heat map to understand relations between each column
num_cols=data.select_dtypes('number').columns
corr=data[num_cols].corr()
fig_heatmap=px.imshow(corr,text_auto=True,title='Correlation heatmap')
# fig.update_layout(width=700,height=800)

 
# ### **The data we have**
# - we have the normal age based on birth date and event year
# - clean -Age- column only between **--12 and 75--**
# - encoded gender to be **--1 Male--**  , **--0 Female--**
# - removed the units form distance and replaces mile(mi) by it equivalent by kilometer(km)
# ---
# 

 
# ## Splitting data into periods to analysis every period
# 



# global period
p80_22=data[(data['Year_of_event']>=1980) & (data['Year_of_event']<=2022)]
# decades period
p80_90=data[(data['Year_of_event']>=1980) & (data['Year_of_event']<=1990)]
p90_00=data[(data['Year_of_event']>=1990) & (data['Year_of_event']<=2000)]
p00_10=data[(data['Year_of_event']>=2000) & (data['Year_of_event']<=2010)]
p10_20=data[(data['Year_of_event']>=2010) & (data['Year_of_event']<=2020)]

 
# ## Analyzing the mean distances for each decade
# 


# the mean of total distance in every decade
mean_dis_80s=p80_90['Event_distance/length'].mean()
mean_dis_90s=p90_00['Event_distance/length'].mean()
mean_dis_00s=p00_10['Event_distance/length'].mean()
mean_dis_10s=p10_20['Event_distance/length'].mean()


# add them to data frame
decades=['1980s','1990s','2000s','2010s']
means=[mean_dis_80s,mean_dis_90s,mean_dis_00s,mean_dis_10s]
mean_df=pd.DataFrame({'decades':decades,'means':means})


fig_pie=px.pie(names=mean_df['decades'],
       values=mean_df['means'],
       title='<b>Percent of total distance in each decade',
       color=mean_df['decades'],
       color_discrete_map={'1990s':'#576fc7','2000s':'#ffb433','2010s':'#98d8ef'},
       hover_name=mean_df['decades'])



 
# ### Now analyzing based on gender


# getting the mean of males and females in each decade
count_male_80s = p80_90[p80_90['Athlete_gender']==1]['Athlete_gender'].count()
                            #shape will return (rows , columns)count [0] will return rows count
mean_male_80s=(count_male_80s/p80_90.shape[0])*100
mean_female_80s = 100 - mean_male_80s


count_male_90s = p90_00[p90_00['Athlete_gender']==1]['Athlete_gender'].count()
                            #shape will return (rows , columns)count [0] will return rows count
mean_male_90s=(count_male_90s/p90_00.shape[0])*100
mean_female_90s = 100 - mean_male_90s

        
count_male_00s = p00_10[p00_10['Athlete_gender'] == 1]['Athlete_gender'].count()
mean_male_00s=(count_male_00s/p00_10.shape[0])*100
mean_female_00s = 100 - mean_male_00s


count_male_10s = p10_20[p10_20['Athlete_gender'] == 1]['Athlete_gender'].count()
mean_male_10s=(count_male_10s/p10_20.shape[0])*100
mean_female_10s = 100 - mean_male_10s




# add means to data frame for visualization
male_means = [round(mean_male_80s,2),round(mean_male_90s,2), round(mean_male_00s,2), round(mean_male_10s,2)]
female_means = [round(mean_female_80s,2),round(mean_female_90s, 2), round(mean_female_00s,2),round(mean_female_10s,2)]

mean_gender = pd.DataFrame({
    #! decade of each gender
    'Decade': decades * 2,  
    #!gender for each decade
    'Gender': ['Male']*4 + ['Female']*4,
    'Mean': male_means + female_means
})


fig_histogram=px.histogram(mean_gender,
             x='Decade',
             y='Mean',
             color='Gender',
             barmode='group',
             text_auto=True,
             title='<b>Percent of Athletes gender for each decade (Histogram)',
             color_discrete_sequence=px.colors.qualitative.Pastel,
             labels={'Mean':'Percent'}
             
             )
# fig.update_layout(yaxis_title='Mean')


fig_line1 = px.line(
    mean_gender,
    x='Decade',
    y='Mean',
    color='Gender',
    markers=True,
    title='<b>Percent of Athletes genders each decade (Line)'
)
# fig.show()


 
# **Line for each year**


  #! very important
# the data frame for athlete genders for every year
gender_per_year_DF=data[(data['Year_of_event']>=1980)]
gender_count_per_year = gender_per_year_DF.groupby(['Year_of_event', 'Athlete_gender']).size().unstack(fill_value=0).rename(columns={0:'Female_count', 1:'Male_count'}).reset_index()


df_long = gender_count_per_year.melt(id_vars='Year_of_event', 
                                     value_vars=['Male_count', 'Female_count'], 
                                     var_name='Gender', 
                                     value_name='Count')


 #! for each year
fig_line2=px.line(df_long
        ,x='Year_of_event'
        ,y='Count'
        ,color='Gender'
        ,title='<b>Athletes genders every year'
        ,markers=True
                )

 
# **Make Gender count(not mean like the histogram cell 38) Years DataFrame for specific Decade**


gender_count_per_year_80s = p80_90.groupby(['Year_of_event', 'Athlete_gender']).size().unstack(fill_value=0).rename(columns={0:'Female_count', 1:'Male_count'}).reset_index()
gender_count_per_year_90s = p90_00.groupby(['Year_of_event', 'Athlete_gender']).size().unstack(fill_value=0).rename(columns={0:'Female_count', 1:'Male_count'}).reset_index()
gender_count_per_year_00s = p00_10.groupby(['Year_of_event', 'Athlete_gender']).size().unstack(fill_value=0).rename(columns={0:'Female_count', 1:'Male_count'}).reset_index()
gender_count_per_year_10s = p10_20.groupby(['Year_of_event', 'Athlete_gender']).size().unstack(fill_value=0).rename(columns={0:'Female_count', 1:'Male_count'}).reset_index()

df_long_80s = gender_count_per_year_80s.melt(id_vars='Year_of_event',value_vars=['Male_count', 'Female_count'],var_name='Gender',value_name='Count')
df_long_90s = gender_count_per_year_90s.melt(id_vars='Year_of_event',value_vars=['Male_count', 'Female_count'],var_name='Gender',value_name='Count')
df_long_00s = gender_count_per_year_00s.melt(id_vars='Year_of_event',value_vars=['Male_count', 'Female_count'],var_name='Gender',value_name='Count')
df_long_10s = gender_count_per_year_10s.melt(id_vars='Year_of_event',value_vars=['Male_count', 'Female_count'],var_name='Gender',value_name='Count')


 #* Choose any decade to display its analysis 


# the decade can change to display each decade we need
fig_line3=px.line(df_long_00s
        ,x='Year_of_event'
        ,y='Count'
        ,color='Gender'
        ,title='<b>Athletes genders every decade'
        ,markers=True
        )

 
# ## Now analyzing distance for each gender


 #* calculating mean distances for each gender in every period
mean_distance_male_80s=((p80_90[p80_90['Athlete_gender']==1]['Event_distance/length'].sum())/p80_90['Event_distance/length'].sum())*100
mean_distance_male_90s=((p90_00[p90_00['Athlete_gender']==1]['Event_distance/length'].sum())/p90_00['Event_distance/length'].sum())*100
mean_distance_male_00s=((p00_10[p00_10['Athlete_gender']==1]['Event_distance/length'].sum())/p00_10['Event_distance/length'].sum())*100
mean_distance_male_10s=((p10_20[p10_20['Athlete_gender']==1]['Event_distance/length'].sum())/p10_20['Event_distance/length'].sum())*100

mean_distance_female_80s=100-mean_distance_male_80s
mean_distance_female_90s=100-mean_distance_male_90s
mean_distance_female_00s=100-mean_distance_male_00s
mean_distance_female_10s=100-mean_distance_male_10s




males_dis=[round(mean_distance_male_80s,2),round(mean_distance_male_90s,2),round(mean_distance_male_00s,2),round(mean_distance_male_10s,2)]
females_dis=[round(mean_distance_female_80s,2),round(mean_distance_female_90s,2),round(mean_distance_female_00s,2),round(mean_distance_female_10s,2)]

mean_dis=pd.DataFrame({
    'Decades':decades*2,
    'Gender':['male']*4 + ['female']*4,
    'Mean distance':males_dis+females_dis
})


fig_line4=px.line(mean_dis,
        x='Decades',
        y='Mean distance',
        color='Gender',
        markers=True
        )

 
# ## AVG speed


 #! to delete any nonnumeric record from avg speed column
p80_22['Athlete_average_speed'] = pd.to_numeric(p80_22['Athlete_average_speed'], errors='coerce')

#change data type to get mean for every year
p80_22['Athlete_average_speed'] = p80_22['Athlete_average_speed'].astype('float')

 
# ## Problem
# before 1995 the AVG speeds unit is deferent from the AVG speed after 1995
# after some searching I found that before 1995 it was by (meter/hour) and after 1995 it was by (km/hour)
# **solution**
# - multiply the AVG Speeds before 1995 by 0.001


conversion_factor = 0.001
p80_22.loc[p80_22['Year_of_event'] <= 1995, 'Athlete_average_speed'] *= conversion_factor


# Data Frame for year and mean avg speed of it
avg_s_80_22 = p80_22.groupby('Year_of_event')['Athlete_average_speed'].mean().reset_index()

def test():
    fig_line5=px.line(avg_s_80_22
            ,x='Year_of_event'
            ,y='Athlete_average_speed'
            ,title='<b>Average Speed for each year'
            ,labels={
                    'Year_of_event': 'Year',
                    'Athlete_average_speed': 'Average Speeds (km/h)'
                }
            ,markers=True
            ,color_discrete_sequence=["#0077FF"]
            )
    return fig_line5



num_of_finishers80_22=p80_22['Event_number_of_finishers'].sum()


# p80_22.shape


# Data Frame for year and mean avg speed of it
num_of_finishers80_22 = p80_22.groupby('Year_of_event')['Event_number_of_finishers'].sum().reset_index()
# num_of_finishers80_22


fig_line6=px.line(num_of_finishers80_22
        ,x='Year_of_event'
        ,y='Event_number_of_finishers'
        ,markers=True)
