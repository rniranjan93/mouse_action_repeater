import csv
import pyautogui as py
with open('exam.csv') as csvfile:
 read=csv.reader(csvfile,delimiter=',')
 for row in read:
  if row==[]:
   continue
  else:
   if row[0]=='left':
    py.click(int(row[1]),int(row[2]),button='left',duration=float(row[3]))
   else:
    py.scroll(int(row[0]))