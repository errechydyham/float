text = "X-DSPAM-Confidence:    0.8475"

#find the index of 0 
x = text.find("0")

#slice the number and turn it into float 
n = float(text[x:]) 

#print the number 
print(n)