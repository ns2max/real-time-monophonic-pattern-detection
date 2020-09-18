import numpy as np
import random
import csv

num_patterns = 3
num_positive = 50
num_negative = 50

met = list(csv.reader(open('data/metadata.csv')))
tempo = int(met[0][0])
bpm = int(met[1][0])
tpb = int(met[2][0])
t_ptc =int(met[3][0])
t_amp = int(met[4][0])
t_dur = float(met[5][0])

pat = []
lbl = []
for i in range (0, num_patterns):
 lbl.append(i+1)
 patfile = 'data/pat_' + str(i) + '.csv'
 pt = []
 with open(patfile) as csvfile:
  rdr = csv.reader(csvfile, quoting=csv.QUOTE_NONNUMERIC)
  for row in rdr:
   pt.append(row)
 pat.append(pt)

##find longerst pattern and normalize lengt)
longest_len = len(max(pat, key=len))
pat_equalized = np.copy(pat)
for i in range(0, len(pat_equalized)):
 for j in range(0, longest_len - len(pat_equalized[i])):
  pat_equalized[i].append([999, 999, 999])

#positive dataset
def rand_pos(val, delta, lower, upper, flag):
 if(flag == 0):
  res = 0
  if(val-delta > lower and val+delta < upper):
   res = random.randint(val-delta, val+delta)   
  elif(val-delta <= lower):
   res = random.randint(lower, val+delta)
  elif(val+delta >= upper):
   res = random.randint(val-delta, upper)   
 if(flag == 1):
  res = 0
  if(val-delta > lower and val+delta < upper):
   res = random.uniform(val-delta, val+delta)   
  elif(val-delta <= lower):
   res = random.uniform(lower, val+delta)   
  elif(val+delta >= upper):
   res = random.uniform(val-delta, upper)   
 res = round(res, 2)
 return res


#negative dataset
def rand_neg(val, delta, lower, upper, flag):
 if(flag == 0):  
  if(val-delta <= lower):
   res = random.randint(val+delta, upper)
  elif(val+delta >= upper):
   res = random.randint(lower, val-delta)
  else:
   rangechoices = ((lower,val-delta), (val+delta, upper))
   fromrange = random.choice(rangechoices)
   res = random.randint(*fromrange)   
 if(flag == 1):  
  if(val-delta <= lower):
   res = random.uniform(val+delta, upper)
  elif(val+delta >= upper):
   res = random.uniform(lower, val-delta)
  else:
   rangechoices = ((lower,val-delta), (val+delta, upper))
   fromrange = random.choice(rangechoices)
   res = random.uniform(*fromrange)   
 res = round(res, 2)
 return res

#creating positive variants
def create_pos(patt, lbll, dst_pat, dst_lbl): 
 for j in range(0, num_positive):
  tmp = []
  for i in range (0, len(patt)):
   ptc_i = patt[i][0]
   amp_i = rand_pos(patt[i][1], t_amp, 0, 127, 0)
   dur_i = rand_pos(patt[i][2], t_dur, 0, 2.0, 1)

   tmp.append([ptc_i, amp_i, dur_i])

  dst_pat.append(tmp)  
  dst_lbl.append(lbll)
  
  
#create amplitude variations from +-1 to +-20
def ampl(patt, lbll, dst_pat, dst_lbl):
 for j in range(-20, 21):
  tmp = []
  for i in range (0, len(patt)):
   ptc_i = patt[i][0]
   amp_i = patt[i][1] - j
   dur_i = patt[i][2]
   
   tmp.append([ptc_i, amp_i, dur_i])

  dst_pat.append(tmp)  
  dst_lbl.append(lbll)
  
  
def create_neg(patt, lbll, dst_pat, dst_lbl):
 for j in range(0, num_negative):
  tmp = []
  for i in range (0, len(patt)):

   ptc_i = rand_neg(patt[i][0], t_ptc, 0, 127, 0)
   amp_i = rand_neg(patt[i][1], t_amp, 0, 127, 0)
   dur_i = rand_neg(patt[i][2], t_dur, 0, 2.0, 1)

   tmp.append([ptc_i, amp_i, dur_i])

  dst_pat.append(tmp)  
  dst_lbl.append(0)

pos_pat = []
pos_lbl = []


for ii in range (0, len(pat_equalized)):
# for ii in range (0, 1):
 pt = pat_equalized[ii]
 
 pos_tmp = []
 varient = False
 
 for i in range (0, len(pt)):
  if pt[i][0]==999 and pt[i][1]==999 and pt[i][2]==999:
   varient = True
 
 if varient == True:
  ##10 variants for padded digit
  for i in range (0, 10):
   pat_tmp = []
   for i in range(0, len(pt)):
				if pt[i][0]==999 and pt[i][1]==999 and pt[i][2]==999:
					n = [random.randint(0,127), 
						random.randint(0,127), 
						round(random.uniform(0,2.0), 2)]
					pat_tmp.append(n)
				else:
					pat_tmp.append(pt[i])   
   pos_tmp.append(pat_tmp)
 else:
  pos_tmp.append(pt)
  

 for i in range(0, len(pos_tmp)):
  create_pos(pos_tmp[i], lbl[ii], pos_pat, pos_lbl)
  ampl(pos_tmp[i], lbl[ii], pos_pat, pos_lbl)

neg_pat = []
neg_lbl = []

#create negative variants
def create_neg(patt, lbl):
 for j in range(0, num_negative*2):
  tmp = []
  for i in range (0, len(patt)):

   ptc_i = rand_neg(patt[i][0], t_ptc, 0, 127, 0)
   amp_i = rand_neg(patt[i][1], t_amp, 0, 127, 0)
   dur_i = rand_neg(patt[i][2], t_dur, 0, 2.0, 1)

   tmp.append([ptc_i, amp_i, dur_i])

  neg_pat.append(tmp)  
  neg_lbl.append(lbl)

  
for i in range(0, len(pat_equalized)):
 create_neg(pat_equalized[i], 0)
 
train_pat = pos_pat + neg_pat
train_lbl = pos_lbl + neg_lbl

with open('snn/data/train_data.csv', mode='w', newline='') as f:
 data_writer = csv.writer(f)
 
 for i in range(0, len(train_pat)):
  tmp = np.asarray(train_pat[i])
  tt = []
  for j in range(0, len(tmp)):
   for k in range(0, len(tmp[j])):
    tt.append(tmp[j][k])
  data_writer.writerow(tt)
  
   
with open('snn/data/train_labels.csv', mode='w', newline='') as f:
 data_writer = csv.writer(f)
 
 for i in range(0, len(train_lbl)):
  tt = []
  tt.append(train_lbl[i])
  data_writer.writerow(tt)