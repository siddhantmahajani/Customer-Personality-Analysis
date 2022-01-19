# Customer-Personality-Analysis
A simple program to perform customer personality analysis.
Author: Siddhant Mahajani

Main program: main.py
Algorithm: aprioriAlgo.py
Read and update data: readData.py
Plot the data using graphs: plotData.py
Prepare data for analysis: prepareData.py

Information about the programs:
main.py - This program is the main execution program. The program takes location of the file as input and returns analysis of the customer based on the input provided in apriori algorithm
aprioriAlgo.py - This is the main algorithm file. The algorithm will provide information about products and the segment you want information about. Currently we have used Fruits and High Consumer.
prepareData.py - This program will help us rename columns, prepare segments, define spending variables and prepare data according to these requirements. We will also be performing clustering to cluster the data according to the Income and Spending.
readData.py - This file will help you read the data from the csv and remove na/null values from the data.
plotData.py - This will help in plotting data in graphical format.

Output: The output will be written in output.txt file in the customer data folder. The location is provided in the main python program file.

Apriori Algorithm:
This algorithm refers to an algorithm that is used in mining frequent products sets and relevant association rules. Generally, the apriori algorithm operates on a database containing huge number of transactions. The parameters used are "Support" and "Confidence" are used. Support refers to items' frequency of occurence; confidence is a conditional probability. Items in a transaction from an item set. Example of this algorithm is customers buying a lot of goods from a grocery store, by applying this method of the algorithm the grocery stores can enhance their sales performance and could work effectively.
