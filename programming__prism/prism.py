"""
Data Mining Fall 2018
Programming Assignment 01: Implementation of the PRISM algorithm
Name: Kyoosik Kim

The program can work on both numerical and categorical data set.
It prints all steps and shows rules found at the end.
Results are susceptible to overfitting By the nature of the algorithm. (long list of rules)
Details can be found in the "rule_generator" file in which the functions are written.
"""

import pandas as pd
from rule_generator import *

FILENAME = 'sample01.csv'


if __name__ == '__main__':
    input_df = pd.read_csv(FILENAME, encoding="utf-8")
    final_rules = {} # {class: (rule1, accuracy), (rule2, accuracy), ...}

    # attributes
    attr_list = list(input_df.columns)

    # most common class to rarest class
    class_order = input_df['class'].value_counts(ascending=True)
    classes = class_order.index
    final_rules[str(classes[-1])] = ['default'] # most common class

    df = input_df
    for class_val in classes[:-1]: # iterate attributes
        print("\n*** Candidates of Rule for Class " + '"' + str(class_val) + '" ***\n')
        print("<Current Data Frame>\n\n", df.sort_values(by=['class']))

        final_rules[str(class_val)] = []
        threshold = class_order[class_val]/len(input_df) # obs of the class / total obs

        # refine a rule
        while len(df[df['class']==class_val]) != 0:
            rule = rule_finder(df, class_val, list(input_df.columns[:-1]), [])
            df, accu = remove_instances(df, class_val, rule)
            if accu > threshold: # at least more accuate than random picks
                final_rules[str(class_val)].append((rule, accu))

    print("\n*** Attributes ***\n", attr_list[:-1])
    print("\n*** Classes ***\n", list(classes), "\tdefault class: ", str(classes[-1]))
    print("\n*** All Rules ***")
    pprint.pprint(final_rules)
