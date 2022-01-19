"""
Author: Siddhant Mahajani
main.py - Main program to perform customer analysis
"""

from data.read import readData
from data.prepare import prepareData
# from data.plot import plotData
from algorithm import aprioriAlgo
import warnings

warnings.filterwarnings('ignore')


def main():
    data = readData.read(location='customer-data/customer-data.csv')
    # getDataInsights(data)
    spendingVariableData = prepareData.getspendingvariables(data)
    updatedData = readData.removenull(spendingVariableData)
    clusteredData = prepareData.performclustering(updatedData)
    # plotData(summaryData)
    preparedData = prepareData.datapreparation(clusteredData)
    result = aprioriAlgo.performanalysis(preparedData)
    readData.writedata(str(result), location='customer-data/output.txt')
    print('Analysis complete. Please check the data folder for output.')


if __name__ == "__main__":
    main()
