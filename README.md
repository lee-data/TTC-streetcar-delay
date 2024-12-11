# TTC Streetcar Delay Prediction - A Data Science Approach

# **VIDEO**

Click on the image to play the video.

[![TTC Streetcar Delay - A Data Science Approach](https://github.com/lee-data/TTC-streetcar-delay/blob/release/src/visualization/Thumnail.jpg)](https://www.youtube.com/watch?v=US7fKLYEJQg)


## INTRODUCTION 

Delays in public transit can disrupt daily routines and impact customer satisfaction. To address this, we analyzed TTC streetcar delay data from January 2023 to September 2024, applying machine learning techniques to predict delay types and provide actionable insights.

Our goal is to classify TTC streetcar delays into short, normal, or long delay categories to better understand delay patterns and help optimize operations. Predictors used for the calculations include:

-	Day of week
-	Holiday 
-   Season
-	Time of day
-	Line
-	Location
-	Bound
-	Vehicle
-	Incident type


## CHALLENGES

![Challenges](<https://github.com/lee-data/TTC-streetcar-delay/blob/release/src/visualization/READ%20ME%20-%20Challenges.png>)  

However, challenges such as measurement error and recall bias were observed. Exploratory data analysis revealed significant clusters at exact 10-minute intervals with dips in the minutes between, suggesting potential recall bias. Additionally, significant outliers were observed beyond the 1-hour delay mark, extending up to 15 hours.


## DATA PREPROCESSING  

We worked with about 4,400 one-hot encoded features derived from delay records. Data pre-processing involved the removal of null and missing values, as well as stratified sampling, class weight balancing, and dimensionality reduction. This included utilizing the feature importance algorithm derived from random forest, applying principal component analysis (PCA), and testing uniform manifold approximation and projection (UMAP).


## PREDICTIVE MODELS

![PREDICTIVE MODELS](https://github.com/lee-data/TTC-streetcar-delay/blob/release/src/visualization/README%20-%20Predictive%20models.png)

We explored seven predictive models optimizing for balanced accuracy. The random forest classifier, XG boost classifier, and neural network were applied to various transformed data sets. The ensemble bagging method with PCA emerged as the top performer, while other models were more effective at identifying the majority class but struggled to detect the minority classes.


## PROTOTYPE

To make our findings actionable, we developed an interactive web application hosted on Render, allowing users to predict delay types based on selected features. 
Click on the image to access our interactive web application. 

[![PROTOTYPE](https://github.com/lee-data/TTC-streetcar-delay/blob/release/src/visualization/Prototype.png)](https://ttc-app.eltaydigital.com)




## INSIGHTS

![INSIGHTS](https://github.com/lee-data/TTC-streetcar-delay/blob/release/src/visualization/README%20-%20Insights.png)

Here are key insights from our data analysis highlighting critical patterns and trends in streetcar delays.

-   Top 10 features importance: Incident-related features like diversion and mechanical issues are the most influential in predicting delay types, along with key routes such as lines 512 and 506.

-	Top 10 incidents: Diversions lead delay causes with 931 hours annually, followed by operational incidents, underscoring areas for improvement.
-	Line and line type: The Queen line sees the highest delays, while regular service lines account for 94% of total delay hours, making them a priority for optimization.
-	Delay hotspots: King and Church and Dundas West station are the top delay hotspots.
-	Time of day: Off-peak hours accumulate to the most delay hours at 1,820 hours annually.
-	Critical lines: Lines like 501, 504, 505, and 506 appear frequently, confirming their critical role in addressing delays.


## RECOMMENDATIONS

Key recommendations include:
-	Addressing measurement errors and recall bias.
-	Prioritizing the dominant features contributing most to delays.
-	Leveraging these predictions for continuous improvements in operational efficiency.


## PROJECT TEAM 

![PROJECT TEAM](https://github.com/lee-data/TTC-streetcar-delay/blob/release/src/visualization/README%20-%20Project%20team.png)

Meet the team behind this project:
-	**[Jay Menorca](https://www.linkedin.com/in/jay-menorca/)**: Expert in GitHub, extract load transform, and DevOps. LinkedIn: https://www.linkedin.com/in/jay-menorca/ 
-	**Ly Nguyen**: Delivering data pre-processing, exploratory analysis, machine learning models, visualization insights, and app development.
-	**XiaoXiao Gong**: Contributing to descriptive analytics, visualization, and actionable insights.
-	**Shruti Patil**: Specializing in interactive dashboards with Tableau.

Video Editing: Ly Nguyen

Together, we've combined our strengths to create a valuable outcome for this project.



---
**Acknowledgement**: This project has been made possible thanks to the open data initiative of Toronto Transit Commission (TTC) and the support of The University of Toronto - Data Sciences Institute.
