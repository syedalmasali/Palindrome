""" 
This program reads in a text file as a single string.

Usage: python palindrome.py inputFile
 (requires an input text file)
"""


from sys import argv,exit

def readFile(fname):
  """
  input: the name of a text file which contains text
  output: a single string which is the entire file contents
  """
  f = open(fname)
  finalString = ""
  for line in f:
    finalString += line # concatenate it!
  return finalString


def main():
  if len(argv) != 2:
    print("usage %s <number> <inputFile>" % argv[0])
    exit()

  s = readFile(argv[1]) # this is the string
  

  start= 0 #starting index for palindrome
  maxlength = 1 #length of max plaindrome which is 1 b/c a letter is a palindrome
  n = len(s) #length of string

  #searched up how to make 2d array
  array = [[0]*n]*n

  #make the diagnaols a palindrome bc a letter is a plaindrome
  for i in range(n):
    array[i][i] = 1

  #check to see if the ith term is the same as i+1 term
  #split up because easier to check if "aa" instead of "aba"
  for i in range(n - 1): #have to range to n-1 b/c last term cannot have a next term
    if s[i] == s[i + 1]:
      array[i][i + 1] = 1
      start = i
      maxlength += 1
        
  for i in range(3, n+1): #start at 3 because we checked first 2 letter already and +1 for last term
    for j in range(n-i+1): #subtract i to keep indexes legal and +1 for the last term
      last = j+i-1  # Ending index of the inner string
      #Check to see if the shorter string is a palindrome and the inner substring is a palindrome. 
      if array[j+1][last-1] and s[j] == s[last]:
        array[j][last] = 1
        start = j
        maxlength = i

  l = maxlength
  pal = s[start:start+maxlength] #index slices

  print("The length of the longest palindrome is %d." % l)
  print("The longest palindrome is: %s" % pal)
  
main()
