#*******
#* Read input from STDIN
#* Use: echo or print to output your result to STDOUT, use the /n constant at the end of each result line.
#* Use: sys.stderr.write() to display debugging information to STDERR
#* ***/
import sys

lines = []
for line in sys.stdin:
	lines.append(line.rstrip('\n'))
	
nb_cartons = int(lines[0])
voyage = poids = 0
i = 1

while i <= nb_cartons:
    poids += int(lines[i])
    
    if poids > 100 :
        poids = 0
        voyage += 1
        i -= 1
        
    i += 1
        
if poids > 0 :
    voyage += 1
    
print(voyage)