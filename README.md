# Enviromental Analysis of the Greater Los Angeles Area

The goal of this project is to understand the pollution and its impact
on the communities located in the Greater Los Angeles Area. The
dataset used is [CalEnviroScreen
3.0](https://oehha.ca.gov/calenviroscreen/report/calenviroscreen-30)
provided by the [The Office of Environmental Health Hazard Assessment
(OEHHA)](https://oehha.ca.gov/). The CalEnviroScreen aims at
identifying the communities that burdened by pollution.

## Configuration

The project was implemented using Jupyter Notebooks, Python and
libraries used for data analysis such as Pandas and scikit-learn. A
simple way to recreate the development environment is with
[Docker](https://docs.docker.com/), following these steps.

1. Install docker and docker-compose in your computer.

2. Clone the [config-mgmt](https://github.com/aproano2/conf\
ig-mgmt) repository.

3. Go to the `config-mgmt/docker/docker-anaconda3` directory.

4. Run `docker-compose up`.

5. Visit [localhost:8888](http://localhost:8888) in a web browser to
access Jupyter Notebooks.

6. Visit [localhost:5000](http://localhost:5000) in a web browser to
access nbviewer.


## Methodology

In this project, the cross-industry standard process for data mining (CRISP-DM) was used.

### 1. Business Understanding

To guide the project, the following questions were considered:

- What are the main factors that contribute to the pollution burden in Los Angeles?
- What are the less polluted areas in Los Angeles?
- What are the areas with the lowest unemployment?
- Is there a correlation between socioeconomic factors and pollution burden?
- How well can we predict the pollution burden?
- How well can we predict cardiovascular diseases?

### 2. Data Understanding

The data provided by the OEHHA was used to do the exploratory data
analysis presented in the
[ces3la.ipynb](https://github.com/aproano2/la-pollution-burden/blob/master/ces3la.ipynb)
notebook. Both the understanding of the data and the business
understanding were done in the exploration stage. Checking the data
and the correlations helped to get an idea of what questions to
pursue.


### 3. Prepare Data

In the
[helper.py](https://github.com/aproano2/la-pollution-burden/blob/master/helper.py)
file, the `clean_data` and `handle_categorical` functions are
provided. They implement the following functionality:

- Get the data for the Greater Los Angeles Area Column names are
formatted to names without spaces, points and lower case.

- Remove the columns including percentiles since they were not used
for this analysis.

- Remove rows with incorrect ZIP codes.

- Impute numeric missing values.

-Get dummy columns to handle categorical data.


### 4. Data Modeling

The
[helper.py](https://github.com/aproano2/la-pollution-burden/blob/master/helper.py)
file also includes a function that performs linear regression on the
data. It allows the user to use a percentage of the data for training
and the remaining is used to test the accuracy of the model. The
function uses the names of the response columns and the exploratory
columns.

### 5. Evaluate the Results

Results of the analysis and figures are provided in the
[ces3la.ipynb](https://github.com/aproano2/la-pollution-burden/blob/master/ces3la.ipynb)
notebook. These have been collected and described in a blog.

### 6. Deploy

The results have been shared in this [blog post](https://aproano2.github.io/la-pollution-burden).