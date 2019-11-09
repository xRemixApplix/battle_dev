#*******
#* Read input from STDIN
#* Use: echo or print to output your result to STDOUT, use the /n constant at the end of each result line.
#* Use: sys.stderr.write() to display debugging information to STDERR
#* ***/
import sys

lines = []
for line in sys.stdin:
	lines.append(line.rstrip('\n'))
	
###############################################	
place = int(lines[0])

def split_line(line) :
    line_tab = line.split()
    return int(line_tab[0]), int(line_tab[1])

for i in range(1, len(lines)):
    perdu, gagne = split_line(lines[i])
    place += perdu - gagne
    
if place <= 100 :
    gain = 1000
elif place <= 10000 :
    gain = 100
else :
    gain = "KO"
    
print(gain)