import numpy as np
import csv
import math

met = list(csv.reader(open('data/metadata.csv')))
tempo = int(met[0][0])
bpm = int(met[1][0])
tpb = int(met[2][0])
t_ptc =int(met[3][0])
t_amp = int(met[4][0])
t_dur = float(met[5][0])

num_patterns = 3
lbl = []

pat = []
for i in range (0, num_patterns):
 lbl.append(i+1)
 patfile = 'data/pat_' + str(i) + '.csv'
 pt = []
 with open(patfile) as csvfile:
  rdr = csv.reader(csvfile, quoting=csv.QUOTE_NONNUMERIC)
  for row in rdr:
   pt.append(row)
 pat.append(pt)

test_data = []
with open('data/test_data.csv') as csvfile:
 rdr = csv.reader(csvfile, quoting=csv.QUOTE_NONNUMERIC)
 for row in rdr:
  test_data.append(row)

def check_pat(pat_in, pat_ref):
 res = 0
 if len(pat_in) == len(pat_ref):        
  for i in range (0, len(pat_in)):
   if ((pat_in[i][0] >= pat_ref[i][0]-t_ptc) and (pat_in[i][0] <= pat_ref[i][0]+t_ptc)): 
     res = res+1
   if ((pat_in[i][1] >= pat_ref[i][1]-t_amp) and (pat_in[i][1] <= pat_ref[i][1]+t_amp)): 
    res = res+1
   if ((pat_in[i][2] >= pat_ref[i][2]-t_dur) and (pat_in[i][2] <= pat_ref[i][2]+t_dur)): 
    res = res+1
 if res == len(pat_ref)*3:
  return 1
 else:
  return 0

res = []
for i in range (0, len(test_data)):
 p = 0
 for j in range(0, len(pat)):
  pt = [] 
  if (len(test_data)-i) >= len(pat[j]):
for k in range (0, len(pat[j])):
 pt.append(test_data[i+k]) 
  if check_pat(pt, pat[j])==1:
p = j+1
 res.append(p)

print(res)