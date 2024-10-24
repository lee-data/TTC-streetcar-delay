# Team 24 - TTC Streetcar Delay

UOfT-DSI Cohort 4 - Team 24's Project Repo 

<h2>Dataset</h2>
TTC Streetcar Delay

<h2>Research Question</h2>
<ul>
  <li>Multivariate Linear Regression: How do external factors like weather conditions or seasonal variations impact incident rates and delays?</li>
  <li>Random Forest Classification: Which features are most likely predictors for which incident?</li> 
</ul>

<h2>Business Case</h2>
<TODO>

Who is the intended audience for our data analysis? 
<TODO>

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
