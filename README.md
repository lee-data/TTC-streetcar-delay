# Team 24 - TTC Streetcar Delay

UOfT-DSI Cohort 4 - Team 24's Github project repository.

<h2>Dataset</h2>
TTC Streetcar Delay

<h2>Research Question</h2>
<ul>
  <li>Random Forest Classification: Which features are most likely predictors for which delay type (fast, expected, long)?</li> 
</ul>

<h2>Business Case</h2>
<ul>
  <li>Case Study: TTC StreetCar Delays - Predictive Modeling </li> 
</ul>

<ul>
  <li>Introduction: Toronto’s streetcar service faces incidents and delays, impacting efficiency and passenger experience. Using machine learning, particularly the Random Forest Classifier, we aim to identify key predictors of these delays.</li> 
</ul>

<ul>
  <li>Objective: Analyze the "TTC Streetcar Delays" dataset, and use machine learning to identify and rank the most significant predictors of delay type, to provide actionable insights.</li> 
</ul>

<ul>
  <li>Scope:

Data Analysis: Apply the Random Forest Classifier to historical delay data of years 2023 and 2024.

Feature Identification: Determine and rank key predictors of delays.

Implementation: Develop models for timely risk assessments and predictive insights.

Outcome Communication: Present findings through clear visualizations and reports.</li> 
</ul>


<ul>
  <li>Expected Benefits:

Operational Efficiency: Target key delay predictors to improve service reliability.

Passenger Satisfaction: Reduce delays to enhance commuting experiences.

Resource Optimization: Optimize maintenance and scheduling.

Data-Driven Decisions: Support ongoing improvements with data insights.</li> 
</ul>

<ul>
  <li>Risk Management:

Data Quality: Ensure accurate data collection and preprocessing.

Model Accuracy: Regularly validate and monitor the predictive model.

Stakeholder Engagement: Keep stakeholders updated and incorporate feedback.</li> 
</ul>

<ul>
  <li>Conclusion: This initiative aims to support TTC’s goal of providing efficient and reliable streetcar services by identifying and addressing the root causes of delays.</li> 
</ul> 


<h2>Reference</h2>
https://open.toronto.ca/dataset/ttc-streetcar-delay-data/

<h2>Members</h2>
<ul>
  <li>Isaias (Jay) Menorca</li>
  <li>Ly (Lee) Nguyen</li>
  <li>Namreen Syed</li>
  <li>Shruti Patel</li>
  <li>Xiaoxiao Gong</li>
</ul>


<h2>Project Notes</h2>
<h3>Data Preparation</h3>
1.) run query file -> streetcar_delay_data_schema.sql
2.) run loadXlsx2DB.py
3.) run cleanupDB.py
4.) run createDateTable.py
5.) run query file -> create_line_table.sql
6.) run query file -> create_delay-table.sql
7.) run loadFrSQLiteDB2DataFrame.py to see sample loading to DataFrame with additional generated column
