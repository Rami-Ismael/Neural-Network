from tkinter import *
import random
import sys; 
print(sys.version)
WIDTH=1000
HEIGHT = 1000
root = Tk()

myCanvas = Canvas(root, width=WIDTH, height=HEIGHT)
myCanvas.pack()
myCanvas.create_line(0,0,500,500)
def sign(n):
  if(n>=0):
    return 1
  else:
    return -1
    #create a perceptron

class perceptron:
  
  
  def __init__(self,n):
    self.weight =[]
    self.lr = 0.01
    for x in range(n-1):
      # random unifrom function will give a r radnom float between -1 and 1
      self.weight.append(random.uniform(-1,1))
 #reeive the input 
  def perceptronThinks(self,input):
    sum=0.0
    #take the dot porduct of the two matrix
    for w,i in zip(self.weight,input):
      sum+=w*i
    output = sign(sum)
    return output
  def train(self,input,target):
    estimate = self.perceptronThinks(input)
    error = target-estimate
    list = []
    #tune all the weight to get the right value
    for i,w in zip(input,self.weight):
      list.append(w+(error*i*self.lr))
    self.weight = list

brain = perceptron(20)
def create_circle(x, y, r, canvasName,color): #center coordinates, radius
    x0 = x - r
    y0 = y - r
    x1 = x + r
    y1 = y + r
    return canvasName.create_oval(x0, y0, x1, y1,fill=color)
#create a class in python that only hold x and y val

class Point:
  def __init__(self, x, y,color):
    self.x = x
    self.y = y
    self.color = color
# have a list of circle
points =[]
#create a 20 circle split my y= mx line taht will be trianing data
for z in range(200):
  x = random.randint(1,500)
  y= random.randint(1,500)
  if(x>y):
    points.append(Point(x,y,1))
  if(x<y):
    points.append(Point(x,y,-1)) 

# Python3 code to iterate over a list 
# Using for loop 
for obj in points: 
  if(obj.color==1):
   create_circle(obj.x, obj.y, 3, myCanvas,"red")
  else:
    create_circle(obj.x, obj.y, 3, myCanvas,"blue")
  

'''
#supervised Learning
#1 rpovide the preception iwth inputs for which there is a know answer
#ask the perceptron to gueess an answer
#3 copmuter the error
#4 Adjust all the weights acccdoirnd tot he error
#5 return to setp 1 adn repeat
weight = error *input
newweight = weight-error*input
'''
'''
for al lthe points
'''
for p in points:
  list =[]
  list.append(p.x)
  list.append(p.y)
  guess =brain.perceptronThinks(list)
  target = p.color
  if(guess==target):
     create_circle(p.x, p.y, 3, myCanvas,"green")
  else:
    create_circle(p.x, p.y, 3, myCanvas,"pink")

dis = 500
myCanvas.create_line(500,0,500,1000)
myCanvas.create_line(500,0,1000,500)
for p in points:
  list =[]
  list.append(p.x)
  list.append(p.y)
  
  brain.train(list,p.color)

  guess =brain.perceptronThinks(list)
  target = p.color
  if(guess==target):
     create_circle(p.x+dis, p.y, 3, myCanvas,"green")
  else:
    create_circle(p.x+dis, p.y, 3, myCanvas,"pink")    
myCanvas.create_line(0,500,500,1000)
for p in points:
  list =[]
  list.append(p.x)
  list.append(p.y)
  
  brain.train(list,p.color)

  guess =brain.perceptronThinks(list)
  target = p.color
  if(guess==target):
     create_circle(p.x, p.y+dis, 3, myCanvas,"green")
  else:
    create_circle(p.x, p.y+dis, 3, myCanvas,"pink")    


root.mainloop()
