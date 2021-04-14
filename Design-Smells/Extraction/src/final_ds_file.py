import os
import pandas as pd
import numpy as np
import re
def final_ds_output(input_path, out_path):
    anti_patternlist = ['SpeculativeGenerality', 'BaseClassKnowsDerivedClass','MessageChains', 
                    'LongParameterList', 'SpaghettiCode', 'BaseClassShouldBeAbstract',
                    'LongMethod', 'ClassDataShouldBePrivate', 'TraditionBreaker', 
                    'ManyFieldAttributesButNotComplex', 'RefusedParentBequest', 'SwissArmyKnife',
                    'Blob', 'AntiSingleton', 'ComplexClass', 'LargeClass', 'FunctionalDecomposition',
                    'LazyClass']
    frames = []
    for ap in anti_patternlist:
        filename = os.sep.join([input_path] + [f'{ap}.csv'])
        dataframe = pd.read_csv(filename)
        frames.append(dataframe)
    project_ds = pd.concat(frames)

    # create a new dataframe
    project_ds_data = pd.DataFrame(columns=[anti_patternlist])
    project_ds_data.insert(0, 'FullClassPath', True)

    # create a list of unique class files
    unique_class = list(project_ds.FullClassPath.unique())
    project_ds_data['FullClassPath'] = unique_class

    # matrix construction and transformation
    index = 0;
    for i in unique_class:
        for j in range (0, len(project_ds['FullClassPath'])):
            if i == project_ds['FullClassPath'].iloc[j]:
                project_ds_data.at[index, 'FullClassPath'] = i
                project_ds_data.at[index, project_ds['AntiPattern'].iloc[j]] =1 # count
        index = index + 1

    # replace all nan with zeros
    project_ds_data = project_ds_data.fillna(0)
    print(project_ds_data.head())

    # write data to csv
    project_ds_data.to_csv(r'src/results/' + out_path)
    print("SUCCESS: ", "check src/results directory for the output")