import pyHook
import pythoncom
import pyautogui as py
import csv
k=1
c=0
z=[]
l=[]
m=[]
p=[]
def left_down(event):
    global z
    global l
    global m
    global c
    if c!=0:
     m.append(0)
     l.append(str(c))
     z.append(py.position())
     c=0
    m.append(0)
    l.append('left')
    z.append(py.position())
    return True # if return false, the event will not be passed on to other programs. 
                # The cursor will appear freeze

def right_down(event):
    print ("right click")
    global k
    k=0
    return True  

def middle_down(event):

    print ("middle click")
    return True  
     
def OnKeyboardEvent(event):
	print(chr(event.Ascii))
	return True
def wheel(event):
    global c
    c=c+event.Wheel
    return True

hm = pyHook.HookManager()

# hook mouse
hm.SubscribeMouseLeftDown(left_down)
hm.SubscribeMouseRightDown(right_down)
hm.SubscribeMouseMiddleDown(middle_down)
hm.SubscribeMouseWheel(wheel)
hm.HookMouse()

#hook keyboard
hm.KeyDown = OnKeyboardEvent # watch for all keyboard events
hm.HookKeyboard()
while k:
 pythoncom.PumpWaitingMessages()
with open('exam.csv','r+') as f:
 writer=csv.writer(f)
 for i in range(len(l)):
  writer.writerow([l[i],z[i][0],z[i][1],0.3])
 f.close()

hm.UnhookMouse()
hm.UnHookKeyboard()