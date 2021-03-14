import pandas as pd
from matplotlib import pyplot as plt
import seaborn as sns

df = pd.read_csv("Pokemon.csv", encoding='latin1', index_col=0)
print(df.head())    #first 5 results

#Seaborn for plotiing
sns.lmplot(x = "Attack", y = "Defense", data = df,
            fit_reg = False, #Removes the regression line
            hue = "Stage")  #Color by evolution stage

#Tweaking using matplotlib
plt.ylim(0, None)
plt.xlim(0, None)

# plt.show()  #output

#Boxplot view
sns.boxplot(data = df)

#Removing unrequired columns
stats_df = df.drop(["Total", "Stage", "Legendary"], axis = 1)

#New boxplot after dropping above columns
sns.boxplot(data = stats_df)

# plt.show()

#Whitegrid theme with Violin plot to show the distribution (through the thickness of the violin) 
# instead of only the summary statistics
sns.set_style("whitegrid")
sns.violinplot(x= "Type 1", y = "Attack", data = df)

# plt.show()

#setting individualized colors for respective plots
pkmn_type_colors = ['#78C850',  # Grass
                    '#F08030',  # Fire
                    '#6890F0',  # Water
                    '#A8B820',  # Bug
                    '#A8A878',  # Normal
                    '#A040A0',  # Poison
                    '#F8D030',  # Electric
                    '#E0C068',  # Ground
                    '#EE99AC',  # Fairy
                    '#C03028',  # Fighting
                    '#F85888',  # Psychic
                    '#B8A038',  # Rock
                    '#705898',  # Ghost
                    '#98D8D8',  # Ice
                    '#7038F8',  # Dragon
                   ]

# Violin plot with Pokemon color palette
sns.violinplot(x='Type 1', y='Attack', data=df, 
               palette=pkmn_type_colors) # Set color palette

# plt.show()

#Displaying the Swarm plots
sns.swarmplot(x='Type 1', y='Attack', data=df, 
               palette=pkmn_type_colors)

# plt.show()

#Overlaying plots
# Set figure size with matplotlib
plt.figure(figsize=(10,6))
 
# Create plot
sns.violinplot(x='Type 1',
               y='Attack', 
               data=df, 
               inner=None, # Remove the bars inside the violins
               palette=pkmn_type_colors)
 
sns.swarmplot(x='Type 1', 
              y='Attack', 
              data=df, 
              color='k', # Make points black
              alpha=0.7) # and slightly transparent
 
# Set title with matplotlib
plt.title('Attack by Type')

# plt.show()

# Melt DataFrame
melted_df = pd.melt(stats_df, 
                    id_vars=["Name", "Type 1", "Type 2"], # Variables to keep
                    var_name="Stat") # Name of melted variable
melted_df.head()
#All 6 of the stat columns have been "melted" into one, and the new Stat column indicates the 
# original stat (HP, Attack, Defense, Sp. Attack, Sp. Defense, or Speed). For example, it's hard to see here, 
# but Bulbasaur now has 6 rows of data.

# Swarmplot with melted_df
sns.swarmplot(x='Stat', y='value', data=melted_df, 
              hue='Type 1')

#Making it more readable
# 1. Enlarge the plot
plt.figure(figsize=(10,6))
 
# plt.show()

sns.swarmplot(x='Stat', 
              y='value', 
              data=melted_df, 
              hue='Type 1', 
              split=True, # 2. Separate points by hue
              palette=pkmn_type_colors) # 3. Use Pokemon palette
 
# 4. Adjust the y-axis
plt.ylim(0, 260)
 
# plt.show()

# 5. Place legend to the right
plt.legend(bbox_to_anchor=(1, 1), loc=2)

# plt.show()

#More data visualization techniques
#1. Heatmap - to visualize data in a matrix form
corr = stats_df.corr()
sns.heatmap(corr)

# plt.show()

#2. Histogram - for distribution of numeric variables
sns.displot(df.Attack)

# plt.show()

#3. Bar Plot - to visualize the distribution of categorical values
# Count Plot (a.k.a. Bar Plot)
sns.countplot(x='Type 1', data=df, palette=pkmn_type_colors)
 
# Rotate x-labels
plt.xticks(rotation=-45)

# plt.show()

#4. Factor Plot - to separate plots with categorical values
g = sns.factorplot(x='Type 1', 
                   y='Attack', 
                   data=df, 
                   hue='Stage',  # Color by stage
                   col='Stage',  # Separate by stage
                   kind='swarm') # Swarmplot
 
# Rotate x-axis labels
g.set_xticklabels(rotation=-45)
 
# Doesn't work because only rotates last plot
# plt.xticks(rotation=-45)

# plt.show()

#5. Density Plot - To display the distribution between 2 variables [TIP- consider overlaying this with a scatter plot]
sns.kdeplot(df.Attack, df.Defense)

# plt.show()

#6. Joint Distribution plot - Joint distribution plots combine information from scatter plots and histograms 
# to give you detailed information for bi-variate distributions.
sns.jointplot(x='Attack', y='Defense', data=df)

plt.show()


