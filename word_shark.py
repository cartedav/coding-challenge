# -*- coding: utf-8 -*-
"""
Created on Thu Oct 01 18:30:22 2015

@author: David
"""

from collections import defaultdict

def main():
    
    # Ask user for filename
    filename = raw_input('Enter the name of the dictionary file: ')
    
    # Open dictionary file to read words
    file = open(filename)
    
    # The first 26 prime numbers
    letter_values = [2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37, 41, 43, 47, 53, 59, 61, 67, 71, 73, 79, 83, 89, 97, 101]
    
    # Offset value to convert ASCII value to 0-25 (indexing)
    offset = 97
    
    # Defaultdict to organize words by total value
    organized_words = defaultdict(list)
    
    # Set to keep all unique values of words
    unique_values = set()
    
    # Iterate over each word (line) in dictionary
    for line in file:
        
        # Remove newline characters
        word = line.rstrip('\n')
        
        # To begin, each word has a value of 1
        value = 1        
        # Iterate over each letter in the word
        for i in word:
            # The total value of each word is the product of the value of each letter
            value *= letter_values[ord(i) - offset]
        
        # Add word and value to dictionary
        organized_words[value].append(word)
        
        # Add value to set of all unique values
        unique_values.add(value)

    # Close the filestream  
    file.close()
    
    # for each value in the set of unique values
    for number in unique_values:
        # access list of words with that value
        matching_words = organized_words[number]
        
        # If there are at least as many words with that value as there 
        # are letters in those words (as many anagrams as letters)
        if (len(matching_words) >= len(matching_words[0])):
            # Create blank string
            to_print = ''
            # for each word with that value
            for word in matching_words:
                # Add word to string that will be printed
                to_print += word + ', '
            # Remove final blank space
            to_print = to_print[:-1]
            # Remove final ','
            to_print = to_print[:-1]   
            # Print string of words with that particular value
            print(to_print)
    
if __name__ == "__main__":
    main()
