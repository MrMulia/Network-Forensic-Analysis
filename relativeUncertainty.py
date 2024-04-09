import math
import sys

def calculate(fileName):
    try:
        #opens file 
        file = open(fileName, "r") 
    except:
        print("File doesn't exist")

    #get lines
    lines = file.readlines()

    #counts each line
    idx = 0
    idx += 1
    value = ""
    dict = {}
    for line in lines: #for each line/value in file
      idx += 1
      value = line.strip() #make it int, get rid of formatting
      if value not in dict.keys():
        dict[value] = 1
      else:
        dict[value] += 1

    idx = idx - 1

    #print("Final count:", idx)

    MaxEntropy = math.log(idx, 2)
    #print("Max Entropy: ",  MaxEntropy)

    #For each key
    mathWork = 0
    Entropy = 0
    for keys in dict.keys(): 
      appearance = dict[keys] 
      whole = idx
      propability = float(appearance) / float(whole)
      mathWork = (propability*(math.log(propability, 2)))*(-1)
      Entropy = mathWork + Entropy #adds up each keys Entropy
      
    #print("Entropy: ", Entropy)


    #To get entropy between 0 and 1
    standardEntropy = Entropy / MaxEntropy
    print(round(standardEntropy, 3))

#ex6
print("\nRelative Uncertainty:")

if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: python relativeUncertainty.py <filename>")
        sys.exit(1)

    fileName = sys.argv[1]
    calculate(fileName)

