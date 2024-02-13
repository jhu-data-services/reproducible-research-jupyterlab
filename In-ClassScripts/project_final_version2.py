# Some code to predict penguins species
#Gorman KB, Williams TD, Fraser WR (2014) Ecological Sexual Dimorphism and Environmental Variability within a Community of Antarctic Penguins (Genus Pygoscelis). PLoS ONE 9(3): e90081. https://doi.org/10.1371/journal.pone.0090081
import pandas as pd
raw_penguins_df = pd.read_csv("../data/raw/penguins_lter.csv")
variables_to_keep = ["Species", 
                     "Island", 
                     "Flipper Length (mm)",
                     "Culmen Length (mm)",
                     "Culmen Depth (mm)",
                     "Body Mass (g)", 
                     "Sex"]
penguins_df = raw_penguins_df[variables_to_keep]
penguins_df.head
#Rename species from scientific name to common name, for example Adelie Penguin (Pygoscelis adeliae) is renamed to Adelie.
penguins_df.rename(columns = {'Species':'species', 
                              'Island':'island', 
                              'Flipper Length (mm)':'flipper_length_mm',
                              'Culmen Length (mm)':'bill_length_mm',
                              'Culmen Depth (mm)':'bill_depth_mm',
                              'Body Mass (g)':'body_mass_g',
                              'Sex':'sex'},inplace=True)
penguins_df.head()
species = penguins_df.species.unique().tolist()
species_common = ["Adelie",
                 "Chinstrap",
                 "Gentoo"]
penguins_df.loc[:,'species'] = penguins_df.loc[:,'species'].replace(species, species_common)
penguins_df.head()
penguins_df.to_csv('../data/cleaned/penguins_cleaned.csv', index=False)
penguins = pd.read_csv("../data/cleaned/penguins_cleaned.csv")
penguins.head()
%matplotlib inline
import seaborn as sns
import matplotlib.pyplot as plt
sns.set_style('whitegrid')
g = sns.boxplot(x = 'island',
            y ='body_mass_g',
            hue = 'species',
            data = penguins,
            palette=['#FF8C00','#159090','#A034F0'],
            linewidth=0.3)
g.set_xlabel('Island')
g.set_ylabel('Body Mass')
plt.savefig("../output/figures/body_mass_boxplot.png")
g = sns.lmplot(x="flipper_length_mm",
               y="body_mass_g",
               hue="species",
               height=7,
               data=penguins,
               palette=['#FF8C00','#159090','#A034F0'])
g.set_xlabels('Flipper Length')
g.set_ylabels('Body Mass')
plt.savefig("../output/figures/flipper_to_mass_scatter.png")
import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.pipeline import FeatureUnion, make_pipeline
from sklearn.metrics import confusion_matrix
### To deal with missing values
from sklearn.experimental import enable_iterative_imputer
from sklearn.impute import IterativeImputer
from sklearn.tree import DecisionTreeClassifier
# Load penguins cleaned data
penguins = pd.read_csv("../data/cleaned/penguins_cleaned.csv")
penguins.head()
# Split data into features and labels
X = penguins.loc[:,["bill_length_mm", "flipper_length_mm", "body_mass_g"]]
y = penguins.loc[:,["species"]]

# Create training/testing split
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=100,
                                            random_state=0)
imp = IterativeImputer(max_iter=10, random_state=0)
clf = make_pipeline(imp, DecisionTreeClassifier())
clf = clf.fit(X_train, y_train)

# Test the trained model using test set
y_pred = clf.predict(X_test)