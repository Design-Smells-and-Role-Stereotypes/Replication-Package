import os
import re
import csv


def write_csv_data(basepath, files, regex):
    anti_patternlist = ['SpeculativeGenerality', 'BaseClassKnowsDerivedClass', 'MessageChains',
                        'LongParameterList', 'SpaghettiCode', 'BaseClassShouldBeAbstract',
                        'LongMethod', 'ClassDataShouldBePrivate', 'TraditionBreaker',
                        'ManyFieldAttributesButNotComplex', 'RefusedParentBequest', 'SwissArmyKnife',
                        'Blob', 'AntiSingleton', 'ComplexClass', 'LargeClass', 'FunctionalDecomposition',
                        'LazyClass']
    header = ['FullClassPath', 'AntiPattern']
    datas = files
    for data in datas:
        for ap in anti_patternlist:
            search = re.search(ap, data)
            if search != None:
                anti_pattern = search.group()
                filename = f'{basepath}{anti_pattern}.csv'
                # write header
                try:
                    f = open(filename, 'w')
                    writer = csv.DictWriter(f, fieldnames=header)
                    writer.writeheader()
                    f.close()
                except Exception as e:
                    print("ERROR: could not write .csv header", e)
            else:
                continue
        try:
            f = open(data, 'r')
            content = f.read()
        except Exception as e:
            print("ERROR: failed to read file! ", e)
        r = re.compile(regex)  # e.g. regex=k9mail[a-zA-Z0-9.-]+
        matched_str = r.findall(content)
        if len(matched_str) != 0:
            # write to csv
            print(len(matched_str))
            to_write = []
            for cl in matched_str:
                # create a pair of classnames and anti_pattern
                to_write = [cl, anti_pattern]
                try:
                    with open(filename, 'a', newline='') as file:
                        writer = csv.writer(file, delimiter=',')
                        writer.writerow(i for i in to_write)
                except Exception as e:
                    print("ERROR: failed to write data in the .csv file! ", e)
