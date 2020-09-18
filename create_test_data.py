import numpy as np
import random
import csv
import mido
from mido import MidiFile

def generate_csv(filename, output_csv, met):
 mid = MidiFile(filename)

     
 if mid.tracks[0][1].type == 'set_tempo': 
  tempo = mid.tracks[0][1].tempo
  bpm = round(1000000*60/mid.tracks[0][1].tempo)
 else:
  tempo = mid.tracks[0][2].tempo
  bpm = round(1000000*60/mid.tracks[0][2].tempo)
 tpb = mid.ticks_per_beat

 # tolerances 
 t_ptc = 0
 t_amp = round(127*5/100)
 t_dur = (60/bpm)*0.05

 seq = []
 track = mid.tracks[0]
 for i in range (0, len(track)):
  if (track[i].type=='note_on'):        
   if(track[i].time > 0):
    ptc = 0
    amp = 0
    dur = mido.tick2second(track[i].time, tpb, tempo)
    seq.append([ptc, amp, dur])        
   ptc = track[i].note
   amp = track[i].velocity
   dur = mido.tick2second(track[i+1].time, tpb, tempo)
   seq.append([ptc, amp, dur])

   train_pat = np.asarray(seq)
   with open(output_csv, mode='w', newline='') as f:
    data_writer = csv.writer(f)    
    for i in range(0, len(train_pat)):
     tt = []
     for j in range(0, len(train_pat[i])):
      tt.append(train_pat[i][j])
     data_writer.writerow(tt) 

 if met == 1:
  with open('data/metadata.csv', mode='w', newline='') as f:
   data_writer = csv.writer(f)
   data_writer.writerow([tempo])
   data_writer.writerow([bpm])
   data_writer.writerow([tpb])
   data_writer.writerow([t_ptc])
   data_writer.writerow([t_amp])
   data_writer.writerow([t_dur])


generate_csv('midi/Scarified.mid', 'data/test_data.csv', 1)
generate_csv('midi/Scarified-p1.mid', 'data/pat_0.csv', 0)
generate_csv('midi/Scarified-p2.mid', 'data/pat_1.csv', 0)
generate_csv('midi/Scarified-p3.mid', 'data/pat_2.csv', 0)
