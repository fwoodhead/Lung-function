# Script to display pulmonary function(PFT) data using python
# Written by Felix Woodhead 30/9/2017

# set location of excel file which will be the origin
# requires os (import if not previously done)

import pandas as pd
import os

#change this to directory where file resides
SOURCE_DIR = r"C:\Users\Dell\Google Drive\Python code\Database and webscrape Feb 2017"

SOURCE_FILE = "Glen_ILD_GLIout.xlsx"

# reads excel file into pandas dataframe
df = pd.read_excel(os.path.join(SOURCE_DIR, SOURCE_FILE), header=0)

# uncomment line below to check dataframe is correctly loaded
# df.head()

# group by patient (stored in variable 'idAnonCode')
grouped = df.groupby('idAnonCode')


# prints PFTs grouped by patient
# uncomment if needed

# for idAnonCode, group in grouped:
#        print(idAnonCode)
#        print(group)

# Store one patient's PFT data as new variable, G7
G7 = df.loc[df['idAnonCode']=='GILD0007']

import matplotlib.pyplot as plt
G7.plot(x='pftDate',y='fvc', kind='line')

# needs invoking to show plot
# this is dependent on the 'backend'
plt.show()

# plots line graph which is lue ('b'), has filled points ('o'), and normal line ('-')
plt.plot(G7['pftDate'],G7['FVCPercentPred'], 'bo-')
plt.show()


# Again, don't forget to use plt.show() to display
def printPFT(ID,MasterList = df, PtCode = "idAnonCode", DateLabel = "pftDate", PFTvar = "FVCPercentPred"):
    """Prints PFTs as a MatLabPlot graph"""
    import matplotlib.pyplot as plt
    
    PtSeries = MasterList.loc[MasterList[PtCode]==ID]
    plt.ylabel(PFTvar)
    plt.title(ID)
    plt.xticks(rotation='vertical')
    plt.plot(PtSeries[DateLabel],PtSeries[PFTvar], 'bo-')

def PFTSeriesChange(ID, MasterList = df, PtCode = "idAnonCode", DateLabel = "pftDate", PFTvar = "FVCPercentPred"):
    """Returns rate of change of parameter per year"""
    
    PtSeries = MasterList.loc[MasterList[PtCode]==ID]
    dtSeries = PtSeries[DateLabel]
    pftSeries = PtSeries[PFTvar]
    
    DeltaPFT = [j-i for i, j in zip(pftSeries[:-1], pftSeries[1:])] # Difference in PFT
    DeltaDate = [j-i for i, j in zip(dtSeries[:-1], dtSeries[1:])] # Difference in date
    DaysDeltaDate = [dt.days for dt in DeltaDate] # Date difference in days as float
    
    my_list = [x/y for x, y in zip(DeltaPFT, DaysDeltaDate)] 
    return [i * 365.25 for i in my_list]

