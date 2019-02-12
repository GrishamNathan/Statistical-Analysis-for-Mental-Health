import os 
import pandas as pd
os.chdir('C:/Users/grish/Desktop/Workstudy/Rashid_workstudy/Stress/')

blank_99=pd.read_excel('Flourish_Data_For Grisham_N_Jan 2018..xlsx')
blank_99_removed=blank_99
unique=blank_99.externalid.unique()

for k in unique:
    store=blank_99[blank_99['externalid']==k]
    dates=store.groupby(['responsedate'])['responsedate'].agg(['count'])
    duplicate_date=[]
    
    for i in range(0,(dates.shape[0])):
        if (dates.iloc[i,0]>=2):
            duplicate_date.append(dates.index.values[i])    
    
    for i in range(0,len(duplicate_date)):
        student_duplicate_date=blank_99[(blank_99.externalid==k) & (blank_99.responsedate == duplicate_date[i])]
        duplicate_indices=pd.merge(student_duplicate_date,blank_99,left_index=True,right_index=True)
        for j in duplicate_indices.index.values:
            if j != max(duplicate_indices.index.values):
                blank_99_removed=blank_99_removed.drop(j)
