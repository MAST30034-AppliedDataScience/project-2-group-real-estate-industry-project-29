# Real Estate Consulting(Victoria Rental Property Analysis)

## Group Introduction(Group 29):
Yuzheng Mu
Tianlu Du
Weicheng Guo

## Project Overview

This project aims to analyze the rental property market in Victoria, Australia, to address the following three key questions:

1. **What are the most important internal and external features in predicting rental prices?**
2. **What are the top 10 suburbs with the highest predicted growth rate?**
3. **According to your chosen metrics, which suburbs are the most livable and affordable?**

By collecting and analyzing various datasets—including property listings, population projections, income data, and geographical data on schools and train stations—we built predictive models and conducted spatial analyses to answer these questions.

## Table of Contents

- [Project Overview]
- [Data Preparation]
- [Model Building]
- [Results]
- [Conclusion]
- [Acknowledgments]
- [License]

## Data Sources

The project utilizes the following datasets:

- **Rental Property Data**: Scraped from real estate websites, including rental prices, property features (bedrooms, bathrooms, parking spaces), and locations (latitude and longitude).
- **Population Projection Data**: Population forecasts by Statistical Area Level 2 (SA2) from the Australian Bureau of Statistics (ABS).
- **Income Data**: Median and average incomes for each SA2 from 2016-17 to 2020-21.
- **School Location Data**: Geographical information of schools in Victoria.
- **Train Station Data**: Locations and annual patronage data of train stations.
- **SA2 Shapefiles**: Geographical boundaries of SA2 regions for spatial analysis.

## Data Preparation

### 1. Data Collection

- **Scraping Rental Property Data**: Collected current rental listings in Victoria using web scraping techniques, capturing property features and locations.
- **Downloading Public Datasets**: Obtained population, income, schools, and train station data from the ABS and other public sources.

### 2. Data Cleaning

- **Handling Missing Values**: Checked for missing data and applied appropriate cleaning methods.
- **Data Type Conversion**: Ensured numerical fields were correctly formatted for analysis.

### 3. Geographical Data Processing

- **Coordinate Reference System (CRS)**: Standardized all spatial data to a common CRS (EPSG:3857) to ensure consistency in spatial operations.
- **Spatial Joins**: Mapped properties to their corresponding SA2 regions based on geographical coordinates.

## Feature Engineering

- **Distance to Nearest Train Station**: Calculated using spatial indexing and nearest-neighbor search.
- **Number of Nearby Schools**: Counted the number of schools within a 2 km radius of each property.
- **Population Growth Rate**: Computed the projected population growth rate for each SA2 between 2022 and 2025.
- **Income Metrics**: Calculated the average median income for each SA2 region.
- **Rent-to-Income Ratio**: Determined affordability by calculating the ratio of annual rent to average median income.

## Model Building

Multiple machine learning models were trained and evaluated to predict rental prices:

- **Linear Regression**
- **Random Forest Regressor**
- **Gradient Boosting Regressor**
- **XGBoost Regressor**
- **Support Vector Regressor**

### Model Evaluation

Models were assessed based on Root Mean Squared Error (RMSE) and R² score.

**Model Performance Comparison:**

| Model | RMSE | R² Score |
| --- | --- | --- |
| Linear Regression | 281.25 | 0.2635 |
| Random Forest Regressor | 204.36 | 0.6112 |
| Gradient Boosting Regressor | 220.06 | 0.5491 |
| XGBoost Regressor | 192.59 | 0.6547 |
| Support Vector Regressor | 327.02 | 0.0044 |

**Selected Model**: Based on RMSE and R² scores, the **XGBoost Regressor** was chosen as the best-performing model.

### Feature Importance

The feature importance analysis from the XGBoost model identified the key predictors affecting rental prices:

1. **Number of Bedrooms (bed)**
2. **Number of Bathrooms (bath)**
3. **Distance to Nearest Train Station (distance_to_station)**
4. **Number of Schools within 2 km (schools_within_2km)**
5. **Number of Parking Spaces (parking)**
6. **Region (region)**

## Results

### Question 1: Most Important Features in Predicting Rental Prices

- **Internal Features**:
    - Number of Bedrooms
    - Number of Bathrooms
    - Number of Parking Spaces
- **External Features**:
    - Distance to Nearest Train Station
    - Number of Nearby Schools
    - Region

### Question 2: Top 10 Suburbs with Highest Predicted Growth Rate

Based on population projection data, we identified the top 10 SA2 regions in Victoria with the highest predicted population growth rate between 2022 and 2025. *(Specific suburbs are listed based on the analysis results.)*

### Question 3: Most Livable and Affordable Suburbs

We calculated livability and affordability scores for each SA2 region:

- **Livability Score**: Based on factors such as distance to train stations and the number of nearby schools.
- **Affordability Score**: Based on the rent-to-income ratio.

By combining these scores, we identified the suburbs that offer the best balance of livability and affordability. *(Specific suburbs are listed based on the analysis results.)*

## Conclusion

The project successfully analyzed the rental property market in Victoria, addressing the key questions regarding rental prices, growth rates, and suburb livability and affordability.

- **Key Findings**:
    - Both internal and external features significantly impact rental prices.
    - Certain suburbs are projected to experience higher growth rates.
    - There is a balance to be found between livability and affordability in specific regions.

## Acknowledgments

- **Australian Bureau of Statistics (ABS)**: For providing population and income data.
- **Victoria State Government Data Portal**: For school and train station data.
- **OpenStreetMap**: For geographical data.
- **Various Python Libraries**: Tools used for data analysis and modeling.

## License

This project is licensed under the MIT License.