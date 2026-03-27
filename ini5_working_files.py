outputFile=[]

with open("C:\\Users\\SRIJATO\\OneDrive\\Documents\\Python\\Rosalind python village\\input.txt", 'r') as f:
    outputFile= [line for pos, line in enumerate(
        f.readlines()) if pos % 2 != 0]
    
with open("C:\\Users\\SRIJATO\\OneDrive\\Documents\\Python\\Rosalind python village\\output.txt", 'w') as f:
    f.write(''.join([line for line in outputFile]))