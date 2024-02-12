# Penguin Species Predictor
Develop a simple machine learning approach to predict the species of a penguin from measurements of different physical characteristics. 

## Data Source
**Gorman KB, Williams TD, Fraser WR** (2014) Ecological Sexual Dimorphism and Environmental Variability within a Community of Antarctic Penguins (Genus Pygoscelis). PLoS ONE 9(3): e90081. doi:10.1371/journal.pone.0090081

## Project Structure

```
.
├── README.md                             # Project overview
├── code:                                 # Analysis, by step, in Jupyter Notebooks
│   ├── 01_data_cleaning.ipynb
│   ├── 02_data_visualization.ipynb
│   └── 03_machine_learning.ipynb
├── data:                                 # Data files for project
│   ├── cleaned                           ## Data cleaned for analysis
│   │   ├── penguins_cleaned.csv
│   │   └── penguins_size.csv
│   └── raw                               ## Original, unprocessed data
│       └── penguins_lter.csv
└── output:                               # Project results
    ├── figures                           ## Figures
    │   ├── body_mass_boxplot.png
    │   └── flipper_to_mass_scatter.png
    ├── manuscript                        ## Manuscript in development
    └── reports                           ## Short reports for communicating interim results
        ├── 01_data_cleaning.html
        ├── 02_data_visualization.html
        └── 03_machine_learning.html
```