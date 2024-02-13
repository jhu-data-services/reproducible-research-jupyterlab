# JupyterLab for Reproducible Research
The JupyterLab half of a 1-hour session for Love Data Week 2024, which will overview Quarto and JupyterLab, two popular tools for integrating code, documentation, and text into reproducible research projects. This workshop will teach you the basics of using Quarto and Jupyter Notebooks to improve the legibility of your code in R, Python, or other programming languages, focusing on features that help you create reproducible research and code for technical and non-technical audiences.

## JHU Data Services   
Website: [dataservices.library.jhu.edu/](https://dataservices.library.jhu.edu/)   
Contact us: [dataservices@jhu.edu](mailto:dataservices@jhu.edu)   
JHU Data Services, part of the Johns Hopkins University Sheridan Libraries, helps the JHU community find, use, visualize, manage, and share data. We offer live webinars and self-paced online trainings on computational research and coding, GIS, data management, data visualization, and more. [See all of our training topics on our website.](https://dataservices.library.jhu.edu/training-workshops/)   

This repository contains materials for one of our live webinars open to JHU students, faculty, and staff. Please [contact us](mailto:dataservices@jhu.edu) with any questions.

As of March 2020, Data Services workshops are being held virtually on Zoom. [See our calendar to register for upcoming workshops.](https://dataservices.library.jhu.edu/training-workshops/calendar/)


## JupyterLab Installation

### Installing with Anaconda Python

The easiest way to install **JupyterLab**, and the preferred if you don't have Python installed already, is using Anaconda Python: https://www.anaconda.com/download. Anaconda Python is a "batteries included" version of Python with JupyterLab and common packages already installed. This is the fastest and easiest way to get started with JupyterLab and Python.

### Installing manually with `conda`.

If you already have the **Conda** pacakge manager installed (which is installed with the Anaconda or Miniconda Python installer), you can use `conda install -c conda-forge jupyterlab` to install JupyterLab.

### Installing with `pip`
If you would prefer to use Python's default package manager **pip**, use `pip install jupyterlab` to install JupyterLab.


## Using JupyterLab

### Command Palette

All user actions in JupyterLab can be accessed with the **Command Palette**. 

To access Command Palette:
- Windows/Linux: `Ctrl Shift C`
- Mac: `Command Shift C`


### Keyboard Shortcuts

A list of all the JupyterLab commands and  corresponding keyboard shortcuts are available: https://jupyterlab.readthedocs.io/en/latest/user/commands.html

To access a list of common keyboard shortcuts, use the command:
- Windows/Linux: `Ctrl Shift H`
- Mac: `Command Shift H`

## Description of Files
- **In-ClassScripts**: This folder contains code files you will need for the workshop:
    - penguins-species-predictor: An example Python reproducible research project we will be using to demonstrate the reproducible research features of JupyterLab

```
.
└── penguin-species-predictor
    ├── README.md
    ├── code
    │   ├── 01_data_cleaning.ipynb
    │   ├── 02_data_visualization.ipynb
    │   └── 03_machine_learning.ipynb
    ├── data
    │   ├── cleaned
    │   │   ├── penguins_cleaned.csv
    │   │   └── penguins_size.csv
    │   └── raw
    │       └── penguins_lter.csv
    └── output
        ├── figures
        │   ├── body_mass_boxplot.png
        │   └── flipper_to_mass_scatter.png
        ├── manuscript
        └── reports
            ├── 01_data_cleaning.html
            ├── 02_data_visualization.html
            └── 03_machine_learning.html
``` 

- **PresentationMaterials**: This folder contains slides and other presentation materials used in the workshop
- **Resources**: This folder contains cheatsheets to assist you during the workshop and links to external sources for you to continue your learning


## License and Terms of Use
The presentation materials are licensed under a [Creative Commons Attribution-NonCommercial-ShareAlike 4.0 International License (CC BY-NC-SA 4.0)](https://creativecommons.org/licenses/by-nc-sa/4.0/), attributable to [Data Services](https://dataservices.library.jhu.edu/), Johns Hopkins University. 

See LICENSE file for additional code licensing and re-use information.   

The images, external resources, and cheatsheets linked in this repository may have other licenses and terms of use.


## Citation
Please cite this material as:    
Johns Hopkins University Data Services. February 13, 2024. JupyterLab for Reproducible Research. https://github.com/jhu-data-services/reproducible-research-jupyterlab.
