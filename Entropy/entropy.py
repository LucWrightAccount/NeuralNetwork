import csv
import math
from typing import Counter
import numpy as np
import pandas as pd

def entrpy():
    df = pd.read_csv('data.csv')

    print(df.head())

    interval = 55
    size = len(df)
    # A set that holds the two interval e_1 and e_2
    #  = e_1 is a set(Set[0]) of value:key pairs that are below the interval
    # Set is a set(Set[1]) of value:key pairs that are equal to or above the interval
    set_1 = []
    set_2 = []
    for index, row in df.iterrows():
        value = row.iloc[1]
        id_class = row.iloc[2]

        if value < interval:
            set_1.append((value, id_class))
        else:
            set_2.append((value, id_class))

    X = [set_1, set_2]
    entropy_weighted = []
    entropy_total = 0
    # "i" is the index of array X
    for i in range(len(X)):
        print(f"set_ {i+1}")
        P = 0
        F = 0
        entropy_set = []
        entropy = 0
        size = len(X[i])


        # j is indext of set i in X
        for j in range(len(X[i])):
            if 'P' in X[i][j]:
                P+=1
            else:
                F+=1

        print("P:", P)
        print("F:", F)

        if P > 0:
            entropy_set.append(
            (P/size) * math.log2(P/size)
        )

        if F >0:
            entropy_set.append(
                    (F / size) * math.log2(F / size)
                )

        for value in entropy_set:
            entropy += value

        entropy*=-1

        print("Entropy:", entropy)
        weighted_entropy = (len(X[i])/(len(set_1)+len(set_2))) * entropy
        entropy_weighted.append(weighted_entropy)
        print("Weighted entropy:", weighted_entropy)

    total = 0
    for value in entropy_weighted:
        total += value

    print("Total entropy:", total)

# Determines how many intervals there is 
def seperations():
    
    sep_count = int(input("How many seperations:" ))
    seperation_set = set()

    for i in range(sep_count):
        seperation_set.add(int(input(f"Enter digit {i+1}: ")))

    seperation_set = sorted(seperation_set)
    return seperation_set

#User GUI
def main():

    # Readss the CSV file for values
    # Column 0 Holds key(1,2,3,4)
    # Column 1 Holds Data values
    # Column 3 Holds values

    # CSV Reader
    df = pd.read_csv('data.csv')
    print(df)
    #Column Index for data
    value_index = 1

    #Column Index for Class
    class_index = 2

    #Gets the intervals ex. (2,3,4)
    seperation_set = seperations()

    #Changes e_i
    i=0

    #data variables in data_table
    total = 0

    #Makes interval_set + 1 range of intervals
    Interval_set = [[]for _ in range(len(seperation_set)+1)]
    #Class_set
    class_set = set()
    #Iterates through each row puting the tuple (value, class) in the interval_set
    for _, row in df.iterrows():
            
            value = row.iloc[value_index]
            id_class = row.iloc[class_index]

            #Gathers all the classes
            class_set.add(id_class)
            #Changes Seperation when length of seperation set is met
            #Changes when the vale is greater than the intercal
            while i < len(seperation_set) and value > seperation_set[i]:
                i+=1

            #Adds tuble to set/list
            Interval_set[i].append((value, id_class))
            total+=1


    #Occurance per set {A : 3, B : 2}
    class_counter = []

    #Total per set {5}
    class_total = []
    for interval in Interval_set:
        counts = []
        total_count = 0
        for class_name in class_set:
            count = 0
            
            for value, id_class in interval:
                if id_class == class_name:
                    count += 1
                    total_count +=1
            counts.append(count)
        class_total.append(total_count)



        class_counter.append(counts)


    print("Class_counter :",class_counter)
    print("Class_total:", class_total)
    #entropy set
    entropy_list = []
    #entropy is the probability of class i/m(set size) * log 2(i/m(set size))
    for i,count in enumerate(class_counter):
        entropy = 0
        for number in count:
            if(number > 0):
                entropy -= number/class_total[i]*math.log2(number/class_total[i])
        
        entropy_list.append(entropy)

    print("Entropy_list :", entropy_list)
    weigted_entropy = []
    for i,e_i in enumerate(entropy_list):
        weight = class_total[i]/total
        we_i = weight * e_i
        print(f"e_{i+1}", e_i)
        print("weight:", weight)
        print(f"we_{i}", we_i)
        weigted_entropy.append(we_i)

    print("Weighted entropy",weigted_entropy)
    sum_we = sum(weigted_entropy)

    print(sum_we)


if __name__ == "__main__":
    main()