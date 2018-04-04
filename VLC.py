"""
language: python3
description: To determine codeword and frequency of symbols in the file and also calculate the VLC and Fixed length
             codeword length.
"""

import heapq
import math


#List for heapq is created
h = []

#Dictionary for mapping the symbols and their frequency is created.
d={}

def file_reading():
    """
        This function reads the file contents , calculates the frequency and determine the codeword of the symbols in file.
        This function also implements heapq for further implementations.
        This function also calculates the VLC and Fixed length codeword length.
    """

    # It prompts the user to type the filename
    fname=input("Enter the file name")

    # It opens the file and performs following computations
    with open(fname) as f:
        for line in f:

            #It inserts or updates the key and values in dictionary based on the conditions.
            for x in line.strip():
                if x not in d:
                    d[x]=1
                else:
                    d[x]=d[x]+1


        #It pushes the elements in the heapq
        for x in d:
            heapq.heappush(h, [d[x],[[d[x], [], x]]])

        #It computes the codeword for the symbols
        while (len(h)>1):
            a=heapq.heappop(h)
            b=heapq.heappop(h)
            if a<b:
                for x in a[1]:
                    L = x[1]
                    x[1] = [0] + L
                for x in b[1]:
                    L = x[1]
                    x[1] = [1] + L
            else:
                for x in a[1]:
                    L = x[1]
                    x[1]=[1]+L
                for x in b[1]:
                    L = x[1]
                    x[1] = [0] + L

            #It calculates the cumulative frequency
            cum_freq=a[0]+b[0]
            c = [cum_freq, a[1] + b[1]]

            heapq.heappush(h,c)

        print("Variable Length Code Output")
        print("-------------------------------------")
        popped_element=heapq.heappop(h)
        for x in popped_element[1]:
            print('symbol:  %2s'%x[2],' Codeword:  %12s'%x[1],'  Frequency:    %5s'%x[0])

        #It calculates the Average VLC codeword length
        sum_num = 0
        sum_den = 0
        for x in popped_element[1]:
            prod=(len(x[1]))*x[0]
            sum_num=prod+sum_num
            sum_den=x[0]+sum_den
        vlc_code_length=sum_num/sum_den
        print("Average VLC codeword length is:",vlc_code_length,"bits per symbol")

        #It calculates the Average Fixed length codeword length
        length = 0
        for x in popped_element[1]:
            for y in x[2]:
                length+=1
        a = math.log(length,2)
        answer = math.ceil(a)
        print("Average Fixed length codeword length is:",answer,"bits per symbol")


        print()



def main():
    """
           This function calls the function file_reading.
    """
    file_reading()

if __name__ == '__main__':
    #main() is called
    main()