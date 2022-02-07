# Customer-Personality-Analysis
A simple program to perform customer personality analysis.
Author: Siddhant Mahajani

Main program: main.py<br/>
Algorithm: aprioriAlgo.py<br/>
Read and update data: readData.py<br/>
Plot the data using graphs: plotData.py<br/>
Prepare data for analysis: prepareData.py<br/>

Information about the programs:<br/>
1. main.py - This program is the main execution program. The program takes location of the file as input and returns analysis of the customer based on the input provided in apriori algorithm.<br/>
2. aprioriAlgo.py - This is the main algorithm file. The algorithm will provide information about products and the segment you want information about. Currently we have used Fruits and High Consumer.<br/>
3. prepareData.py - This program will help us rename columns, prepare segments, define spending variables and prepare data according to these requirements. We will also be performing clustering to cluster the data according to the Income and Spending.<br/>
4. readData.py - This file will help you read the data from the csv and remove na/null values from the data.<br/>
5. plotData.py - This will help in plotting data in graphical format.<br/>

Output: The output will be written in output.txt file in the customer data folder. The location is provided in the main python program file.

Apriori Algorithm:<br/>
This algorithm refers to an algorithm that is used in mining frequent products sets and relevant association rules. Generally, the apriori algorithm operates on a database containing huge number of transactions. The parameters used are "Support" and "Confidence" are used. Support refers to items' frequency of occurence; confidence is a conditional probability. Items in a transaction from an item set. Example of this algorithm is customers buying a lot of goods from a grocery store, by applying this method of the algorithm the grocery stores can enhance their sales performance and could work effectively.<br/>

Libraries used:<br/>
1. pandas: To read data from csv and load it in the program. The library is also used to manipulate data frames according to the requirement.<br/>
2. For mlxtend.frequent_patterns please install mlxtend: This library is required for apriori algorithm and to perform personality analysis.<br/>
3. For plotly.graph_objects install plotly: This library is required to visualise the data based on the personality analysis.<br/>
4. For dataprep.eda install dataprep: This library is used to plot the figure based on the analysed data.<br/>
5. numpy: This library is used to modify the data according to the requirement i.e. to add columns, to filter data, to rename columns, etc.<br/>
6. For sklearn.preprocessing and sklearn.mixture install sklearn: This library is used to transform and fir the data using StandardScaler and then predict using GaussianMixture.<br/>

To install the libraries use pip install <library_name> i.e. pip install pandas.
